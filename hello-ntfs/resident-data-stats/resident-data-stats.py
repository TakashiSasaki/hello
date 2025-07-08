import os
import sys
import subprocess
import statistics
import ctypes
import argparse
import re
from tqdm import tqdm

SHOW_FSUTIL_OUTPUT = False

def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute file statistics with fsutil output display option."
    )
    parser.add_argument(
        "--show-fsutil-output",
        action="store_true",
        help="Display fsutil output and the executed command line for each file processed."
    )
    return parser.parse_args()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def request_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )

def get_short_path(long_path):
    """
    Returns the 8.3 short path for the given long path.
    If retrieval fails, returns the original long path.
    """
    buffer = ctypes.create_unicode_buffer(260)
    ret = ctypes.windll.kernel32.GetShortPathNameW(long_path, buffer, 260)
    if ret == 0:
        return long_path
    return buffer.value

def should_skip_file(file_path):
    """
    Returns True if the file should be skipped for fsutil processing.
    For example, skip files inside a .git directory.
    """
    return ".git" in file_path.lower()

def is_resident(file_path):
    """
    Check if the file's actual data is stored as resident data by analyzing the fsutil file layout output.
    Forces English output by relying on parent's code page set to cp437.
    Uses the short (8.3) path to avoid path syntax issues.
    Returns True if the file's data is resident, False if non-resident.
    """
    try:
        if not os.path.isfile(file_path):
            return False
        if should_skip_file(file_path):
            return False

        abs_file_path = os.path.abspath(file_path)
        short_path = get_short_path(abs_file_path)
        # Build the command as a list (without shell=True)
        cmd = ["fsutil", "file", "layout", short_path]
        if SHOW_FSUTIL_OUTPUT:
            print(f"\nExecuting command: {' '.join(cmd)}")
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="cp437"  # Use cp437 since parent's console is set accordingly.
        )
        output, error = proc.communicate()
        if SHOW_FSUTIL_OUTPUT:
            print(f"fsutil output for {file_path}:\n{output}")
            if error:
                print(f"fsutil error for {file_path}:\n{error}")
        if proc.returncode != 0:
            return False

        output_lower = output.lower()
        # Extract the ::$DATA stream block from the output.
        data_block = ""
        for block in output_lower.split("stream"):
            if "::$data" in block:
                data_block = block
                break

        if not data_block:
            # $DATA stream not found, unable to determine residency.
            return False

        # If "no clusters allocated" is found, data is resident.
        if "no clusters allocated" in data_block:
            return True
        # If "has parsed information" is found, data is non-resident.
        if "has parsed information" in data_block:
            return False

        # Otherwise, compare size vs allocated size.
        size_match = re.search(r"size\s+:\s+([\d,]+)", data_block)
        alloc_match = re.search(r"allocated size\s+:\s+([\d,]+)", data_block)
        if size_match and alloc_match:
            size_val = int(size_match.group(1).replace(",", ""))
            alloc_val = int(alloc_match.group(1).replace(",", ""))
            # Typically, resident means allocated size is nearly equal to size.
            if alloc_val > size_val:
                return False
            else:
                return True

        return False
    except Exception as e:
        if SHOW_FSUTIL_OUTPUT:
            print(f"Exception occurred for {file_path}: {e}")
        return False

def compute_stats(data):
    count = len(data)
    if count == 0:
        return count, None, None, None, None, None
    mean = statistics.mean(data)
    stdev = statistics.stdev(data) if count > 1 else 0
    min_value = min(data)
    max_value = max(data)
    median_value = statistics.median(data)
    return count, min_value, max_value, median_value, mean, stdev

def main():
    # Set parent's console code page to cp437 to force English output for fsutil.
    os.system("chcp 437 > NUL")
    
    resident_file_sizes = []
    nonresident_file_sizes = []
    all_file_sizes = []
    zero_byte_count = 0

    all_file_paths = []
    all_dir_entries = list(os.walk("."))
    for root, dirs, files in tqdm(all_dir_entries, desc="Collecting files", unit="dir"):
        for file in files:
            file_path = os.path.join(root, file)
            all_file_paths.append(file_path)

    total_files = len(all_file_paths)
    print(f"Total files collected: {total_files}")

    try:
        for file_path in tqdm(all_file_paths, total=total_files, desc="Processing files", unit="file", smoothing=0.05):
            try:
                size = os.path.getsize(file_path)
                if size > 0:
                    all_file_sizes.append(size)
                    if is_resident(file_path):
                        resident_file_sizes.append(size)
                    else:
                        nonresident_file_sizes.append(size)
                else:
                    zero_byte_count += 1
            except Exception:
                continue
    except KeyboardInterrupt:
        print("\nProcess interrupted by user (Ctrl+C). Computing partial statistics...")

    res_count, res_min, res_max, res_median, res_mean, res_stdev = compute_stats(resident_file_sizes)
    nonres_count, nonres_min, nonres_max, nonres_median, nonres_mean, nonres_stdev = compute_stats(nonresident_file_sizes)
    all_count, all_min, all_max, all_median, all_mean, all_stdev = compute_stats(all_file_sizes)

    print("\nResident Data Statistics (excluding zero-byte files):")
    print("  Count: ", res_count)
    if res_mean is not None:
        print("  Min file size (bytes): ", res_min)
        print("  Max file size (bytes): ", res_max)
        print("  Median file size (bytes): ", res_median)
        print("  Mean file size (bytes): ", res_mean)
        print("  Standard Deviation (bytes): ", res_stdev)
    else:
        print("  No resident files found.")

    print("\nNon-Resident Data Statistics (excluding zero-byte files):")
    print("  Count: ", nonres_count)
    if nonres_mean is not None:
        print("  Min file size (bytes): ", nonres_min)
        print("  Max file size (bytes): ", nonres_max)
        print("  Median file size (bytes): ", nonres_median)
        print("  Mean file size (bytes): ", nonres_mean)
        print("  Standard Deviation (bytes): ", nonres_stdev)
    else:
        print("  No non-resident files found.")

    print("\nAll Files Statistics (excluding zero-byte files):")
    print("  Count: ", all_count)
    if all_mean is not None:
        print("  Min file size (bytes): ", all_min)
        print("  Max file size (bytes): ", all_max)
        print("  Median file size (bytes): ", all_median)
        print("  Mean file size (bytes): ", all_mean)
        print("  Standard Deviation (bytes): ", all_stdev)
    else:
        print("  No files found.")

    print("\nZero-byte File Count:", zero_byte_count)

    input("\nProcessing complete. Press Enter to exit...")

if __name__ == "__main__":
    args = parse_args()
    SHOW_FSUTIL_OUTPUT = args.show_fsutil_output
    if not is_admin():
        print("Administrator privileges are required. Requesting elevation...")
        request_admin()
        sys.exit(0)
    main()

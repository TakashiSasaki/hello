
# Resident Data Statistics for NTFS Files

This repository provides a Python script that recursively scans a directory tree and computes file size statistics based on where a file's actual data is stored on an NTFS volume. It distinguishes between files whose data is stored as **resident** (within the MFT record) and **non-resident** (stored in external clusters). Zero-byte files are excluded from the statistical calculations (with their count tracked separately).

## Features

- **Resident vs Non-Resident Detection:**  
  The script uses the `fsutil file layout` command to determine if a file's data is stored resident (within the MFT) or non-resident (outside the MFT). It parses the output (using the short 8.3 file path) to make this distinction by analyzing the `$DATA` stream block.

- **Statistics Calculation:**  
  It computes the following statistics (excluding zero-byte files) for:
  - Resident files
  - Non-resident files
  - All files
  The statistics include count, minimum file size, maximum file size, median, mean, and standard deviation.

- **Progress Display:**  
  The script uses the `tqdm` library to provide a progress bar during both file collection and processing.

- **Debug Output Option:**  
  An optional command-line flag (`--show-fsutil-output`) displays the fsutil command output and the executed command line for debugging purposes.

- **Code Page Handling:**  
  To ensure that `fsutil` outputs are decoded correctly, the parent process's console code page is set to `cp437` and the subprocess output is decoded accordingly.

## Requirements

- **Operating System:** Windows (NTFS file system)
- **Python Version:** Python 3.6 or higher
- **Dependencies:**  
  - `tqdm` (Install via `pip install tqdm`)

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/resident-data-stats.git
   cd resident-data-stats
   ```

2. **Install dependencies:**

   ```bash
   pip install tqdm
   ```

3. **Run the script:**

   Simply run the script from the command line. By default, it processes the current directory:

   ```bash
   python resident-data-stats.py
   ```

   To display the fsutil output for each file (useful for debugging):

   ```bash
   python resident-data-stats.py --show-fsutil-output
   ```

   The script will request administrator privileges if it is not already running in an elevated command prompt.

## How It Works

- **File Collection:**  
  The script uses `os.walk()` to recursively gather all file paths from the current directory. A progress bar shows the file collection progress.

- **File Processing:**  
  For each file, it checks the file size. Zero-byte files are skipped from further processing and counted separately. For files with size greater than zero, the script:
  - Converts the file path to its absolute path.
  - Converts the absolute path to its short (8.3) form.
  - Executes the `fsutil file layout` command using the short path.
  - Parses the output from the `$DATA` stream block to determine whether the file data is resident or non-resident. This is done by checking for keywords like "no clusters allocated" (resident) or "has parsed information" (non-resident) and by comparing size values.
  
- **Statistics Calculation:**  
  After processing, the script computes count, min, max, median, mean, and standard deviation for resident files, non-resident files, and for all files (excluding zero-byte files).

## Sample Output

Below is an example of the output (statistics summary):

```
Total files collected: 47827

Resident Data Statistics (excluding zero-byte files):
  Count:  120
  Min file size (bytes):  5615
  Max file size (bytes):  6273
  Median file size (bytes):  5944.0
  Mean file size (bytes):  5944
  Standard Deviation (bytes):  465.28

Non-Resident Data Statistics (excluding zero-byte files):
  Count:  468
  Min file size (bytes):  10
  Max file size (bytes):  6218
  Median file size (bytes):  398.0
  Mean file size (bytes):  1190.12
  Standard Deviation (bytes):  1714.07

All Files Statistics (excluding zero-byte files):
  Count:  588
  Min file size (bytes):  10
  Max file size (bytes):  6273
  Median file size (bytes):  420.0
  Mean file size (bytes):  1325.94
  Standard Deviation (bytes):  1868.79

Zero-byte File Count: 50
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/your-username/resident-data-stats/issues).

## Disclaimer

This script is provided "as is" without any warranty. Use it at your own risk. The tool relies on `fsutil`, which may have limitations in certain environments. Please test thoroughly in your environment before using it in production.

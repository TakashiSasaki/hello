
# EFU File List Specification for Everything

## 1. Introduction

- **Everything Overview:**  
  Everything is a high‑speed file search utility for Windows that indexes all file and folder names to provide near‑instantaneous search results. One of its key features is the ability to generate a static file list (the EFU file) as a snapshot of file metadata.

- **Purpose of EFU Files:**  
  The EFU (Everything File List) file serves as an offline catalog of files. It is particularly useful for indexing files on media that are not constantly connected (such as CD/DVDs or removable storage) or for maintaining a snapshot of files that do not change frequently.

## 2. EFU File Format Overview

- **File Type & Encoding:**  
  - The EFU file is a CSV (Comma-Separated Values) file.
  - It is encoded in UTF-8 to support a wide range of characters, including Unicode.

- **Header Requirements:**  
  - A header row is mandatory.
  - The header must include at least the required column **"Filename"**.
  - Optional columns include **"Size"**, **"Date Modified"**, **"Date Created"**, and **"Attributes"**.

## 3. Detailed Field Specifications

### 3.1 Filename Column
- **Purpose:**  
  - Contains the file path for each file or directory in the list.
- **Path Types:**  
  - Supports both absolute and relative paths.
  - Relative paths are interpreted based on the EFU file’s location.
- **Special Conventions:**  
  - The use of “.” (current directory) and “..” (parent directory) is supported.
  - A leading backslash (“\”) indicates that the path is relative to the list’s root.
  - Special characters (such as commas or quotes) are handled according to standard CSV conventions (i.e., fields containing such characters are enclosed in quotes).

### 3.2 Size Column
- **Purpose:**  
  - Represents the size of the file in bytes.
- **Data Type:**  
  - Expected to be an integer value.

### 3.3 Date Columns (Date Modified and Date Created)
- **Purpose:**  
  - Capture the timestamp for the last modification or creation of the file.
- **Formats:**  
  - Typically stored in FILETIME format—a 64‑bit integer representing the number of 100‑nanosecond intervals elapsed since January 1, 1601 (UTC).
  - Alternatively, an ISO 8601 format (e.g., YYYY‑MM‑DDTHH:MM:SSZ) may be used for improved human readability.
- **Conversion Considerations:**  
  - When used on non‑Windows systems (like Linux), conversion from FILETIME to Unix epoch (seconds since January 1, 1970) may be necessary.

### 3.4 Attributes Column
- **Purpose:**  
  - Stores Windows file attributes as a bitmask.
- **Representation:**  
  - The attributes are represented as an integer value, which can be expressed in either decimal or hexadecimal (with a “0x” prefix).
- **Common Attribute Flags Include:**  
  - **FILE_ATTRIBUTE_READONLY:** 1 (0x1) – File is read‑only.
  - **FILE_ATTRIBUTE_HIDDEN:** 2 (0x2) – File or directory is hidden.
  - **FILE_ATTRIBUTE_SYSTEM:** 4 (0x4) – File is used by the operating system.
  - **FILE_ATTRIBUTE_DIRECTORY:** 16 (0x10) – Entry is a directory.
  - **FILE_ATTRIBUTE_ARCHIVE:** 32 (0x20) – File is marked for backup.
  - **FILE_ATTRIBUTE_TEMPORARY:** 256 (0x100) – File is temporary.
  - **FILE_ATTRIBUTE_COMPRESSED:** 2048 (0x800) – File is compressed.
  - **FILE_ATTRIBUTE_ENCRYPTED:** 16384 (0x4000) – File is encrypted.
- **Combination of Attributes:**  
  - Multiple attributes can be combined by summing the individual flag values (bitwise OR).

## 4. Creation and Usage of EFU Files

### 4.1 Creation Methods
- **Graphical User Interface:**  
  - Users can manually create EFU files by dragging and dropping files into the “File List Editor” provided within Everything.
  - The export function in Everything allows saving search results directly as an EFU file.
  
- **Command-Line Interface:**  
  - EFU files can be generated via command-line using a command such as:  
    `Everything.exe -create-file-list "output.efu" "C:\path\to\scan"`.
  - Additional command‑line options enable filtering (e.g., excluding specific file patterns).

### 4.2 Import and Integration
- **Importing EFU Files:**  
  - EFU files can be imported back into Everything, allowing the static file list to be integrated with the live search index.
  - Changes to the EFU file can be monitored and automatically reloaded by Everything if configured.

## 5. Considerations for Cross‑Platform (Linux) Compatibility

- **CSV and UTF‑8:**  
  - Using CSV and UTF‑8 ensures basic interoperability on Linux and other platforms.
  
- **Timestamp Conversion:**  
  - The FILETIME format must be converted to a Unix‑compatible timestamp (e.g., Unix epoch time) for Linux systems.
  
- **Path Conventions:**  
  - Windows uses backslashes and drive letters, while Linux uses forward slashes and a unified root directory.
  - Tools on Linux must implement robust path conversion logic to handle absolute versus relative paths.
  
- **File Attributes:**  
  - Windows file attributes have no direct counterpart in Linux.
  - Developers may consider mapping key attributes (such as read‑only or hidden) to Linux file permissions or storing the original values as extended attributes.

## 6. Conclusion and Recommendations

- **Key Takeaways:**  
  - The EFU file list is a simple, UTF‑8 encoded CSV format designed primarily for indexing file names and basic metadata.
  - The essential “Filename” column must always be present, while additional metadata (size, dates, attributes) enhances the file list’s utility.
  - Timestamps (FILETIME or ISO 8601) and file attributes (bitmask values) are central to the EFU specification.
  
- **Implementation Advice:**  
  - Ensure that any tool processing EFU files can reliably parse the header and required columns.
  - For cross‑platform use, implement proper conversion of Windows‑specific formats (FILETIME, path styles, attributes) into equivalent Linux representations.
  - Maintain flexibility by supporting optional columns while prioritizing accurate handling of the “Filename” field.

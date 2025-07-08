# MFT Resident Data Size Limit

This document provides an analysis of the maximum size of resident data that can be stored within an NTFS MFT record, based on the results from running `resident-data-stats.py` on a dataset of approximately 50,000 files.

## Background

NTFS (New Technology File System) uses a Master File Table (MFT) to store metadata about files. For small files, the file data may be stored directly within the MFT record itself (resident data). If the file is larger than the available space in the MFT record, the data is stored in separate clusters (non-resident).

## Analysis of Resident Data

After executing `resident-data-stats.py` on a desktop folder containing roughly 50,000 files, the following key observation was made for resident data:

- **Resident Data Statistics (excluding zero-byte files):**
  - **Count:** 10,771 files
  - **Max file size:** 732 bytes

Given that the maximum file size among resident files is 732 bytes, it suggests that the MFT record can accommodate resident data up to around this size. However, due to potential variations in metadata (file name, timestamps, security descriptors, etc.), the practical limit for storing file data resident in the MFT record might be slightly lower.

## Conclusion

Based on the analysis, it appears that:
- The maximum size for resident data in the MFT record is approximately **732 bytes**.
- Allowing for additional metadata overhead, a safe threshold for resident data storage is around **700 bytes**.

This finding is significant for applications and system administrators who need to optimize storage and understand NTFS file system behavior.

## Future Considerations

- Further testing on different volumes and configurations may provide more insights.
- Variations in MFT record layout (depending on the NTFS version and formatting options) could affect this limit.
- This analysis can help in planning file system performance and storage optimizations.


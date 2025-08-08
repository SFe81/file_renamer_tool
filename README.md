# File Renamer Tool

A Python script that renames files by adding their creation date and time as a prefix in the format `yymmdd_hhmmss_original_name`.

## Overview

This tool is designed to help organize files by prefixing them with their creation timestamp. This is particularly useful for:
- Archiving files with temporal context
- Organizing large collections of files chronologically
- Maintaining file creation history during file system operations

## Features

- ✅ Adds creation date/time prefix in format: `yymmdd_hhmmss_original_name`
- ✅ Supports both moving and copying files
- ✅ Handles filename conflicts automatically (adds incremental counter)
- ✅ Processes entire directories or individual files
- ✅ Filter by file extensions
- ✅ Comprehensive logging
- ✅ Cross-platform compatibility (macOS, Windows, Linux)
- ✅ Command-line interface with flexible options

## Directory Structure

```
8_Renaming/
├── file_renamer.py         # Main Python script
├── input_files/            # Place files here to be processed
├── output_files/           # Renamed files will be placed here
├── README.md              # This documentation
└── file_renamer.log       # Log file (created after first run)
```

## Installation & Requirements

### Prerequisites
- Python 3.6 or higher
- No additional packages required (uses only standard library)

### Setup
1. Clone or download this project
2. Ensure Python 3.6+ is installed on your system
3. Make the script executable (optional):
   ```bash
   chmod +x file_renamer.py
   ```

## Usage

### Basic Usage

1. **Place files to be renamed** in the `input_files/` directory
2. **Run the script**:
   ```bash
   python file_renamer.py
   ```
3. **Check results** in the `output_files/` directory

### Command Line Options

```bash
python file_renamer.py [options]
```

#### Available Options:

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--input` | `-i` | Input directory containing files to rename | `./input_files` |
| `--output` | `-o` | Output directory for renamed files | `./output_files` |
| `--copy` | `-c` | Copy files instead of moving them | `False` (moves files) |
| `--extensions` | `-e` | File extensions to process | All files |
| `--file` | `-f` | Process a single file instead of directory | None |
| `--help` | `-h` | Show help message | - |

### Examples

#### Example 1: Basic directory processing
```bash
python file_renamer.py
```
- Processes all files in `./input_files/`
- Moves renamed files to `./output_files/`

#### Example 2: Copy files instead of moving
```bash
python file_renamer.py --copy
```
- Same as above but copies files (originals remain in input folder)

#### Example 3: Custom directories
```bash
python file_renamer.py -i /path/to/source -o /path/to/destination
```

#### Example 4: Process only specific file types
```bash
python file_renamer.py -e .jpg .png .gif
```
- Only processes image files with specified extensions

#### Example 5: Process a single file
```bash
python file_renamer.py -f /path/to/single/file.txt -o ./renamed_files/
```

#### Example 6: Advanced usage
```bash
python file_renamer.py -i ./documents -o ./archived_docs -c -e .pdf .docx .txt
```
- Copy PDF, DOCX, and TXT files from `./documents` to `./archived_docs`

## Output Format

### Filename Format
Original filename: `document.pdf`
Creation date: `March 15, 2025, 14:30:45`
New filename: `250315_143045_document.pdf`

### Format Breakdown
- `25` - Year (2025)
- `03` - Month (March)
- `15` - Day
- `14` - Hour (24-hour format)
- `30` - Minute
- `45` - Second
- `_` - Separator
- `document.pdf` - Original filename

### Conflict Resolution
If a file with the same name already exists, the script automatically adds a counter:
- `250315_143045_document.pdf`
- `250315_143045_document_001.pdf`
- `250315_143045_document_002.pdf`

## Logging

The script creates a log file (`file_renamer.log`) that contains:
- Timestamp of operations
- Files processed successfully
- Error messages for failed operations
- Summary statistics

### Log Example
```
2025-08-08 10:30:15 - INFO - Starting file renaming process...
2025-08-08 10:30:15 - INFO - Found 5 files to process
2025-08-08 10:30:15 - INFO - Moved: photo.jpg -> 250808_103015_photo.jpg
2025-08-08 10:30:15 - INFO - Moved: document.pdf -> 250808_103015_document.pdf
2025-08-08 10:30:15 - INFO - Processing complete: 5 successful, 0 errors
```

## Error Handling

The script handles various error scenarios:
- **File not found**: Logs error and continues with other files
- **Permission errors**: Reports access issues
- **Disk space**: Handles insufficient storage space
- **Invalid paths**: Validates directory existence
- **Naming conflicts**: Automatically resolves with counters

## Platform Compatibility

### macOS
- Uses `st_birthtime` for accurate file creation time
- Fully supported

### Windows  
- Uses `st_ctime` for file creation time
- Fully supported

### Linux
- Uses `st_ctime` (may represent last metadata change)
- Supported with limitation on creation time accuracy

## Best Practices

1. **Backup Important Files**: Always backup important files before processing
2. **Test with Copies**: Use `--copy` flag for initial testing
3. **Check Logs**: Review `file_renamer.log` for any issues
4. **Organize by Type**: Use `--extensions` to process specific file types
5. **Custom Directories**: Use absolute paths for better reliability

## Troubleshooting

### Common Issues

#### "Permission Denied" Error
```bash
# Make sure you have read/write permissions
chmod 644 input_files/*
chmod 755 input_files/ output_files/
```

#### "No Files Found" Message
- Check that files exist in the input directory
- Verify file extensions if using `--extensions` filter
- Ensure the input path is correct

#### Script Won't Run
```bash
# Check Python version
python --version

# Ensure script has execute permissions
chmod +x file_renamer.py

# Try running with python3 explicitly
python3 file_renamer.py
```

### Getting Help

Run the script with the help flag to see all available options:
```bash
python file_renamer.py --help
```

## License

This project is created for Freedom2035 DataPipelines. Please refer to your organization's licensing terms.

## Contributing

To contribute improvements:
1. Test changes thoroughly
2. Update documentation as needed
3. Follow existing code style
4. Add appropriate logging for new features

## Changelog

### Version 1.0 (August 8, 2025)
- Initial release
- Basic file renaming with creation date prefix
- Command-line interface
- Comprehensive logging
- Cross-platform support
- Conflict resolution
- Single file and batch processing

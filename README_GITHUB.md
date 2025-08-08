# File Renamer Tool

A Python utility for organizing files by adding creation date prefixes in the format `yymmdd_hhmmss_original_name`.

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Quick Start

1. Place files in `input_files/` directory
2. Run: `python3 file_renamer.py`
3. Find renamed files in `output_files/` directory

## Features

- ✅ Date prefix format: `yymmdd_hhmmss_original_name`
- ✅ Copy or move files
- ✅ Filter by file extensions
- ✅ Batch processing
- ✅ Comprehensive logging
- ✅ Cross-platform support

## Installation

```bash
git clone https://github.com/SFe81/file_renamer_tool.git
cd file_renamer_tool
python3 file_renamer.py --help
```

## Documentation

See [README.md](README.md) for detailed documentation and usage examples.

## Example

```bash
# Basic usage
python3 file_renamer.py

# Copy files instead of moving
python3 file_renamer.py --copy

# Process only PDFs and images
python3 file_renamer.py --extensions .pdf .jpg .png
```

## Project Structure

```
file-renamer-tool/
├── file_renamer.py      # Main script
├── examples.py          # Usage examples
├── input_files/         # Place files here
├── output_files/        # Renamed files appear here
└── README.md           # Full documentation
```

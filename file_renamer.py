#!/usr/bin/env python3
"""
File Renamer Script

This script renames files by adding their creation date and time as a prefix
in the format: yymmdd_hhmmss_original_name

Author: Generated for Freedom2035 DataPipelines
Date: August 8, 2025
"""

import os
import shutil
import argparse
from datetime import datetime
from pathlib import Path
import logging


def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('file_renamer.log'),
            logging.StreamHandler()
        ]
    )


def get_file_creation_time(file_path):
    """
    Get the creation time of a file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        datetime: Creation time of the file
    """
    try:
        # Get file stats
        stat = os.stat(file_path)
        
        # On macOS, use st_birthtime for creation time
        # On other systems, fall back to st_ctime
        if hasattr(stat, 'st_birthtime'):
            creation_time = stat.st_birthtime
        else:
            creation_time = stat.st_ctime
            
        return datetime.fromtimestamp(creation_time)
    except Exception as e:
        logging.error(f"Error getting creation time for {file_path}: {e}")
        return None


def format_datetime_prefix(dt):
    """
    Format datetime to the required prefix format: yymmdd_hhmmss_
    
    Args:
        dt (datetime): Datetime object
        
    Returns:
        str: Formatted prefix string
    """
    return dt.strftime("%y%m%d_%H%M%S_")


def rename_file(source_path, destination_dir, copy_mode=False):
    """
    Rename a file by adding creation date prefix.
    
    Args:
        source_path (str): Path to the source file
        destination_dir (str): Directory where renamed file will be placed
        copy_mode (bool): If True, copy file instead of moving
        
    Returns:
        tuple: (success, new_filename, error_message)
    """
    try:
        source_path = Path(source_path)
        destination_dir = Path(destination_dir)
        
        # Ensure destination directory exists
        destination_dir.mkdir(parents=True, exist_ok=True)
        
        # Get creation time
        creation_time = get_file_creation_time(source_path)
        if creation_time is None:
            return False, None, "Could not retrieve file creation time"
        
        # Generate new filename
        date_prefix = format_datetime_prefix(creation_time)
        original_name = source_path.name
        new_filename = f"{date_prefix}{original_name}"
        
        # Create destination path
        destination_path = destination_dir / new_filename
        
        # Handle filename conflicts
        counter = 1
        while destination_path.exists():
            name_parts = original_name.rsplit('.', 1)
            if len(name_parts) == 2:
                base_name, extension = name_parts
                new_filename = f"{date_prefix}{base_name}_{counter:03d}.{extension}"
            else:
                new_filename = f"{date_prefix}{original_name}_{counter:03d}"
            destination_path = destination_dir / new_filename
            counter += 1
        
        # Move or copy the file
        if copy_mode:
            shutil.copy2(source_path, destination_path)
            logging.info(f"Copied: {source_path.name} -> {new_filename}")
        else:
            shutil.move(str(source_path), str(destination_path))
            logging.info(f"Moved: {source_path.name} -> {new_filename}")
        
        return True, new_filename, None
        
    except Exception as e:
        error_msg = f"Error processing {source_path}: {e}"
        logging.error(error_msg)
        return False, None, error_msg


def process_directory(input_dir, output_dir, copy_mode=False, file_extensions=None):
    """
    Process all files in the input directory.
    
    Args:
        input_dir (str): Directory containing files to rename
        output_dir (str): Directory where renamed files will be placed
        copy_mode (bool): If True, copy files instead of moving
        file_extensions (list): List of file extensions to process (e.g., ['.txt', '.pdf'])
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    if not input_path.exists():
        logging.error(f"Input directory does not exist: {input_dir}")
        return
    
    # Get all files in input directory
    files = [f for f in input_path.iterdir() if f.is_file()]
    
    # Filter by extensions if provided
    if file_extensions:
        file_extensions = [ext.lower() for ext in file_extensions]
        files = [f for f in files if f.suffix.lower() in file_extensions]
    
    if not files:
        logging.warning("No files found to process")
        return
    
    logging.info(f"Found {len(files)} files to process")
    
    success_count = 0
    error_count = 0
    
    for file_path in files:
        success, new_name, error = rename_file(file_path, output_path, copy_mode)
        if success:
            success_count += 1
        else:
            error_count += 1
            logging.error(f"Failed to process {file_path.name}: {error}")
    
    logging.info(f"Processing complete: {success_count} successful, {error_count} errors")


def main():
    """Main function to handle command line arguments and execute the script."""
    parser = argparse.ArgumentParser(
        description="Rename files by adding creation date prefix (yymmdd_hhmmss_original_name)"
    )
    
    parser.add_argument(
        "-i", "--input", 
        default="./input_files",
        help="Input directory containing files to rename (default: ./input_files)"
    )
    
    parser.add_argument(
        "-o", "--output", 
        default="./output_files",
        help="Output directory for renamed files (default: ./output_files)"
    )
    
    parser.add_argument(
        "-c", "--copy", 
        action="store_true",
        help="Copy files instead of moving them"
    )
    
    parser.add_argument(
        "-e", "--extensions", 
        nargs="+",
        help="File extensions to process (e.g., .txt .pdf .jpg)"
    )
    
    parser.add_argument(
        "-f", "--file", 
        help="Process a single file instead of a directory"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging()
    
    logging.info("Starting file renaming process...")
    
    if args.file:
        # Process single file
        if not os.path.exists(args.file):
            logging.error(f"File does not exist: {args.file}")
            return
        
        success, new_name, error = rename_file(args.file, args.output, args.copy)
        if success:
            logging.info(f"Successfully processed file: {new_name}")
        else:
            logging.error(f"Failed to process file: {error}")
    else:
        # Process directory
        process_directory(args.input, args.output, args.copy, args.extensions)
    
    logging.info("File renaming process completed")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Example usage of the file_renamer.py script

This script demonstrates different ways to use the file renaming tool.
"""

import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and print the description."""
    print(f"\n{'='*60}")
    print(f"EXAMPLE: {description}")
    print(f"COMMAND: {command}")
    print('='*60)
    
    # Ask user if they want to run this example
    response = input("Run this example? (y/n): ").lower().strip()
    if response == 'y':
        try:
            result = subprocess.run(command.split(), capture_output=True, text=True)
            print("STDOUT:")
            print(result.stdout)
            if result.stderr:
                print("STDERR:")
                print(result.stderr)
            print(f"Return code: {result.returncode}")
        except Exception as e:
            print(f"Error running command: {e}")
    else:
        print("Skipped.")

def main():
    """Main function with usage examples."""
    print("File Renamer - Usage Examples")
    print("=" * 40)
    
    # Check if the main script exists
    script_path = Path("file_renamer.py")
    if not script_path.exists():
        print("Error: file_renamer.py not found in current directory")
        sys.exit(1)
    
    # Example 1: Basic usage
    run_command(
        "python3 file_renamer.py --help",
        "Show help and available options"
    )
    
    # Example 2: Basic file processing
    run_command(
        "python3 file_renamer.py",
        "Process all files in input_files/ and move to output_files/"
    )
    
    # Example 3: Copy mode
    run_command(
        "python3 file_renamer.py --copy",
        "Copy files instead of moving them"
    )
    
    # Example 4: Specific file types
    run_command(
        "python3 file_renamer.py --extensions .txt .pdf",
        "Process only .txt and .pdf files"
    )
    
    # Example 5: Custom directories
    run_command(
        "python3 file_renamer.py -i ./input_files -o ./archived_files",
        "Use custom input and output directories"
    )
    
    print(f"\n{'='*60}")
    print("Examples completed!")
    print("Check the output_files/ directory for results.")
    print("Check file_renamer.log for detailed logging.")

if __name__ == "__main__":
    main()

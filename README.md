# Automatic File Organizer

This Python script monitors a specified directory and automatically organizes files into different subdirectories based on their file extensions. It utilizes the `watchdog` library to watch for file system events and a custom event handler to move files to their respective destination directories.

## Requirements

- Python 3.x
- Watchdog library (install using `pip install watchdog`)

## Usage

1. Clone or download this repository.

2. Modify the script to specify your source directory (`source_dir`) and destination directories for different file types (`dst_audio`, `dst_img`, `dst_vid`, `dst_pkg`, `dst_csv`, `dst_dmg`, `dst_doc`).

3. Run the script:

```bash
python automatic_file_organizer.py


# File Organizer

## Overview
This Python script monitors a specified directory for file modifications and automatically organizes the files into different folders based on their file extensions.

## Functionality
The script performs the following actions:
- Monitors a defined directory for file modifications.
- Automatically sorts files into specific folders based on their file extensions.
- Supported file categories include audio, images, video, packages, CSV, DMG, and documents.

## Requirements
- Python 3.x
- External library: `watchdog` (to install: `pip install watchdog`)

## Setup
1. Clone or download the script to your local machine.
2. Install the required dependencies (`watchdog` library) using `pip`.
3. Define the directories:
   - `source_dir`: The directory to be monitored for file changes.
   - `destinations`: Folders where files will be sorted based on their extensions.

## Usage
1. Customize the `source_dir` and `destinations` to match your preferred directory paths and categories.
2. Run the script by executing `python file_organizer.py` in your terminal.
3. The script will continuously monitor the specified directory for file modifications.
4. When a file is modified, it will be automatically sorted into the appropriate category folder.

## Customization
- Extend or modify the `destinations` dictionary to include additional file categories and their respective destination folders.
- Add or modify file extensions and their corresponding categories in the `on_modified()` method within the `FileEventHandler` class.

## Notes
- The script handles common file types, but you can customize and expand it to include other file extensions and categories.
- Use this script responsibly and ensure it’s monitoring the correct directory to prevent accidental data loss.

## Credits
This script utilizes the `watchdog` library for file system monitoring.

---

Certainly! This Python script is designed to monitor a specified directory for file modifications and automatically organize these files into different folders based on their file extensions. Let's break down the script step by step:

### Imported Libraries
- **os, sys, time, logging, shutil:** Python built-in modules for interacting with the operating system, handling file operations, managing time, logging events, and file/directory manipulation.
- **watchdog:** An external library used for monitoring file system events.

### Initial Setup
- **source_dir:** Path of the directory to be monitored (in this case, "/Users/tanishjain/Downloads").
- **destinations:** Dictionary containing different categories as keys and their respective destination paths as values. Files will be sorted into these categories based on their file extensions.

### Function `create_directories()`
This function checks if the destination directories exist and creates them if they don't.

### Class `FileEventHandler`
This class inherits from `FileSystemEventHandler` provided by the `watchdog` library. It's used to handle file system events. The `on_modified()` method is overridden to sort and move files based on their extensions to the respective categories defined in the `destinations` dictionary.

### Main Script
- **Logging Configuration:** Configures the logging settings to display time and messages.
- **Parsing Command Line Arguments:** Determines the directory to monitor. If no directory is provided via command line arguments, it defaults to the source directory.
- **Initializing the Event Handler and Observer:** Creates an instance of the `FileEventHandler` and `Observer` from the `watchdog` library. It attaches the event handler to the observer and specifies the source directory to monitor.

### Observer Execution
- **Observer Start:** Initiates the monitoring process.
- **While Loop:** Keeps the main thread running while the observer is active.
- **Handling Keyboard Interrupt (Ctrl+C):** Gracefully stops the observer when the user terminates the script using Ctrl+C.

### Observer Termination
- **Observer Stop:** Stops the observer.
- **Observer Join:** Ensures that the observer completes its tasks before the script terminates.

### How the File Sorting Works
- The `on_modified()` method triggers each time a file in the monitored directory is modified.
- For each file in the directory, it extracts the file extension.
- It then checks the extension against predefined categories and moves the file to the appropriate destination folder if a match is found.

### Conclusion
This script utilizes the `watchdog` library to monitor a directory for file modifications and automatically organizes these files into different folders based on their file extensions, providing an automated file organization system.

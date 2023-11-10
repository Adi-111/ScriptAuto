import os
import sys
import time
import logging
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Define the directory to monitor
source_dir = "/Users/tanishjain/Downloads"
destinations = {
    "audio": "/Users/tanishjain/Desktop/Adi/Audio",
    "images": "/Users/tanishjain/Desktop/Adi/Images",
    "video": "/Users/tanishjain/Desktop/Adi/Video",
    "packages": "/Users/tanishjain/Desktop/Adi/Packages",
    "csv": "/Users/tanishjain/Desktop/Adi/CSV",
    "dmg": "/Users/tanishjain/Desktop/Adi/DMG",
    "doc": "/Users/tanishjain/Desktop/Adi/DOC",
}

# Function to create directories if they don't exist


def create_directories():
    for path in destinations.values():
        if not os.path.exists(path):
            os.makedirs(path)


# Define a custom event handler that will respond to file system events

class FileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        create_directories()  # Ensure directories are created
        for entry in os.scandir(source_dir):
            if entry.is_file():
                name = entry.name
                extension = name.split(".")[-1].lower()

                for category, destination in destinations.items():
                    if extension in {"wav", "mp3"} and category == "audio":
                        shutil.move(entry.path, destination)
                    elif extension in {"jpg", "jpeg", "png"} and category == "images":
                        shutil.move(entry.path, destination)
                    elif extension in {"mov", "mp4"} and category == "video":
                        shutil.move(entry.path, destination)
                    elif extension == "csv" and category == "csv":
                        shutil.move(entry.path, destination)
                    elif extension == "pkg" and category == "packages":
                        shutil.move(entry.path, destination)
                    elif extension == "dmg" and category == "dmg":
                        shutil.move(entry.path, destination)
                    elif extension in {"pdf", "doc", "docx", "eps"} and category == "doc":
                        shutil.move(entry.path, destination)


# Create an observer and attach the event handler
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
path = sys.argv[1] if len(sys.argv) > 1 else '.'
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, path=source_dir, recursive=False)

# Start the observer
observer.start()

try:
    while True:
        # The observer runs in the background, so you need to keep the main thread running
        time.sleep(1)
except KeyboardInterrupt:
    # Gracefully stop the observer when you press Ctrl+C
    observer.stop()


# Wait for the observer to complete
observer.join()


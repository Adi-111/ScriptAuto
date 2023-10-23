import os
import sys
import time
import logging
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Define the directory to monitor
source_dir = "/Users/tanishjain/Downloads"
dst_audio = "/Users/tanishjain/Desktop/Adi/Audio"
dst_img = "/Users/tanishjain/Desktop/Adi/Images"
dst_vid = "/Users/tanishjain/Desktop/Adi/Video"
dst_pkg = "/Users/tanishjain/Desktop/Adi/Packages"
dst_csv = "/Users/tanishjain/Desktop/Adi/CSV"
dst_dmg = "/Users/tanishjain/Desktop/Adi/DMG"
dst_doc = "/Users/tanishjain/Desktop/Adi/DOC"
dst_code = "/Users/tanishjain/Desktop/Adi/Code"


# Define a custom event handler that will respond to file system events
class FileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('wav') or name.endswith('mp3'):
                    shutil.move(source_dir, dst_audio)
                elif name.endswith('jpg') or name.endswith('jpeg') or name.endswith('png'):
                    shutil.move(source_dir, dst_img)
                elif name.endswith('mov') or name.endswith('mp4'):
                    shutil.move(source_dir, dst_vid)
                elif name.endswith('csv'):
                    shutil.move(source_dir, dst_csv)
                elif name.endswith('pkg'):
                    shutil.move(source_dir, dst_pkg)
                elif name.endswith('dmg'):
                    shutil.move(source_dir, dst_dmg)
                elif name.endswith('pdf') or name.endswith('DOC') or name.endswith('DOCX') or name.endswith('EPS'):
                    shutil.move(source_dir, dst_doc)


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

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os.path import exists, join, splitext
from shutil import move
from extensions import *

import logging

# paths
source_dir = os.path.join(os.path.expanduser("~"), "Downloads" + "/")
dest_dir_music = os.path.join(source_dir, "Music")
dest_dir_images = os.path.join(source_dir, "Images")
dest_dir_videos = os.path.join(source_dir, "Videos")
dest_dir_docs = os.path.join(source_dir, "Documents")


def create_dir(dest):
    """Check if the folder does not exists

    Args:
        dest (str): folder path
    """
    if not os.path.exists(dest):
        # Create the folder
        os.makedirs(dest)


def make_unique(dest, name):
    """In case there is a file with the same name, add a number to the end of the file name.

    Args:
        dest (str): file path
        name (str): file name

    Returns:
        str: file name modified
    """
    filename, extension = splitext(name)
    counter = 1
    # If file exists, adds number to the end of the filename
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    """Move the file

    Args:
        dest (str): file path
        entry (str): new path
        name (str): file name
    """
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        os.rename(oldName, newName)
    # Check if the folder does not exists
    create_dir(dest)
    # Move the file
    move(entry, dest)


def on_cleaner():
    """Main function.
    Iterate between the existing files in the path and execute each of the functions.
    """
    with os.scandir(source_dir) as entries:
        for entry in entries:
            name = entry.name
            check_audio_files(entry, name)
            check_video_files(entry, name)
            check_image_files(entry, name)
            check_document_files(entry, name)


def check_audio_files(entry, name):
    """Check if any audio file exist and moves it to its respective folder.

    Args:
        entry (str): new path
        name (str): file name
    """
    for audio_extension in audio_extensions:
        if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
            move_file(dest_dir_music, entry, name)
            logging.info(f"Moved audio file: {name}")


def check_video_files(entry, name):
    """Check if any video file exist and moves it to its respective folder.

    Args:
        entry (str): new path
        name (str): file name
    """
    for video_extension in video_extensions:
        if name.endswith(video_extension) or name.endswith(video_extension.upper()):
            move_file(dest_dir_videos, entry, name)
            logging.info(f"Moved video file: {name}")


def check_image_files(entry, name):
    """Check if any image file exist.

    Args:
        entry (str): new path
        name (str): file name
    """
    for image_extension in image_extensions:
        if name.endswith(image_extension) or name.endswith(image_extension.upper()):
            move_file(dest_dir_images, entry, name)
            logging.info(f"Moved image file: {name}")


def check_document_files(entry, name):
    """Check if any document file exist.

    Args:
        entry (str): new path
        name (str): file name
    """
    for document_extension in document_extensions:
        if name.endswith(document_extension) or name.endswith(
            document_extension.upper()
        ):
            move_file(dest_dir_docs, entry, name)
            logging.info(f"Moved document file: {name}")


# Check if the downloads folder has been modified.
class DownloadHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            on_cleaner()


# Check if run by the user in terminal
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    path = source_dir
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

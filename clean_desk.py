from pathlib import Path
from time import sleep

from watchdog.observers import Observer

from EventHandler import EventHandler

if __name__ == '__main__':
    watch_path = Path.home() / 'OneDrive/Desktop'
    destination_root = Path.home() / 'OneDrive/Desktop/holder of things'
    event_handler = EventHandler(watch_path=watch_path, destination_root=destination_root)

    observer = Observer()
    observer.schedule(event_handler, f'{watch_path}', recursive=True)
    print("Start watching...")
    observer.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
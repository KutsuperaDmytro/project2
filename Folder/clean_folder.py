from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize
def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_archive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True) # робимо папку для архіва
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(filename, folder_for_file) # TODO: Check!
    except shutil.ReadError:
        print('It is not archive')
        folder_for_file.rmdir()
    filename.unlink()

def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Can't delete folder: {folder}")

def main():
    if len(sys.argv) > 1:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder: {folder_for_scan.resolve()}')
        parser.scan(folder_for_scan)

    for file in parser.JPEG_IMAGES:
        handle_media(file, parser.folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_media(file, parser.folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_media(file, parser.folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handle_media(file, parser.folder / 'images' / 'SVG')
    for file in parser.MP3_AUDIO:
        handle_media(file, parser.folder / 'audio' / 'MP3')

    for file in parser.MY_OTHER:
        handle_media(file, parser.folder / 'MY_OTHER')
    for file in parser.AECHIVES:
        handle_media(file, parser.folder / 'AECHIVES')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)

if __name__ == "__main__":
    main()

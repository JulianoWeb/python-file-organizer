from pathlib import Path
import shutil

from config import CATEGORIES


def get_category(file: Path):
    extension = file.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Outros"


def organize_folder(folder: Path):
    for file in folder.iterdir():
        if not file.is_file():
            continue

        category = get_category(file)

        destination = folder / category

        destination.mkdir(exist_ok=True)

        shutil.move(
            str(file),
            str(destination / file.name)
        )

        print(f"[+] {file.name} -> {category}/")
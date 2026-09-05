from pathlib import Path
from tkinter import Tk, filedialog

from organizer import organize_folder


def main():

    root = Tk()
    root.withdraw()

    folder_selected = filedialog.askdirectory(
        title="Escolha a pasta que deseja organizar"
    )

    root.destroy()

    if not folder_selected:
        print("[-] Nenhuma pasta foi selecionada.")
        return

    folder = Path(folder_selected)

    organize_folder(folder)


if __name__ == "__main__":
    main()


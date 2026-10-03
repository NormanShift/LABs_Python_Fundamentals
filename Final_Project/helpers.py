# Helper functions. Initially used by the menu system in main.py, but can be used by other modules as well.

import os
import subprocess


def clear_screen():
    if os.name == "nt":
        subprocess.run(
            ["cmd", "/c", "cls"],
            check=False
        )
    else:
        subprocess.run(
            ["clear"],
            check=False
        )


def pause():
    input("\nPress Enter to continue...")



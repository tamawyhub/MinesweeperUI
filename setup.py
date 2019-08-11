import sys
from cx_Freeze import setup, Executable

base = None    

executables = [Executable("MinesweeperUI.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "MinesweeperUI",
    options = options,
    version = "1.0.0",
    description = 'The Minesweeper User Interface',
    executables = executables
)

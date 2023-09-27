import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("index.py", base=base)]

build_options = {
    "packages": ["tkinter", "PIL", "pages", "login"],
    "excludes": ["__pycache__"],
    "include_files": [("img", "img")]
}

setup(
    name="TuNombreDeApp",
    version="1.0",
    description="Descripción de tu aplicación",
    options={"build_exe": build_options},
    executables=executables
)

from os import system

NAME = "pbrain-LILLE-Lopacinski.Augustin.exe"
FILES = [
    "pbrain.py",
    "Game.py",
    "Infos.py",
    "algo/attack.py",
    "algo/get_nb_match_pawn.py",
    "algo/min_max.py",
    "algo/peril.py",
]

files_list = ""
for file in FILES:
    files_list += " " + file
system("pyinstaller " + files_list + " --name " + NAME + " --onefile")
system("xcopy dist\\" + NAME + " . /Y")

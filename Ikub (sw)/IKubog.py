import os
import subprocess
import webbrowser
from pathlib import Path
home = str(Path.home())
home = home.replace("\\", "/")
webbrowser.open('https://aternos.org/server/')
subprocess.run(home + "\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
try: os.startfile(home + "\\Desktop\\Salwyrr.lnk")
except: os.startfile(home + "\\AppData\\Roaming\\.Salwyrr\\launcher\\launcher.jar")

# Version: 1.2 (10.05.22)
# Made by Maksiks for IceCubeCraft

import os
import subprocess
import webbrowser
import time
from pathlib import Path
home = str(Path.home())
home = home.replace("\\", "/")
time.sleep(0.2)
subprocess.run(home + "\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
time.sleep(0.4)
try: os.startfile (home + "\\Desktop\\TLauncher.lnk")
except: subprocess.run(home + "\\AppData\\Roaming\\.minecraft\\TLauncher.exe")

webbrowser.open('https://aternos.org/server/')

# Version: 1.2 (Release) (10.05.22)
# Made by Maksiks for IceCubeCraft
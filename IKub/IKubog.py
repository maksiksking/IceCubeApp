import os
import subprocess
import webbrowser
import time
from pathlib import Path
home = str(Path.home())
home = home.replace("\\", "/")
subprocess.run(home + "\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
time.sleep(0.2)
try: os.startfile (home + "\\Desktop\\Minecraft.lnk")
except: subprocess.run("C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe")
time.sleep(1.6)
webbrowser.open('https://aternos.org/server/')

# Version: 1.2 (Release) (10.05.22)
# Made by Maksiks for IceCubeCraft
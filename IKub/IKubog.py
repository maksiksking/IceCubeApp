import os
import subprocess
import webbrowser
from pathlib import Path
home = str(Path.home())
home = home.replace("\\", "/")
webbrowser.open('https://aternos.org/server/')
subprocess.run(home + "\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe")
try: os.startfile (home + "\\Desktop\\Minecraft.lnk")
except: subprocess.run("C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe")

# Version: 1.1 (10.05.22)
# Made by Maksiks for IceCubeCraft
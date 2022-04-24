#from asyncio import subprocess
import os
from whichcraft import which

class General():
    ps_path = which("powershell")
    #class for general use
    def turn_off(self):
        #to turn off the pc
        os.system("shutdown -s -t 0")
        #subprocess.run(["shutdown", "-s", "-t", "0"])

    def reboot(self):
        #to reboot the pc (maybe will mix with turn off)
        os.system("shutdown -s -t 0")
        #subprocess.run(["shutdown", "-r", "-t", "0"])

    def task_kill(self, task:str):
        os.system("taskkill /IM {task} /F")
        #subprocess.run(["taskkill", "/IM", f"{task}", "/F"])

    def task_name(self, task:str):
        pass
import os
import subprocess
from .general import General as gen

class Printers():
    printer_list=[]
    def get_printer_list(self):
        res = subprocess.check_output([gen.ps_path, "Get-Printer", "|", "Format-List"])
        for _ in str(res).split("\\r\\n"):
            if _.startswith("Name"):
                #This will clean lines like the following
                #Name                         : Microsoft Print to PDF
                self.printer_list.append( _.split(":")[1].strip())

    def remove_printer(self, printer_name):
        if self.printer_list:
            subprocess.run([gen.ps_path, "Remove-Printer", "-n", printer_name])
            return "no faile"
        else:
            return "fail"
        
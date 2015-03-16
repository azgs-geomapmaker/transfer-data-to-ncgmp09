import arcpy, os
from arcpy import env

env.workspace = "C:\\Documents\\azgs\\mixed"
executefile = ["execute-mixed.py"]
scripts = os.listdir("C:\\Documents\\transfer-data-to-ncgmp09-master")
for script in scripts:
    if script.endswith(".py"):
        if script not in executefile:
            print script
            execfile(script, {"env.workspace": env.workspace})

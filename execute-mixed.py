import arcpy, os

executefile = ["execute-mixed.py"]
scripts = os.listdir("G:\\scripts\\append\\mixed")
for script in scripts:
    if script not in executefile:
        print script
        execfile(script)

import arcpy, shutil
from arcpy import env


# List all file geodatabases in the current workspace 
# 
workspaces = arcpy.ListWorkspaces("*", "")
for workspace in workspaces: 
    # Compact each geodatabase 
    #
    sr = arcpy.Describe(workspace + "\\GeologicMap").spatialReference
    name = arcpy.Describe(workspace).name
    namepart = name.split(".")
    newname = namepart[0]
    print workspace + " GeologicMap: " + name + "\n"
    print "Create file geodatabase " + name + ". . ."
    shutil.copytree("G:\\templates\\ncgmp\\database\\" + sr.name + ".gdb",
                    "C:\\Documents\\ncgmp\\mixed\\" + newname + ".gdb" )
    print "Copy " + workspace + " complete. . ."


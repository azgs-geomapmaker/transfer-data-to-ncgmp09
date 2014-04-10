import arcpy, shutil
from arcpy import env

# Set the workspace environment
#
env.workspace = "G:\\geologic map data\\azgs\\mixed"

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
                    "G:\\geologic map data\\ncgmp\\mixed\\" + newname + ".gdb" )
    print "Copy " + workspace + " complete. . ."


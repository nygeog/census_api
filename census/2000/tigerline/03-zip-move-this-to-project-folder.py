Select only Feature Class A, Road


Like 'A%'

Make Feature Class for Complete Chain

Join ZipCodes and ZipPlus4 tables

Feature Class to Feature Class






# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "CompleteChain"
arcpy.Buffer_analysis("CompleteChain","C:/Users/danielmsheehan/Documents/ArcGIS/Default.gdb/CompleteChain_Buffer_L","30 Feet","LEFT","ROUND","NONE","#")
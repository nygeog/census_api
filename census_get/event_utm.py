def eventUTM():
	arcpy.TableToTable_conversion(xyList,dd+"/input.gdb","xy_list")
	arcpy.MakeXYEventLayer_management(dd+"/input.gdb/xy_list",lngField,latField,"xy_list_Layer","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision","#")
	arcpy.FeatureClassToFeatureClass_conversion("xy_list_Layer",dd+"/input.gdb","xy_wgs84")
	arcpy.Intersect_analysis(dd+"/input.gdb/xy_wgs84 #;"+utm_bounds,dd+"/input.gdb/xy_wgs84_utm_int","ALL","#","INPUT")

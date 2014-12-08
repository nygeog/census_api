def projTractsGetCounties(fc,myField,outGDB):
    fieldList = arcpy.ListFields(fc)
    for field in fieldList:
        if str.lower(str(field.name)) == str.lower(myField):
            print "    " + fc + " contains fieldname: " + myField
            maxValue = arcpy.SearchCursor(fc, "", "", "", myField + " D").next().getValue(myField) #Get 1st row in descending cursor sort
            minValue = arcpy.SearchCursor(fc, "", "", "", myField + " A").next().getValue(myField) #Get 1st row in ascending cursor sort
            maxValue = int(maxValue)
            minValue = int(minValue)

            for i in range(minValue, maxValue + 1):
                biggestBuf = outGDB+"/xy_wgs84_utm_int_"+ str(i)+"_prj_b"+str(bufList[-1])

                print 'make feature layer for all states tracts'
                arcpy.MakeFeatureLayer_management("W:/GIS/Projects/CensusGet/states_all.gdb/all_states_tracts","all_states_tracts_Layer")

                print 'select tracts by location that intersect with biggest buf layer'
                arcpy.SelectLayerByLocation_management("all_states_tracts_Layer","INTERSECT",biggestBuf,"#","NEW_SELECTION")


                print 'project selected tracts to proper utm zone '+str(i)

                if i == 12:
                    prjInfo = """PROJCS['NAD_1983_UTM_Zone_12N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-111.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]"""
                elif i == 13:
                    prjInfo = """PROJCS['NAD_1983_UTM_Zone_13N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-105.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]"""
                elif i == 14:    
                    prjInfo = """PROJCS['NAD_1983_UTM_Zone_14N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-99.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]"""
                elif i == 15:    
                    prjInfo = """PROJCS['NAD_1983_UTM_Zone_15N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-93.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]"""              
                elif i == 16:    
                    prjInfo = """PROJCS['NAD_1983_UTM_Zone_16N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-87.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]"""
                elif i == 17:    
                    prjInfo = """PROJCS['NAD_1983_UTM_Zone_17N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-81.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]"""
                elif i == 18:    
                    prjInfo = """PROJCS['NAD_1983_UTM_Zone_18N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-75.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]"""
                elif i == 19:
                    prjInfo = """PROJCS['NAD_1983_UTM_Zone_19N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-69.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]"""
                else:
                    print 'error'

                print 'selected tracts from big buffer fc to fc for utm '+str(i)
                arcpy.FeatureClassToFeatureClass_conversion("all_states_tracts_Layer","W:/GIS/Projects/CensusGet/tracts_unprj.gdb","tracts_"+str(i))
                print 'project for utm '+str(i)
                arcpy.Project_management("W:/GIS/Projects/CensusGet/tracts_unprj.gdb/tracts_"+str(i),"W:/GIS/Projects/CensusGet/tracts_prj.gdb/tracts_"+str(i)+'_prj',prjInfo)
                print 'add origarea field'
                arcpy.AddField_management("W:/GIS/Projects/CensusGet/tracts_prj.gdb/tracts_"+str(i)+'_prj',"origarea","FLOAT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                print 'calc origarea field'
                arcpy.CalculateField_management("W:/GIS/Projects/CensusGet/tracts_prj.gdb/tracts_"+str(i)+'_prj',"origarea","!shape.area@squaremeters!","PYTHON_9.3","#")
                

            env.workspace = "W:/GIS/Projects/CensusGet/tracts_unprj.gdb"

            fcList = arcpy.ListFeatureClasses()

            print fcList
            print 'create merged tracts geos for getting counties water'
            arcpy.Merge_management(fcList, "W:/GIS/Projects/CensusGet/counties.gdb/sel_tracts")
            print 'add county id field'
            arcpy.AddField_management("W:/GIS/Projects/CensusGet/counties.gdb/sel_tracts","geoid_county","TEXT","#","#","5","#","NULLABLE","NON_REQUIRED","#")
            print 'calc county id field'
            arcpy.CalculateField_management("W:/GIS/Projects/CensusGet/counties.gdb/sel_tracts","geoid_county","!GEOID![:5]","PYTHON_9.3","#")
            print 'dissolve by county'
            arcpy.Dissolve_management("W:/GIS/Projects/CensusGet/counties.gdb/sel_tracts","W:/GIS/Projects/CensusGet/counties.gdb/sel_tracts_dis_county","geoid_county","#","MULTI_PART","DISSOLVE_LINES")
            print 'project counties just so I can export xy stats'
            arcpy.Project_management("W:/GIS/Projects/CensusGet/counties.gdb/sel_tracts_dis_county","W:/GIS/Projects/CensusGet/counties.gdb/sel_tracts_dis_county_prj","PROJCS['USA_Contiguous_Albers_Equal_Area_Conic',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Albers'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-96.0],PARAMETER['Standard_Parallel_1',29.5],PARAMETER['Standard_Parallel_2',45.5],PARAMETER['Latitude_Of_Origin',37.5],UNIT['Meter',1.0]]","#","GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
            print 'export master list of counties'
            arcpy.ExportXYv_stats("W:/GIS/Projects/CensusGet/counties.gdb/sel_tracts_dis_county_prj","geoid_county","COMMA","W:/GIS/Projects/CensusGet/county_list/county_list.csv","NO_FIELD_NAMES")


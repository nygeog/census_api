import arcpy
from arcpy import env
env.overwriteOutput = True
import csv

xyList =  'Z:/GitHub/census_api/census_get/data/xy_list.csv'
xyList =  'Y:/GitHub/census_api/census_get/data/xy_list.csv'

dataDirectory = 'Z:/Dropbox/GIS/Projects/CensusGet' #iMac
dataDirectory = 'W:/GIS/Projects/CensusGet' #Mac Pro

latField = "Field1"
lngField = "Field2"
bufList = ['500','1000','5000'] #in meters

#UTM BOUNDS DOWNLOAD LOCATION
#https://www.dropbox.com/s/q9drix81l2d7kq6/UTM_Zone_Boundaries.zip?dl=1
utm_bounds = 'Z:/Dropbox/GIS/Data/UTM_Zone_Boundaries/UTM_Zone_Boundaries.shp' #iMac
utm_bounds = 'W:/GIS/Data/UTM_Zone_Boundaries/UTM_Zone_Boundaries.shp' #Mac Pro
state_bounds = 'W:/GIS/Data/Census/census_2010/states/tl_2013_us_state/tl_2013_us_state.shp'

dd = dataDirectory

try:
	arcpy.CreateFileGDB_management(dataDirectory,"input","CURRENT")
except:
	print 'input gdb has already been created'
try:
	arcpy.CreateFileGDB_management(dataDirectory,"processing","CURRENT")
except:
	print 'processing gdb has already been created'
try:
	arcpy.CreateFileGDB_management(dataDirectory,"output","CURRENT")
except:
	print 'output gdb has already been created'

#create GDB states_int, states_all, counties, counties_water 

#create states_list, county_list, download

#create folders in download
#data
#geog
    #2010
        #county
        #county_water
        #tracts
        #blocks
        #block_groups

arcpy.TableToTable_conversion(xyList,dd+"/input.gdb","xy_list")
arcpy.MakeXYEventLayer_management(dd+"/input.gdb/xy_list",lngField,latField,"xy_list_Layer","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision","#")
arcpy.FeatureClassToFeatureClass_conversion("xy_list_Layer",dd+"/input.gdb","xy_wgs84")
arcpy.Intersect_analysis(dd+"/input.gdb/xy_wgs84 #;"+utm_bounds,dd+"/input.gdb/xy_wgs84_utm_int","ALL","#","INPUT")

def CensusGet1(fc,myField,outGDB):
    fieldList = arcpy.ListFields(fc)
    for field in fieldList:
        if str.lower(str(field.name)) == str.lower(myField):
            print "    " + fc + " contains fieldname: " + myField
            maxValue = arcpy.SearchCursor(fc, "", "", "", myField + " D").next().getValue(myField) #Get 1st row in descending cursor sort
            minValue = arcpy.SearchCursor(fc, "", "", "", myField + " A").next().getValue(myField) #Get 1st row in ascending cursor sort
            maxValue = int(maxValue)
            minValue = int(minValue)
            for i in range(minValue, maxValue + 1):
            	fcname = fc.rsplit('/', 1)[1] + '_' + str(i)
            	print fcname
            	exp = '"'+myField+'"' + " = '" + str(i) + "'"
            	infc = fc
            	oufc = outGDB+"/"+fcname
            	arcpy.Select_analysis(infc,oufc,exp)

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

                arcpy.Project_management(outGDB+"/xy_wgs84_utm_int_"+ str(i),outGDB+"/xy_wgs84_utm_int_"+ str(i)+"_prj",prjInfo)

                for j in bufList:
                    dist = str(j) + " Meters"
                    arcpy.Buffer_analysis(outGDB+"/xy_wgs84_utm_int_"+ str(i)+"_prj",outGDB+"/xy_wgs84_utm_int_"+ str(i)+"_prj_b"+str(j),dist,"FULL","ROUND","NONE","#")
        
                biggestBuf = outGDB+"/xy_wgs84_utm_int_"+ str(i)+"_prj_b"+str(bufList[-1])
                arcpy.Intersect_analysis(biggestBuf+" #;W:/GIS/Data/Census/census_2010/states/tl_2013_us_state/tl_2013_us_state.shp","W:/GIS/Projects/CensusGet/states_int.gdb/utm_"+str(i)+'_b'+str(bufList[-1]),"ALL","#","INPUT")

            from arcpy import env
            env.workspace = dd+"states_int.gdb"

            fcList = arcpy.ListFeatureClasses()

            print fcList
            print 'create merged all states'
            arcpy.Merge_management(fcList, "W:/GIS/Projects/CensusGet/states_all.gdb/all_states")
            print 'dissolve by states'
            arcpy.Dissolve_management("W:/GIS/Projects/CensusGet/states_all.gdb/all_states","W:/GIS/Projects/CensusGet/states_all.gdb/all_states_dis","GEOID","#","MULTI_PART","DISSOLVE_LINES")
            print 'export master list of states touched by buffers'
            arcpy.ExportXYv_stats("W:/GIS/Projects/CensusGet/states_all.gdb/all_states_dis","GEOID","COMMA","W:/GIS/Projects/CensusGet/states_list/states_list.csv","NO_FIELD_NAMES")

outGDB = dd + '/processing.gdb'
myField = 'ZONE'
fc = dd+"/input.gdb/xy_wgs84_utm_int"
CensusGet1(fc,myField,outGDB)

statesCSV = dd+"states_list/states_list.csv"

with open(statesCSV, 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

idList = []
for i in your_list:
    idList.append(i[2])

print idList

print 'import modules to donwload zip files of geogs'
import re, urllib, time, zipfile, os

download_location = "W:/GIS/Projects/CensusGet/download/geog/2010/tracts/"

stop_time = 3

state_fips = idList

for k in state_fips:
    url = 'http://www2.census.gov/geo/tiger/TIGER2013/TRACT/tl_2013_'+k+'_tract.zip'
    outzip = download_location + 'tl_2013_'+k+'_tract.zip'
    print 'downloading... ' + url
    urllib.urlretrieve(url, outzip)
    print 'unzipping... ' + outzip
    zipfile.ZipFile(outzip).extractall(download_location)

    time.sleep(stop_time)

from arcpy import env
env.workspace = "W:/GIS/Projects/CensusGet/download/geog/2010/tracts/"

fcList = arcpy.ListFeatureClasses()

print fcList
print 'create merged all states geos (change and create to a variable for tracts/blocks later on)'
arcpy.Merge_management(fcList, "W:/GIS/Projects/CensusGet/states_all.gdb/all_states_tracts")


def CensusGet2(fc,myField,outGDB):
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

CensusGet2(fc,myField,outGDB)

print 'get counties list (csv)'
countyCSV = "W:/GIS/Projects/CensusGet/county_list/county_list.csv"

with open(countyCSV, 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)

idList = []
for i in your_list:
    idList.append(i[2])

print idList

print 'import modules to download zip files of geogs'
import re, urllib, time, zipfile, os

download_location = "W:/GIS/Projects/CensusGet/download/geog/2010/county_water/"

stop_time = 3

county_fips = idList

for k in county_fips:
    
    url = 'http://www2.census.gov/geo/tiger/TIGER2013/AREAWATER/tl_2013_'+k+'_areawater.zip'
    
    outzip = download_location + 'tl_2013_'+k+'_areawater.zip'
    print 'downloading... ' + url
    urllib.urlretrieve(url, outzip)
    print 'unzipping... ' + outzip
    zipfile.ZipFile(outzip).extractall(download_location)

    time.sleep(stop_time)

env.workspace = "W:/GIS/Projects/CensusGet/download/geog/2010/county_water/"

fcList = arcpy.ListFeatureClasses()

print fcList
print 'create merged counties water geos'
arcpy.Merge_management(fcList, "W:/GIS/Projects/CensusGet/counties_water.gdb/sel_water")
print 'intersect water and utm boundaries'
arcpy.Intersect_analysis("W:/GIS/Projects/CensusGet/counties_water.gdb/sel_water #;W:/GIS/Data/UTM_Zone_Boundaries/UTM_Zone_Boundaries.shp #","W:/GIS/Projects/CensusGet/counties_water.gdb/sel_water_int","ALL","#","INPUT")
      

def CensusGet3(fc,myField,outGDB):
    fieldList = arcpy.ListFields(fc)
    for field in fieldList:
        if str.lower(str(field.name)) == str.lower(myField):
            print "    " + fc + " contains fieldname: " + myField
            maxValue = arcpy.SearchCursor(fc, "", "", "", myField + " D").next().getValue(myField) #Get 1st row in descending cursor sort
            minValue = arcpy.SearchCursor(fc, "", "", "", myField + " A").next().getValue(myField) #Get 1st row in ascending cursor sort
            maxValue = int(maxValue)
            minValue = int(minValue)


            for i in range(minValue, maxValue + 1):

                exp = '"'+myField+'"' + " = '" + str(i) + "'"
                infc = "W:/GIS/Projects/CensusGet/counties_water.gdb/sel_water_int"
                oufc = "W:/GIS/Projects/CensusGet/counties_water.gdb/water_utm_"+str(i)
                arcpy.Select_analysis(infc,oufc,exp)

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

                arcpy.Project_management(oufc,oufc+"_prj",prjInfo)
                arcpy.Erase_analysis("W:/GIS/Projects/CensusGet/tracts_prj.gdb/tracts_"+str(i)+"_prj","W:/GIS/Projects/CensusGet/counties_water.gdb/water_utm_"+str(i)+"_prj","W:/GIS/Projects/CensusGet/tracts_prj.gdb/tracts_"+str(i)+"_prj_lnd","#")
                print 'add landarea field utm '+str(i)
                arcpy.AddField_management("W:/GIS/Projects/CensusGet/tracts_prj.gdb/tracts_"+str(i)+'_prj_lnd',"landarea","FLOAT","#","#","#","#","NULLABLE","NON_REQUIRED","#")
                print 'calc landarea field utm '+str(i)
                arcpy.CalculateField_management("W:/GIS/Projects/CensusGet/tracts_prj.gdb/tracts_"+str(i)+'_prj_lnd',"landarea","!shape.area@squaremeters!","PYTHON_9.3","#")
                
CensusGet3(fc,myField,outGDB)



#NEXT UP INTERSECT THE BUFFERS WITH THE TRACTS _lnd 






def CensusGet(xyList, latField, lngField, dataDirectory, censusType, censusYear, variablesList):


xyList =  'Z:/GitHub/census_api/census_get/data/xy_list.csv'
dataDirectory = 'Z:/Dropbox/GIS/Projects/CensusGet'
latField = "Field1"
lngField = "Field2"

#UTM BOUNDS DOWNLOAD LOCATION
#https://www.dropbox.com/s/q9drix81l2d7kq6/UTM_Zone_Boundaries.zip?dl=1
utm_bounds = 'Z:/Dropbox/GIS/Data/UTM_Zone_Boundaries/UTM_Zone_Boundaries.shp'

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
arcpy.TableToTable_conversion(xyList,dd+"/input.gdb","xy_list")
arcpy.MakeXYEventLayer_management(dd+"/input.gdb/xy_list",lngField,latField,"xy_list_Layer","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision","#")
arcpy.FeatureClassToFeatureClass_conversion("xy_list_Layer",dd+"/input.gdb","xy_wgs84")
arcpy.Intersect_analysis(dd+"/input.gdb/xy_wgs84 #;"+utm_bounds,dd+"/input.gdb/xy_wgs84_utm_int","ALL","#","INPUT")

def FindField(fc,myField,outGDB):
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

            	prjInfo12 = "PROJCS['NAD_1983_UTM_Zone_12N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-111.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]"
            	prjInfo13 = "PROJCS['NAD_1983_UTM_Zone_13N',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-105.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]","WGS_1984_(ITRF00)_To_NAD_1983","GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433],METADATA['World',-180.0,-90.0,180.0,90.0,0.0,0.0174532925199433,0.0,1262]]"
            	prjInfo14
            	prjInfo15
            	prjInfo16
            	prjInfo17
            	prjInfo


				listUsaUtmZones = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','55','59','60']
				#later on add all these possible zones for analysis and projection  

            	prjInfo = prjInfo+str(i)
            	arcpy.Project_management(outGDB+"/xy_wgs84_utm_int_"+ str(i),outGDB+"/xy_wgs84_utm_int_"+ str(i)+"_prj",prjInfo)
        #else:
        	#print "    " + fc + " does not contain fieldname: " + myField

outGDB = dd + '/processing.gdb'
myField = 'ZONE'
fc = dd+"/input.gdb/xy_wgs84_utm_int"
FindField(fc,myField,outGDB)



arcpy.Project_management("Z:/Dropbox/GIS/Projects/CensusGet/processing.gdb/xy_wgs84_utm_int_13","Z:/Dropbox/GIS/Projects/CensusGet/processing.gdb/xy_wgs84_utm_int_13_prj",)



# radbufListFn = ['r0050m','r0100m','r0250m','r0500m','r1000m']
# myField = 'expl'

# for a in geogList:
# 	for b in radbufListFn:
# 		fc = wp+'geogs/buffers.gdb/'+a+b
# 		FindField(fc,myField)



#ADD BUFFER SIZES!!!!!


#/Users/danielmsheehan/Dropbox/GIS/Data/UTM_Zone_Boundaries/UTM_Zone_Boundaries.shp
#DOWNLOAD COUNTIES OR STATES, how is utm dictated? by state? 

#INTERSECT DEPENDING ON ZONE PUT THE POINT INTO A UTM ZONE 

#

# if cen2000

# elif acs2012
# elif acs2011
# elif acs2010
# elif acs2009




# else error 
# #maybe should be an except

xyList =  'Z:/GitHub/census_api/census_get/data/xy_list.csv'
dataDirectory = 'Z:/Dropbox/GIS/Projects/CensusGet'
censusType = 'acs5yr' #or census for 2000 or 2010
censusYear = 2012 #2000, 2010, for census 2010, 2011, 2012 for acs 5 year
variablesList = ['totpop']


CensusGet(xyList, dataDirectory, censusType, censusYear, variablesList)
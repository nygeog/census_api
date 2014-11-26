import arcpy

inCSV = open("Z:/GitHub/census_api/census/2000/tigerline/list_of_ny_counties.txt")
countyList = []
for row in inCSV:
	r = row[19:24]
	countyList.append(r)
print countyList
fips = countyList

#REMOVE THIS WHEN 36001 is finsihed
fips = [ '36001']

wd = 'W:/GIS/Data/Census/census_2000/tigerline/counties/'

for i in fips:
	theGDB = wd+"36/"+i+"/tl"+i+".gdb"
	
	infc = wd+'36/'+i+'/CompleteChain.shp'
	sefc = wd+"36/"+i+"/tiger_a_"+i+".shp"
	lay1 = "tiger_a_"+i+"_Layer"
	zipc = wd+"36/"+i+"/ZipCodes.dbf"
	o1fc = "tiger_a_"+i+"_zip"
	lay2 = "tiger_a_"+i+"_zip_Layer"
	o1fp = theGDB + "/tiger_a_"+i+"_zip"
	zip4 = wd+"36/"+i+"/ZipPlus4.dbf"
	o2fc = "tiger_a_"+i+"_zip_plus4"

	bufDist = "60 Feet"

	try:
		arcpy.CreateFileGDB_management(wd+"36/"+i,"tl"+i,"CURRENT")
	except:
		print i + ' gdb is created'
	arcpy.Select_analysis(infc,sefc,""""CFCC" LIKE 'A%'""")
	arcpy.MakeFeatureLayer_management(sefc,lay1)
	arcpy.AddJoin_management(lay1,"TLID",zipc,"TLID","KEEP_ALL")
	arcpy.FeatureClassToFeatureClass_conversion(lay1,wd+"36/"+i+"/tl"+i+'.gdb',o1fc)
	arcpy.MakeFeatureLayer_management(o1fp,lay2)
	arcpy.AddJoin_management(lay2,"TLID",zip4,"TLID","KEEP_ALL")
	arcpy.FeatureClassToFeatureClass_conversion(lay2,wd+"36/"+i+"/tl"+i+'.gdb',o2fc)
	arcpy.Buffer_analysis(theGDB+"/tiger_a_"+i+"_zip_plus4",theGDB+"/"+o2fc+"_l",bufDist,"LEFT","FLAT","NONE","#")
	arcpy.Buffer_analysis(theGDB+"/tiger_a_"+i+"_zip_plus4",theGDB+"/"+o2fc+"_r",bufDist,"RIGHT","FLAT","NONE","#")
	arcpy.FeatureToPoint_management(theGDB+"/"+o2fc+"_l",theGDB+"/"+o2fc+"_l_pt","INSIDE")
	arcpy.FeatureToPoint_management(theGDB+"/"+o2fc+"_r",theGDB+"/"+o2fc+"_r_pt","INSIDE")


#MAKE SURE COUNT OF ZIP 4's = the ZIP 4 count in the input file

GET ESRI 9-01 DATA ZIP CODES!!!!!!!
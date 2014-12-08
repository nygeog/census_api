def createDirs():
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
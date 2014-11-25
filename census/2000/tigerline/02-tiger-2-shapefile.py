import os

############
############
############
# NOTE YOU HAVE TO RUN THIS FROM TERMINAL
# python /Users/danielmsheehan/GitHub/census_api/census/2000/tigerline/02-tiger-2-shapefile.py
############
############
############

inCSV = open("/Users/danielmsheehan/GitHub/census_api/census/2000/tigerline/list_of_ny_counties.txt")
countyList = []
for row in inCSV:
	r = row[19:24]
	countyList.append(r)
print countyList
fips = countyList

for i in fips:
	print 'create folders for each county '+i
	directory = '/Users/danielmsheehan/Dropbox/GIS/Data/Census/census_2000/tigerline/counties/36/'+i
	if not os.path.exists(directory):
	    os.makedirs(directory)

	inFile = '/Users/danielmsheehan/Dropbox/GIS/Data/Census/census_2000/tigerline/counties/36/TGR'+i+'.RT1'
	ouFold = '/Users/danielmsheehan/Dropbox/GIS/Data/Census/census_2000/tigerline/counties/36/'+i
	gdalCMD = 'ogr2ogr -overwrite -f "ESRI Shapefile" '+ouFold+' '+inFile #TGR36001.RT1'

	print gdalCMD
	os.system(gdalCMD)



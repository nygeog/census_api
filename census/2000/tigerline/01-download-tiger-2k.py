import re, urllib, time, zipfile, os 

download_location = "/Volumes/Hotel/Dropbox/GIS/Data/Census/census_2000/tigerline/"

inCSV = open("list_of_ny_counties.txt")

countyList = []

for row in inCSV:
	r = row[16:28]
	countyList.append(r)

print countyList
fips = countyList

url_pre = "ftp://ftp2.census.gov/geo/tiger/tiger2k/ny/"
url_mid = ""#tgr"
#url_ltr = "_d90_shp"
url_zip = ".zip"

stop_time = 3

#loop through all the county fips
for fi in fips:
	

	dlZIP = url_pre + url_mid + fi #+ url_zip
	inZIP = download_location+url_mid + fi #+ url_zip
	print dlZIP
	print inZIP

	#download the zip file
	urllib.urlretrieve(dlZIP, inZIP)
	print "Downloading... " + fi 

	#unzip the file
	zipfile.ZipFile(inZIP).extractall(download_location+"/")
	print "Unzipping... " + fi 

	#delete the zip file
	#os.remove(download_location+url_mid + fi + url_ltr + zipfile_year + url_zip)
	#print "Deleting... " + fi + "'s ZIP file"

	#wait 3 seconds in case network connection is slow
	time.sleep(stop_time)


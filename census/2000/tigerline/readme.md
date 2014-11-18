###Batch Download Census TIGER/line with Python

1. Go to this website for the state you need, 
ftp://ftp2.census.gov/geo/tiger/tiger2k/ny/

2. In Google Chrome-> View Source -> Copy the rows that look like this. 
<script>addRow("tgr36001.zip","tgr36001.zip",0,"1.8 MB","10/11/01, 12:00:00 AM");</script>

3. Save as a txt in Sublime Text. Save as list_of_ny_counties.txt (sub ny for whatever state or use the fips (36))

4. Modify and run the script. 


#####the python script
	

		
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
import urllib2
import json
import csv
import sys, re, time

pause = 1

proj_path = '/Volumes/Echo/GIS/projects/transit/tasks/201405_transit/data/input/census_fact_finder/vehicle/2012_acs5yr/original/'
pp = proj_path
pd = pp


totpop  = ["B01003_001E"] #Total Population (Weighted)

vehic1 = ["B25044_001E",
"B25044_002E",
"B25044_003E",
"B25044_004E",
"B25044_005E",
"B25044_006E",
"B25044_007E",
"B25044_008E",
"B25044_009E",
"B25044_010E",
"B25044_011E",
"B25044_012E",
"B25044_013E",
"B25044_014E",
"B25044_015E",
"B25045_001E",
"B25045_002E",
"B25045_003E",
"B25045_004E",
"B25045_005E",
"B25045_006E",
"B25045_007E",
"B25045_008E",
"B25045_009E",
"B25045_010E",
"B25045_011E",
"B25045_012E",
"B25045_013E",
"B25045_014E",
"B25045_015E",
"B25045_016E",
"B25045_017E",
"B25045_018E",
"B25045_019E"]

vehic2 = ["B25046_001E",
"B25046_002E",
"B25046_003E"]


variabletypelist   =[ totpop , vehic1 , vehic2 ]
variabletypelistnm =['totpop','vehic1','vehic2']

statesList = ["01","02","04","05","06","08","09","10","11","12","13","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","44","45","46","47","48","49","50","51","53","54","55","56","72"]

for state in statesList:
	for topic, topicnm in zip(variabletypelist, variabletypelistnm):
		#----
		print 'OKAY NOW RUN THE API GRABS'

		print 'get '+topicnm+' vars'
		allcensusvars   = ','.join(topic)
		censusapipreurl = "http://api.census.gov/data/2010/acs5?key="
		censusapikey    = "30699f15ab4d04a1e0943715b539d256c9a3ee44"
		gettxt          = "&get="
		forgeog         = "&for=tract:*"
		instate         = "&in=state:" + state
		url = censusapipreurl + censusapikey + gettxt + allcensusvars + forgeog + instate
		print url
		data = urllib2.urlopen(url).read()
		data = json.loads(data)
		fname = pd+"acs5yr_2012_tract_st"+state+"_"+topicnm+".csv"
		with open(fname,'wb') as outf:
		    outcsv = csv.writer(outf)
		    outcsv.writerows(data)
		time.sleep(pause)
		#----
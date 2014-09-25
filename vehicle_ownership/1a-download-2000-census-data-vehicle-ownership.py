import urllib2
import json
import csv
import sys, re, time

pause = 1

proj_path = '/Volumes/Echo/GIS/projects/transit/tasks/201405_transit/data/input/census_fact_finder/vehicle/2000_census/original/'
pp = proj_path
pd = pp


totpop  = ["P001001"] 

vehic1 = ["H044001",
"H044002",
"H044003",
"H044004",
"H044005",
"H044006",
"H044007",
"H044008",
"H044009",
"H044010",
"H044011",
"H044012",
"H044013",
"H044014",
"H044015",
"H045001",
"H045002",
"H045003",
"H045004",
"H045005",
"H045006",
"H045007",
"H045008",
"H045009",
"H045010",
"H045011",
"H045012",
"H045013",
"H045014",
"H045015",
"H045016",
"H045017",
"H045018",
"H045019",
"H045020",
"H045021",
"H045022",
"H045023",
"H045024",
"H045025",
"H045026",
"H045027",
"H045028",
"H045029",
"H045030",
"H045031",
"H045032",
"H045033",
"H045034",
"H045035"]

vehic2 = ["H046001",
"H046002",
"H046003"]


variabletypelist   =[ totpop , vehic1 , vehic2 ]
variabletypelistnm =['totpop','vehic1','vehic2']

statesList = ["01","02","04","05","06","08","09","10","11","12","13","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","44","45","46","47","48","49","50","51","53","54","55","56","72"]

for state in statesList:
	for topic, topicnm in zip(variabletypelist, variabletypelistnm):
		#----
		print 'OKAY NOW RUN THE API GRABS'

		print 'get '+topicnm+' vars'
		allcensusvars   = ','.join(topic)
		censusapipreurl = "http://api.census.gov/data/2000/sf3?key="
		censusapikey    = "30699f15ab4d04a1e0943715b539d256c9a3ee44"
		gettxt          = "&get="
		forgeog         = "&for=tract:*"
		instate         = "&in=state:" + state
		url = censusapipreurl + censusapikey + gettxt + allcensusvars + forgeog + instate
		print url
		data = urllib2.urlopen(url).read()
		data = json.loads(data)
		fname = pd+"census_2000_tract_st"+state+"_"+topicnm+".csv"
		with open(fname,'wb') as outf:
		    outcsv = csv.writer(outf)
		    outcsv.writerows(data)
		time.sleep(pause)
		#----
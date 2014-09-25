import urllib2
import json
import csv
import sys, re, time

pause = 1

proj_path = '/Volumes/Echo/GIS/projects/nets/tasks/201406_nets_sum_by_flag/'
pp = proj_path
pd = pp + 'data/input/census/'


totpop = ["P0010001"] #Total Population (Weighted)


variabletypelist   =[ totpop ]
variabletypelistnm =['totpop']

statesList = ['36','34','42']

for state in statesList:
	for topic, topicnm in zip(variabletypelist, variabletypelistnm):
		#----
		print 'OKAY NOW RUN THE API GRABS'

		print 'get '+topicnm+' vars'
		allcensusvars   = ','.join(topic)
		censusapipreurl = "http://api.census.gov/data/2010/sf1?key="
		censusapikey    = "30699f15ab4d04a1e0943715b539d256c9a3ee44"
		gettxt          = "&get="
		forgeog         = "&for=tract:*"
		instate         = "&in=state:" + state
		url = censusapipreurl + censusapikey + gettxt + allcensusvars + forgeog + instate
		print url
		data = urllib2.urlopen(url).read()
		data = json.loads(data)
		fname = pd+"census_2010_tract_st"+state+"_"+topicnm+".csv"
		with open(fname,'wb') as outf:
		    outcsv = csv.writer(outf)
		    outcsv.writerows(data)
		time.sleep(pause)
		#----
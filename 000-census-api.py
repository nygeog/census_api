import pandas as pd
import csv
import urllib2
import json
import sys, re, time

# proj_path = '/Volumes/Echo/GIS/projects/streetview/tasks/201403_canvas_paper_edits/'
# pp = proj_path
# pd = pp + 'data'

infile = 'list.txt'

cr = csv.reader(open(infile,"rb"))

idList = []

for row in cr:
	idList.append(row)

print idList


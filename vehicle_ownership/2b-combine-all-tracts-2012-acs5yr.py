import pandas as pd
import glob
import csv

pp = '/Volumes/Echo/GIS/projects/transit/tasks/201405_transit/data/input/census_fact_finder/vehicle/2012_acs5yr/'
pt = pp + 'original/'

variabletypelistnm =['totpop','vehic1','vehic2']

for k in variabletypelistnm:
	exp = "*"+k+".csv"
	all_csvs = glob.glob(pt+exp)
	print all_csvs
	df_list = []
	print "concatenating (merge) all tracts into 1 file"
	i = 0
	for j in all_csvs:

		df = pd.read_csv(j, header=0, dtype={'state':object,'county':object,'tract':object})
		df_list.append(df)
		i += 1
		print i
	df   = pd.concat(df_list)
	df   = df.sort_index(axis=1)
	df.to_csv(pp+'acs5yr_2012_'+k+'.csv', sep=',', index=False)
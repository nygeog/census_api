import pandas as pd
import glob
import csv

proj_path = '/Volumes/Echo/GIS/projects/nets/tasks/201406_nets_sum_by_flag/'
pp = proj_path
pt = pp + 'data/input/census/'

csv_dir = pt
out_dir = pt

all_csvs = glob.glob(csv_dir+"*totpop.csv")

df_list = []

print "concatenating (merge) all tracts into 1 file - 11 seconds"

i = 0
for allcsvs in all_csvs:

	df = pd.read_csv(allcsvs, header=0, dtype={'state':object,'county':object,'tract':object})
	df_list.append(df)
	i += 1
	print i

df   = pd.concat(df_list)
df   = df.sort_index(axis=1)

df.to_csv(out_dir+'census_2010_tracts.csv', sep=',', index=False)
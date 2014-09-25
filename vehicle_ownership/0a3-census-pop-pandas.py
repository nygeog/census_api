import pandas as pd

proj_path = '/Volumes/Echo/GIS/projects/nets/tasks/201406_nets_sum_by_flag/'
pp = proj_path
pt = pp + 'data/input/census/'

inFile  = pt + 'census_2010_tracts.csv'
outFile = pt + 'census_2010_tracts_geoid.csv'

df = pd.read_csv(inFile, dtype={'state':object,'county':object,'tract':object})

df['GEOID10'] = df['state'] + df['county'] + df['tract']
df = df.drop(['state','county','tract'], axis=1)
df['count'] = 1
df = df.groupby(['GEOID10','P0010001']).sum()
df = df.sort(['count'], ascending=False)
df.to_csv(outFile, index=True)
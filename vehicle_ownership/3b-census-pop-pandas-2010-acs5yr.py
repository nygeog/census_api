import pandas as pd

pp = '/Volumes/Echo/GIS/projects/transit/tasks/201405_transit/data/input/census_fact_finder/vehicle/2012_acs5yr/'
pt = pp + 'data/input/census/'

#start updating here 

inFile  = pt + 'census_2010_tracts.csv'
outFile = pt + 'census_2010_tracts_geoid.csv'

df = pd.read_csv(inFile, dtype={'state':object,'county':object,'tract':object})

df['GEOID10'] = df['state'] + df['county'] + df['tract']
df = df.drop(['state','county','tract'], axis=1)
df['count'] = 1
df = df.groupby(['GEOID10','P0010001']).sum()
df = df.sort(['count'], ascending=False)
df.to_csv(outFile, index=True)
from create_dirs import createDirs
from utm_state import getUTMandState
from event_utm import eventUTM
from proj_utm_states import projUTMStates
from download_tracts import downloadTracts
from proj_tracts_get_counties import projTractsGetCounties
from get_hydro import getHydro
from erase_water import eraseWater 

xyList =  'Y:/GitHub/census_api/census_get/data/xy_list.csv'
latField = "Field1"
lngField = "Field2"
bufList = ['500','1000','5000'] 
dataDir = 'W:/GIS/Projects/CensusGet'
dd = dataDir

outGDB = dd + '/processing.gdb'
myField = 'ZONE'
fc = dd+"/input.gdb/xy_wgs84_utm_int"

#projUTMStates(fc,myField,outGDB)
#projTractsGetCounties(fc,myField,outGDB)
#eraseWater(fc,myField,outGDB)




def getHydro():
    print 'get counties list (csv)'
    countyCSV = "W:/GIS/Projects/CensusGet/county_list/county_list.csv"

    with open(countyCSV, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    idList = []
    for i in your_list:
        idList.append(i[2])

    print idList

    print 'import modules to download zip files of geogs'
    import re, urllib, time, zipfile, os

    download_location = "W:/GIS/Projects/CensusGet/download/geog/2010/county_water/"

    stop_time = 3

    county_fips = idList

    for k in county_fips:
        
        url = 'http://www2.census.gov/geo/tiger/TIGER2013/AREAWATER/tl_2013_'+k+'_areawater.zip'
        
        outzip = download_location + 'tl_2013_'+k+'_areawater.zip'
        print 'downloading... ' + url
        urllib.urlretrieve(url, outzip)
        print 'unzipping... ' + outzip
        zipfile.ZipFile(outzip).extractall(download_location)

        time.sleep(stop_time)

    env.workspace = "W:/GIS/Projects/CensusGet/download/geog/2010/county_water/"

    fcList = arcpy.ListFeatureClasses()

    print fcList
    print 'create merged counties water geos'
    arcpy.Merge_management(fcList, "W:/GIS/Projects/CensusGet/counties_water.gdb/sel_water")
    print 'intersect water and utm boundaries'
    arcpy.Intersect_analysis("W:/GIS/Projects/CensusGet/counties_water.gdb/sel_water #;W:/GIS/Data/UTM_Zone_Boundaries/UTM_Zone_Boundaries.shp #","W:/GIS/Projects/CensusGet/counties_water.gdb/sel_water_int","ALL","#","INPUT")
      
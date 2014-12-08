def downloadTracts():
    statesCSV = dd+"states_list/states_list.csv"

    with open(statesCSV, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    idList = []
    for i in your_list:
        idList.append(i[2])

    print idList

    print 'import modules to donwload zip files of geogs'
    import re, urllib, time, zipfile, os

    download_location = "W:/GIS/Projects/CensusGet/download/geog/2010/tracts/"

    stop_time = 3

    state_fips = idList

    for k in state_fips:
        url = 'http://www2.census.gov/geo/tiger/TIGER2013/TRACT/tl_2013_'+k+'_tract.zip'
        outzip = download_location + 'tl_2013_'+k+'_tract.zip'
        print 'downloading... ' + url
        urllib.urlretrieve(url, outzip)
        print 'unzipping... ' + outzip
        zipfile.ZipFile(outzip).extractall(download_location)

        time.sleep(stop_time)

    from arcpy import env
    env.workspace = "W:/GIS/Projects/CensusGet/download/geog/2010/tracts/"

    fcList = arcpy.ListFeatureClasses()

    print fcList
    print 'create merged all states geos (change and create to a variable for tracts/blocks later on)'
    arcpy.Merge_management(fcList, "W:/GIS/Projects/CensusGet/states_all.gdb/all_states_tracts")

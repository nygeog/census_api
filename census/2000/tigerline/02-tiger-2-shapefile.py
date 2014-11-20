#import re, urllib, time, zipfile, os 

download_location = "/Volumes/Hotel/Dropbox/GIS/Data/Census/census_2000/tigerline/counties/test/"  #TEST FOLDER FOR NOW


#OGR TO OGR code, masuffolk is the folder
ogr2ogr -f "ESRI Shapefile" masuffolk TGR25025.RTI

ogr2ogr -f "ESRI Shapefile" out TGR36001.RT1
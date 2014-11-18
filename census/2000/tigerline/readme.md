###Batch Download Census TIGER/line with Python

1. Go to this website for the state you need, 
ftp://ftp2.census.gov/geo/tiger/tiger2k/ny/

2. In Google Chrome-> View Source -> Copy the rows that look like this. 
<script>addRow("tgr36001.zip","tgr36001.zip",0,"1.8 MB","10/11/01, 12:00:00 AM");</script>

3. Save as a txt in Sublime Text. Save as list_of_ny_counties.txt (sub ny for whatever state or use the fips (36))

4. Modify and run the script. 
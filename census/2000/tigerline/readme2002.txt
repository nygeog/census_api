June 2003

U.S. CENSUS BUREAU
TIGER/Line 2002

Census TIGER(R) and TIGER/Line(R) are registered trademarks of the
U.S. Census Bureau.  ZCTA(TM) is a trademark of the U.S. Census Bureau.  
Windows is a registered trademark of the Microsoft Corporation.  ADOBE, 
Acrobat, and Acrobat Reader are registered trademarks of Adobe Systems 
Inc.  ZIP Code and ZIP+4 are trademarks of the U.S. Postal Service.

Some legal boundaries and names are those reported to the U.S. Census 
Bureau to be legally in effect on January 1, 2000 (Census 2000 geographic 
areas) while others are updated and legally in effect as of the latest 
Boundary and Annexation Survey (BAS) (current geographic areas).  The 
current boundaries represented in the 2002 TIGER/Line files are those 
reported to the Census Bureauu by April 1, 2002 as being in effect as of 
January 1, 2002.  The boundary information in the TIGER/Line files for 
both legal and statistical entities are for Census Bureau statistical data 
collection and tabulation purposes only; their depiction and designation 
for statistical purposes does not constitute a determination of 
jurisdictional authority or rights of ownership or entitlement.

WHAT ARE TIGER/LINE FILES

The TIGER/Line files were created from the Census Bureau's TIGER
(Topologically Integrated Geographic Encoding and Referencing) database
of selected geographic and cartographic information. TIGER was 
developed at the Census Bureau to support the mapping and related 
geographic activities required by the decennial and economic censuses 
and sample survey programs.  TIGER/Line files are made available to the 
public and are typically used by people to provide the digital map base 
for their Geographic Information System or mapping software.

This CD-ROM does not contain software to display or generate maps, nor 
is the data on this CD-ROM in the form of a map image.  To create maps 
with the data on this CD-ROM, one would typically use a Geographic 
Information System package or other mapping software.  The Census 
Bureau cannot provide help in how to use this data with specific 
software packages.  The TIGER/Line files are provided in ASCII text 
format only.  Users are responsible for converting or translating the 
files into a format used by their specific software package.   

For information on how to use the TIGER/Line data with a specific 
software package one should contact the company that produced the
software. For information on companies that sell products that use
TIGER/Line data or that provide various TIGER/Line-related services 
refer to the "Vendor's List" on the TIGER Page at the Census Bureau's 
World Wide Web site described below.

ACCESSING TIGER/LINE FILES

The TIGER/Line files are distributed on CD-ROM and on the Census 
Bureau's Internet site (www.census.gov).  This README.TXT file 
references both the disc and Internet distribution methods.  For those 
downloading the TIGER/Line files from the Internet, unless otherwise 
noted, you can find the supplementary files mentioned below through 
links from the TIGER/Line download page.

WHAT'S NEW - KEY CHANGES

The 2002 TIGER/Line files include files for all counties and 
statistically equivalent entities in the United States as well as 
files for Puerto Rico and the Island Areas.  The 2002 TIGER/Line 
files are released by county or statistically equivalent entity 
based on the current boundaries in effect as of January 1, 2002 as 
reported to the Census Bureau by April 1, 2002.  Since Census 
2000 there have been changes in the universe of counties or 
statistically equivalent entities.  In Colorado, Broomfield County 
was created from parts of Adams, Boulder, Jefferson, and Weld Counties.  
This change has resulted in the creation of a separate TIGER/Line file 
for Broomfield County, Colorado.  In Virginia, the independent city of 
Clifton Forge changed its status to become Clifton Forge town and is 
now part of Alleghany County, Virginia; it appears in the Alleghany 
County, Virginia TIGER/Line file.  Beginning with the 2002 TIGER/Line 
files, the Census Bureau no longer will produce a TIGER/Line file for 
the Midway Islands.

The 108th Congressional Districts do not appear in the 2002 TIGER/Line 
files. The Census Bureau still was in the process of collecting this 
information from the states at the time of the creation of the 2002 
TIGER/Line files. 

The 2002 TIGER/Line files contain few, if any, updates to street
features or address ranges from the Census 2000 versions of the
TIGER/Line files.  Some additional features may have been added in the
20 counties where the Census Bureau improved the street feature 
coordinates.  In a few instances some new features may appear, and 
address ranges could have been added or updated, to resolve challenges 
as part of the Census 2000 Count Question Resolution (CQR) Program.  
As part of a research project to upgrade the positional accuracy of
TIGER data, the Census Bureau improved the street feature coordinates 
in the following counties:  Kent, New Castle, and Sussex Counties in 
Delaware; Seminole County in Florida; Cecil, Somerset and Talbot 
Counties in Maryland; Baltimore City in Maryland; Auglaize, Crawford, 
Defiance, Delaware, Fulton, Henry, Miami, Putnam, Richland, Van Wert, 
and Williams Counties in Ohio; and Hughes County in South Dakota. 

The Census Bureau has made major changes to the structure, field 
definitions, and contents for the 2002 TIGER/Line files.  New record 
types have been added, two record types were deleted, and several 
record types were expanded and substantially revised.  The Census 
Bureau has removed the 1990 geography from the 2002 TIGER/Line files 
replacing it with current geography.  Also new for the 2002 TIGER/Line 
files is a permanent zero-cell (or node) identification number (TZID) 
for each node. 

To improve the ability of data users to merge multiple counties, the
Census Bureau is adding the state and county codes to those Record Type
1 records for the adjacent county (these are the Record Type 1 records
that have the single-sided segment flag set, and until this version,
all the data elements for the side of the record "outside" the county
have been blank).  The Census Bureau also is making the TLIDs and TZIDs
for these records the same.  Thus the county boundary segments and
zero-cells in adjacent counties will now have the same TLID and TZID.

TIGER/LINE AND ACCOMPANYING FILES

The Census 2000 TIGER/Line files contain digital cartographic data and 
are accompanied by documentation and related files. These files are 
distributed as a disc-on-demand CD-ROM product and on the Census 
Bureau's Internet site (www.census.gov).  On the Internet site (start 
with the "TIGER" link from the home page) there are links to  the 
directory/folder for each state where the individual files are stored.  
Other links lead one to the accompanying files.

On the CD-ROM the TIGER/Line data is stored in the TIGER directory in 
subdirectories by state.  Each state subdirectory is named using the 
two-digit FIPS code and the Post Office abbreviation for the state 
(ex. 02_AK for Alaska).  Within the state subdirectory each county 
file has the name TGRssccc.ZIP, where the "ss" is the state FIPS code 
and "ccc" is the county FIPS code.  Appendix A of the TIGER/line 
documentation provides a list of counties and their FIPS codes by state. 

The data for each county (or statistically equivalent entity) is stored  
in a single compressed file that, when decompressed, results in up to  
19 separate files representing each of the TIGER/Line record types that 
exist for that county.  Some counties did not require all of the 19 
record types and therefore will have less than 19 files. If the types 
of data contained in record types 4, 6, 7, 8, B and Z are not 
appropriate for a given county then the files for those record types 
will NOT be included. New Record Types E and U do not appear in the 
2002 TIGER/Line files.  The name of each of these files uses a 
modification of the above convention (TGRssccc.RTx) where "x" is the 
Record Type.  The data in these files is in a standard ASCII format.  The 
Census Bureau does NOT release the TIGER/Line data or an extract of the 
internal Census TIGER database in vendor-specific GIS/mapping software 
formats.

Information on the content of each record type can be found in Chapter 
6 of the TIGER/Line documentation.  Information on decompressing the 
data files is found below under the heading "DATA COMPRESSION".  

The files use the TIGER/Line record formats as described in the
accompanying documentation.  When decompressed they are fixed length
ASCII with record separators (carriage return, line feed). 

ADDITIONAL FILES:

COUNTSss.TXT

Each CD-ROM contains COUNTSss.TXT files in the subdirectory for each 
state under the TIGER directory of the disc.  If you are downloading 
from the Census Internet site they can be found in the appropriate 
state folder.  The file name will have the appropriate state FIPS code 
in place of "ss" in the file name.  The COUNTSss.TXT files show the 
counts for the number of records for each record type by county for 
all states that are included on the CD-ROM.  Note that all counties 
are listed for a given state.  The layout of COUNTSss.TXT is  as 
follows:

FIPS state code       16:17
FIPS county code      20:22
Creation date         25:30
Record type           33:33
Record Count          36:43

An important aspect of the COUNTSss.TXT file is the "Creation Date"
information for these files.  This date is the date the TIGER/Line file
was created from a benchmark of the TIGER database.  The process of 
creating TIGER/Line files involves extracting the appropriate data from 
various internal data sets to create what we term a TIGER/Line 
benchmark.  Essentially this benchmark is a snapshot in time of our 
TIGER databases which are constantly being updated.  From this 
benchmark we create the TIGER/Line files for use in our operations.  
Depending on the nature of the operation for which the files are being 
created, this process can proceed over several months as the sets of 
files for individual states are created.  The VERSION CODE field in 
TIGER/Line identifies the benchmark used and one can determine the 
vintage of the file from the information in this field (see page 2-1 of 
the TIGER/Line documentation).  However, infrequently errors are found 
in the benchmark or in the software that produces the TIGER/Line files.  
Corrections are made to the benchmark file and then a new TIGER/Line is 
created from the benchmark.  In these situations the VERSION CODE for 
the original and corrected files would be the same but the "Creation 
Date" information in the COUNTSss.TXT file would reflect the different 
vintages.  

README.TXT

The document that you are presently reading.

DOCUMENTATION

The documentation for the TIGER/Line files is contained in the TECHDOC
subdirectory of the CD-ROM.   The file name is TGR2002.pdf and is 
provided in the PDF format which requires the ADOBE Acrobat Reader 
(version 3.0 or higher).  We are including the installation software 
for the ar505enu.exe version (5.05) of the reader in the 
TECHDOC/ACROREAD CD-ROM directory. If you have a version of Acrobat 
Reader more current than version 5.05, do not install the version of 
Acrobat Reader contained on the 2002 TIGER/Line CD-ROM.

Included here are ADOBE's instructions for the installation of the 
Reader software: "Copy this software to the hard drive of your computer 
and run it.  It will install the version 5.05 of the ADOBE Reader 
software on your computer.  If there is a failure at any point during 
the installation of Acrobat Reader, the installer performs a complete 
uninstall. For this reason, it is  important not to close the installer 
application by clicking its close box in the upper right corner of the 
background window after clicking the "Thank You" dialog box that 
appears at the end of the installation. If you wait for a second or 
two, the installer will automatically close the background windows 
after the installation is complete."

When the installation is complete you can view the TIGER/Line 
documentation by running the ADOBE Reader and selecting the TGR2002.pdf 
file from the "Open" menu.  To get the ADOBE Reader for other computer 
platforms visit the ADOBE Web site for the proper software 
(http://www.adobe.com).

METADATA

Federal Geographic Data Committee (FGDC) compliant metadata is included 
on the CD-ROM in the TIGER subdirectory.  It is also available from the 
Census Internet download site. 

DATA COMPRESSION

The TIGER/Line data on this disk has been compressed into an archive 
file to save space and reduce the number of disks required for the data 
and to facilitate downloading from the Internet.  If the files were not 
compressed it would require over 40 CD-ROM disks to hold the data 
needed to cover the entire United States.  They are compressed into the 
widely used zip format.  Software applications to decompress files in 
this format are widely available.

KNOWN PROBLEMS AND ANOMALIES WITH THIS TIGER/LINE DATA SET:

DUPLICATE TIGER/LINE ID (TLID)

Because of a unique situation in seven counties or statistical 
equivalents of counties the Census Bureau inadvertently created two line 
segments with the same TIGER/Line ID (TLID) within the same county.  
The Census Bureau has corrected the problem and regenerated the TIGER/Line
files for Juneau Borough, Alaska (FIPS code 02110); Pierce County, Georgia
(FIPS code 13229); Ware County, Georgia (FIPS code 13299); James City
County, Virginia (FIPS code 51095), Prince William County, Virginia (FIPS
code 51153); Manassas City, Virginia (FIPS code 51683); and Williamsburg
City, Virginia (FIPS code 51830) in June 2003.  The regenerated 2002
TIGER/Line files have a version code of 0503.

TIGER ZERO-CELL ID (TZID)

Because the 2002 TIGER/Line files are the first version of the 
TIGER/Line files to contain the permanent zero-cell identification 
number (TZID), we expect there to be some possible differences between 
the TZIDs in the 2002 and the 2003 TIGER/Line files.  The Census Bureau
expects the TZIDs to be stable in the 2003 and later versions of the 
TIGER/Line files.  The differences will mainly appear in the 20 counties 
listed in the What's New - Key Changes section of this document where 
the Census Bureau improved the street feature coordinates and possibly 
their adjacent counties. 

RANGE OF TIGER/LINE IDENTIFICATION NUMBERS (TLIDS) IN RECORD TYPE R

Record Type H contains the range of unique complete chain record numbers
assigned to a census file.  In counties with changes to their county
boundaries after January 1, 2000, the complete range of TLIDs within the
current county boundary do not appear in Record Type R of the 2002 
TIGER/Line file for that county.  Users will need to reference Record 
Type R from the adjoining county to identify the potential range of
unique complete chain record numbers.

ADDRESS ANOMALIES IN PUERTO RICO 

The TIGER/Line files contain some address range coverage for Puerto 
Rico. However, use of this information for geocoding purposes may be 
problematic and the data user should proceed with caution.  These 
address ranges are preliminary attempts at using Puerto Rico address 
ranges in Census Bureau files.  Due to the lack of software or 
resources to handle some of the more unique aspects of addressing in 
Puerto Rico, the address ranges were entered without the standard edits 
and quality checks used in other parts of the United States. 
Improvements in software and address standardization for Puerto Rico 
are expected in the future.  At present, there are inconsistencies, 
overlaps, and duplication of address ranges. Address ranges may lack 
alpha character prefixes or have hyphenated prefixes. The files also 
lack the community names used in a four-line address that the U.S. 
Postal Service requires to avoid duplicate addresses. Errors in the 
reference files, and other factors may limit the usefulness of this 
product for geocoding purposes. 

ROAD  FEATURE  ANOMALIES

The Census Bureau extracts TIGER/Line files from the TIGER database
which is continually updated. During the clerical update process for 
some Census 2000 operations errors caused anomalies to be introduced 
into some chains represented in Record Types 1 and 2. For these cases 
road features may appear in the 2002 TIGER/Line files unconnected to 
other road features (so-called floating features) or severely skewed in 
relation to surrounding line features of any type.  We correct these 
errors as we find them, however, it is likely that some still exist. 

Another road feature anomaly is the sporadic occurrence of road 
segments with a misclassified Census Feature Class Code (CFCC).  The 
result is that complete chains for the affected road features will have 
segments with different CFCC values assigned erroneously.  This problem 
could affect applications that use the CFCC values for network 
analysis, routing, or for assigning symbology to a feature when 
creating a map.  We believe that these errors were introduced 
inadvertently during an updating operation to edit address range 
information on new as well as existing records.  We are continuing to 
correct these as they are discovered.  

QUESTIONS AND ADDITIONAL INFORMATION

Questions about the Census TIGER/Line files and future plans for this 
and other TIGER-related products may be directed to the Geographic 
Products Management Branch of the Geography Division at (301) 763-1128 
or to the e-mail address tiger@census.gov.

General information about TIGER-related products is available from the
TIGER page on the Census Bureau's World Wide Web site 
(http://www.census.gov/geo/www/tiger/). This Web site also is a source
of other information that is of specific interest to TIGER/Line users 
and of general interest regarding the geographic programs at the Census 
Bureau.  As appropriate, additional information about this product will 
be posted, such as ERRATA or USER NOTES.



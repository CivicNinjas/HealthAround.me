#!/bin/bash
set -e  # Exit on errors

# 11 = DC
# 24 = Maryland
# 25 = Massachusetts
# 40 = Oklahoma
# 42 = Pennsylvania
# 51 = Virginia

STATES="11 24 25 40 42 51"
IFS=" "

# Fetch files if they aren't already downloaded
wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/COUNTY/tl_2013_us_county.zip
wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/STATE/tl_2013_us_state.zip
wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/STATE/tl_2013_us_state.zip
for state in $STATES
do
    wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/TRACT/tl_2013_${state}_tract.zip  # Tract
    wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/BG/tl_2013_${state}_bg.zip  # Block Group
done
chmod 664 *.zip

# Did the STATES list change
if [ -f .imported_states_list ]
then
    OLD_STATES=`cat .imported_states_list`
else
    OLD_STATES="not_imported"
fi

if [[ "${OLD_STATES}" != "${STATES}" ]]
then
    rm -f tracts.zip bgs.zip
fi

# Convert counties data from iso-8859-1 to utf-8
if [ ! -f counties.zip ]
then
    gv=`ogr2ogr --version | cut -d. -f1-2`
    if [ "$gv" != "GDAL 1.11" -a "$gv" != "GDAL 1.9" ]
    then
        echo "GDAL must be at least 1.9 to convert the counties file."
        echo "Run fetch_data.sh from a more modern system."
        exit 1
    fi
    dir=`mktemp -d 2>/dev/null || mktemp -d -t 'shape'`
    unzip tl_2013_us_county.zip -d $dir
    cd $dir
    ogr2ogr --DEBUG ON counties.shp tl_2013_us_county.shp -lco ENCODING=UTF8
    zip counties.zip counties.dbf counties.prj counties.shp counties.shx
    cd -
    mv $dir/counties.zip .
    rm $dir/*
    rmdir $dir
fi

# Combine tract shapefiles
if [ ! -f tracts.zip ]
then
    dir=`mktemp -d 2>/dev/null || mktemp -d -t 'shape'`
    for state in $STATES
    do
        unzip tl_2013_${state}_tract.zip -d $dir
    done
    cd $dir
    for state in $STATES
    do
        if [ ! -e tracts.shp ]
        then
            # First pass
            ogr2ogr --DEBUG ON tracts.shp tl_2013_${state}_tract.shp -lco ENCODING=UTF8
        else
            # Append passes
            ogr2ogr --DEBUG ON -update -append tracts.shp tl_2013_${state}_tract.shp -lco ENCODING=UTF8 -nln tracts
        fi
    done
    zip tracts.zip tracts.dbf tracts.prj tracts.shp tracts.shx
    cd -
    mv $dir/tracts.zip .
    rm $dir/*
    rmdir $dir
fi

# Combine block group shapefiles
if [ ! -f bgs.zip ]
then
    dir=`mktemp -d 2>/dev/null || mktemp -d -t 'shape'`
    for state in $STATES
    do
        unzip tl_2013_${state}_bg.zip -d $dir
    done
    cd $dir
    for state in $STATES
    do
        if [ ! -e bgs.shp ]
        then
            # First pass
            ogr2ogr --DEBUG ON bgs.shp tl_2013_${state}_bg.shp -lco ENCODING=UTF8
        else
            # Append passes
            ogr2ogr --DEBUG ON -update -append bgs.shp tl_2013_${state}_bg.shp -lco ENCODING=UTF8 -nln bgs
        fi
    done
    zip bgs.zip bgs.dbf bgs.prj bgs.shp bgs.shx
    cd -
    mv $dir/bgs.zip .
    rm $dir/*
    rmdir $dir
fi

echo "$STATES" > .imported_states_list

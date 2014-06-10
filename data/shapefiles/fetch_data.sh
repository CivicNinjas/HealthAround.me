#!/bin/sh

# Fetch files if they aren't already downloaded
wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/COUNTY/tl_2013_us_county.zip
wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/STATE/tl_2013_us_state.zip
wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/STATE/tl_2013_us_state.zip
wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/TRACT/tl_2013_40_tract.zip  # Oklahoma
wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/TRACT/tl_2013_42_tract.zip  # Pennsylvania
wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/BG/tl_2013_40_bg.zip  # Oklahoma
wget -N ftp://ftp2.census.gov/geo/tiger/TIGER2013/BG/tl_2013_42_bg.zip  # Pennsylvania

# Convert counties data from iso-8859-1 to utf-8
if [ ! -f counties.zip ]
then
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
    unzip tl_2013_40_tract.zip -d $dir
    unzip tl_2013_42_tract.zip -d $dir
    cd $dir
    ogr2ogr --DEBUG ON tracts.shp tl_2013_40_tract.shp -lco ENCODING=UTF8
    ogr2ogr --DEBUG ON -update -append tracts.shp tl_2013_42_tract.shp -lco ENCODING=UTF8 -nln tracts
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
    unzip tl_2013_40_bg.zip -d $dir
    unzip tl_2013_42_bg.zip -d $dir
    cd $dir
    ogr2ogr --DEBUG ON bgs.shp tl_2013_40_bg.shp -lco ENCODING=UTF8
    ogr2ogr --DEBUG ON -update -append bgs.shp tl_2013_42_bg.shp -lco ENCODING=UTF8 -nln bgs
    zip bgs.zip bgs.dbf bgs.prj bgs.shp bgs.shx
    cd -
    mv $dir/bgs.zip .
    rm $dir/*
    rmdir $dir
fi

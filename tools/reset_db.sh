#!/bin/bash
set -e  # Exit on errors
set -v  # Print shell input lines
# Change to project root
MY_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $MY_DIR/..

./manage.py reset_db --noinput
echo "CREATE EXTENSION IF NOT EXISTS postgis; CREATE EXTENSION IF NOT EXISTS postgis_topology; \q" | ./manage.py dbshell
./manage.py syncdb --noinput
./manage.py migrate
cd data/shapefiles
./fetch_data.sh
cd -
./manage.py loadshapefiles
./manage.py loaddata scores
./manage.py import_census_data
./manage.py import_dartmouth_data
./manage.py import_ers_data
echo "Done.  You may want to run ./manage.py createsuperuser"

#!/bin/sh
set -e  # Exit on errors
set -v  # Print shell input lines
# Change to project root
MY_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $MY_DIR/..

./manage.py reset_db --noinput
echo "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology; \q" | ./manage.py dbshell
./manage.py syncdb --noinput
./manage.py migrate
cd data/shapefiles
./fetch_data.sh
cd -
./manage.py loadshapefiles
./manage.py import_census_data
./manage.py loaddata scores
echo "Done.  You may want to run ./manage.py createsuperuser"

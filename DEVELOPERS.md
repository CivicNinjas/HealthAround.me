Getting Started
===============

Here's how to get started on an Ubuntu 12.04 machine.

Install PostgreSQL 9.3 / PostGIS 2.1
------------------------------------
Ubuntu 12.04 uses PostgreSQL 9.1 and PostGis 1.x.  To get the latest, we need
to add the
[PostgreSQL Global Development Group's APT repo](https://wiki.postgresql.org/wiki/Apt).

1. Get your release's code name with `lsb_release -c`.  These instructions
   are for 12.04, codename "precise".
2. Create `/etc/apt/sources.list.d/pgdg.list` with the content:

        dev http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main

3. Install the PostgreSQL server and PostGIS:

        sudo apt-get install postgresql-9.3-postgis-2.1 postgresql-server-dev-9.3

4. Install a healtharoundme user and database

        createuser healtharoundme -s -d -P  # Create healtharoundme user
        createdb healtharoundme -O healtharoundme  # Create healtharoundme database

5. Install PostGIS extensions

        psql -U healtharoundme
        CREATE EXTENSION postgis;
        CREATE EXTENSION postgis_topology;

6. Optionally,
   [tune your PostgreSQL settings](https://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server).
   `shared_buffers` will have the biggest impact.


Install Python Dev Tools
------------------------

1. Install Python headers for linked to C libraries:

        sudo apt-get install python-pip python-dev

2. Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org)

        sudo pip install virtualenvwrapper

3. Add something similar to this to `~/.bashrc`:

       export WORKON_HOME=$HOME/.virtualenvs
       export PROJECT_HOME=$HOME/Devel
       source /usr/local/bin/virtualenvwrapper.sh

4. Update your environment:

       source ~/.bashrc


Install the HealthAround.me project
-----------------------------------
1. Fork the project, and clone it locally

       cd ~/src
       git clone git@github.com:me/HealthAround.me healtharoundme
       cd healtharoundme

2. Create a [virtualenv](http://virtualenvwrapper.readthedocs.org/en/latest/)

       mkvirtualenv healtharound.me

3. Install the base and dev requirements

        pip install -r requirements.txt
        pip install -r requirements-dev.txt

4. Customize settings:

        cp settings_override.example.py settings_override.py
        vim settings_override.py # Fill DATABASES with your selected settings

5. Setup database

        ./manage.py syncdb
        ./manage.py migrate

6. Test that things are working.  Each of these should run without errors.
   Maybe some warnings, but no errors.

        ./manage.py dbshell     # \q to exit
        ./manage.py shell       # Ctrl-D to exit
        ./manage.py runserver   # Ctrl-C to exit


Install Data
------------

1. Go to the download site:
   <https://www.census.gov/geo/maps-data/data/tiger-line.html>
2. Download each of these 2013 boundaries:
   - Counties and equivalent (`tl_2013_us_county.zip`)
   - States and equivalent (`tl_2013_us_state.zip`)
   - Block groups (`tl_2013_40_bg.zip`)
   - Census tracts (`tl_2013_40_tract.zip`)
3. Load the counties data into [QGIS](http://www.qgis.org), and re-export in
   UTF-8 encoding as `counties.zip`
4. Run the shapefile import script (takes about 10 minutes)

        ./manage.py loadshapefiles

5. Run the census import script (takes about 60 minutes)

        ./manage.py import_census_data

6. Import the initial score tree (takes seconds)

        ./manage.py loaddata scores

Run it!
-------
1. `./manage.py runserver`, and go to <http://localhost:8000/>


TODO
====
- Update local_settings.example.py with better database defaults (host, post, u+p)
- Create .keep in /data/census/cache/.keep

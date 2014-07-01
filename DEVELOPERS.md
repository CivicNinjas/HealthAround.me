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

        createuser django -s -d -P  # Create healtharoundme user
        createdb healtharoundme -O django  # Create healtharoundme database


5. Install PostGIS extensions

        psql -U django -d healtharoundme
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
        vim settings_override.py
        # Fill DATABASES with your selected settings
        # If you are using the healtharound.me database dump, your
        # database user must be "django"

5. Customize virtualenv for tests:

        cdvirtualenv
        vim bin/postactivate
        # Add the line, customizing as needed:
        export DATABASE_URL="postgis://username:p@ssw0rd@127.0.0.1:5432/healthgeist
        source bin/postactivate

Install Data From HealthAround.me
---------------------------------
You have two choices for loading data - install from a healtharound.me
database dump, or load from 3rd party sources.  These are the
instructions for the first method.  It takes about 30 minutes.


1. Check postgis version on the healtharound.me server:

        sudo -u postgres psql -d healtharoundme -c "SELECT PostGIS_full_version();"
        # Response is something like:
        POSTGIS="2.1.3 r12547" GEOS="3.3.3-CAPI-1.7.4" PROJ="Rel. 4.7.1, 23 September 2009" GDAL="GDAL 1.9.0, released 2011/12/29" LIBXML="2.7.8" LIBJSON="UNKNOWN" TOPOLOGY RASTER

1. Create a database dump.  On the healtharound.me server:

        sudo -u postgres pg_dump -Fc healtharoundme > ~/ham.dump

2. Transfer the dump to your machine:

        scp healtharound.me:ham.dump .

3. Check that you are on the same minor version as the server (For example, 2.1.4 is compatible with 2.1.3)

        sudo -u postgres psql -d healtharoundme -c "SELECT PostGIS_full_version();"

4. Load the database dump

        pg_restore -h localhost -U django -d healtharoundme ham.dump

5. If you don't have a admin user on the server:

        ./manage.py createsuperuser


Install Data From External Sources
----------------------------------
You have two choices for loading data - install from a healtharound.me
database dump, or load from 3rd party sources.  These are the
instructions for the second method.  It takes about 2 hours.

1. Download and import the data:

        tools/reset_db.sh

2. Setup your superuser account

        ./manage.py createsuperuser


Run it!
-------
1. `./manage.py runserver`, and go to <http://localhost:8000/>

Create scores.json
==================
After updating ScoreNodes or ScoreMetrics, you should add the changes to
version control.

        ./manage.py dumpdata --indent 2 healthdata.ScoreMetric healthdata.ScoreNode | sed 's/[ \t]*$//' > healthdata/fixtures/scores.json

This will dump the ScoreMetric and ScoreNode rows to indented JSON, remove
trailing whitespace, and store them in scores.json.  Check in your changes.
When integrate, pull changes to server, and load with:

        ./manage.py loaddata scores


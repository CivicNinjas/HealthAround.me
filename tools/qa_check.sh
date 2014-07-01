#!/bin/bash
#!/bin/bash
MY_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $MY_DIR/..
./manage.py test -sx --ipdb --ipdb-failures --with-coverage $*
if [[ $? -ne 0 ]]; then exit 1; fi
flake8 .
coverage html
python -m webbrowser -t "file://${MY_DIR}/../htmlcov/index.html"

# Viewkids

## Description

Application for registration of children ages 0 to 18 +

## Implementation

Backend - Python 3, Djangо 1.9

## How to start

Clone project

    git clone https://github.com/mitrofun/kids2.git

Create `virtualenv` and install dependencies:
    
    cd kids2
    virtualenv --python=python3 env
    source env/bin/activate
    pip install -r requirements/dev.txt

Create user settings
    
    cp src/settings/local.py.skeleton src/settings/local.py

Init database and install some fixtures:

    python manage.py migrate
    python manage.py filldicts --fill
    python manage.py sitetree_resync_apps

Create super user
    
    python manage.py createsuper
    
## Deploy with fabric

Copy settings for fabric script deploy
    
    cp ./settings.py.skeleton ./settings.py
    
Enter your parameters in the file `./settings.py` and just run script 
    
    fab deploy


#### Command transfer children

Add to cron

    crontab -e

    0 0 1 9 * /.env/name/bin/python /projects/kids2/manage.py transfer_children

### Doc

pip install -r requirements/doc

cd docs && make html

For develop

    ln -s ~/projects/kids2/docs/build/html/ ~/projects/kids2/src/static/html

For production:

    ln -s ~/projects/kids2/docs/build/html/ ~/projects/kids2/public/static/html


P.S. The README file is written much later than the application, there may be errors. 
If there are questions [write on my mail](mailto:mitri4@bk.ru).

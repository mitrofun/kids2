# Viewkids

## Description

Application for registration of children ages 0 to 18 +

## Implementation

Backend - Python 3, Djangо 1.9

#### Command transfer children

Add to cron

    crontab -e

    0 0 1 9 * /.env/name/bin/python /projects/kids2/manage.py transfer_children

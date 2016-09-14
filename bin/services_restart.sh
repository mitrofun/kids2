#!/usr/bin/env bash
sudo supervisorctl update
sudo killall gunicorn
sudo nginx -s reload
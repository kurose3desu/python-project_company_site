#!/usr/bin/env bash
# exit on error
sudo chmod +x file.sh
set -o errexit


pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser

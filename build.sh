#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
apt install postgresql
systemctl enable postgresql
systemctl start postgresql
netstat -ltpn
ls

python manage.py collectstatic --no-input
python manage.py migrate
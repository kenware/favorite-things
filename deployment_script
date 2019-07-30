#!/bin/bash

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
cd client
npm install
npm run server
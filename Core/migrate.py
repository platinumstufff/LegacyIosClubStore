import os
import sys

os.chdir(sys.path[0])
# Make migrations
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')

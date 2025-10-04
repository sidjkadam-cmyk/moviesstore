# PythonAnywhere WSGI Configuration File
# Replace the contents of your /var/www/sidjkadam01_pythonanywhere_com_wsgi.py file with this

import os
import sys

# Add your project directory to the Python path
path = '/home/sidjkadam01/Django-5-for-the-Impatient-Second-Edition/moviesstore'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesstore.settings_production')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

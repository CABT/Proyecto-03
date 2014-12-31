import os
import sys

path='/srv/http/sangobemoledor.com'

if path not in sys.path:
sys.path.append(path)

os.environ['DJANGO_SETINGS_MODULE'] = 'sangobemodelor.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
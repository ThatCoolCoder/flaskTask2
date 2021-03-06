# http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/#creating-a-wsgi-file
# http://www.enigmeta.com/2012/08/16/starting-flask/

# for Py3:
# http://askubuntu.com/questions/488529/pyvenv-3-4-error-returned-non-zero-exit-status-1

import os, sys

PROJECT_DIR = '/var/www/flaskTask2'
sys.path.insert(0, PROJECT_DIR)


def execfile(filename):
    globals = dict( __file__ = filename )
    exec( open(filename).read(), globals )

activate_this = os.path.join( PROJECT_DIR, 'flaskTask2/flaskTask2Venv/bin', 'activate_this.py' )
#execfile( activate_this )


from flaskTask2 import app as application
application.debug = True

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'SECRET_KEY_FOR_SESSION_SIGNING'

# Define the path of our database inside the root application, where 'app.db' is the database's name
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTION = {}

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'SOMETHING_IMPOSSIBLE_TO_GUEES'
import os

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgres://localhost:5432/pokemon")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get("SECRET_KEY", 'it430iowf9hu24noerijpsslld')

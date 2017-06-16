import os


DEBUG = True

# database config

DB_HOST = os.getenv('DB_HOST', 'host')
DB_NAME = os.getenv('DB_NAME', 'name')
DB_USERNAME = os.getenv('DB_USERNAME', 'username')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

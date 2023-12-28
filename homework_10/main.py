from app import main
from database import database
import os

if not os.path.exists('sql_app.db'):
    database.create_new()

app = main.app

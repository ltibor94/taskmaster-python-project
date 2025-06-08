# Database initializer script
from app import app
from config import db

with app.app_context():
    created = db.create_all()
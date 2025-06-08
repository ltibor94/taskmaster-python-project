from app import app, db

with app.app_context():
    created = db.create_all()
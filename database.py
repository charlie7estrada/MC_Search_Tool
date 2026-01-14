# database initialization
from models import db, Client, Member
from pathlib import Path

def init_db(app):
    db.init_app(app)

    with app.app_context():
        data_dir = Path(app.root_path) / 'data'
        data_dir.mkdir(exist_ok=True)

        db.create_all()

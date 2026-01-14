# configuration settings
import os
from pathlib import Path

# base directory of the project
BASE_DIR = Path(__file__).parent

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{BASE_DIR / "data" / "members.db"}'
    
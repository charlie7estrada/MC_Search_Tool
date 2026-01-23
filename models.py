# SQLAlchemy models
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    __tablename__ = 'members'
    
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    ssn = db.Column(db.String(11), nullable=True)  # Optional, format: XXX-XX-XXXX
    
    # Foreign key to clients
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    
    
class Client(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    dashboard_url = db.Column(db.String(255), nullable=False)
    
    # Relationship: one client has many members
    members = db.relationship('Member', backref='client', lazy=True)
    

# main flask app
from flask import Flask, render_template, request, jsonify
from database import init_db
from models import db, Member, Client
import os

app = Flask(__name__, instance_relative_config=True)
# Build absolute path to database
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'members.db')
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

init_db(app)

@app.route('/')
def index():
    """Home page with search form"""
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    """Search endpoint - handles member lookups"""
    # Get search parameters from form
    first_name = request.args.get('first_name', '').strip()
    last_name = request.args.get('last_name', '').strip()
    dob = request.args.get('dob', '').strip()
    
    # Build query
    query = Member.query
    
    # Filter by first name (case-insensitive, partial match)
    if first_name:
        query = query.filter(Member.first_name.ilike(f'%{first_name}%'))
    
    # Filter by last name (case-insensitive, partial match)
    if last_name:
        query = query.filter(Member.last_name.ilike(f'%{last_name}%'))
    
    # Filter by DOB (exact match)
    if dob:
        from datetime import datetime
        try:
            dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
            query = query.filter(Member.dob == dob_date)
        except ValueError:
            pass  # Invalid date format, ignore
    
    # Execute query
    results = query.all()
    
    return render_template('index.html', 
        results=results,
        first_name=first_name,
        last_name=last_name,
        dob=dob
    )


if __name__ == '__main__':
    app.run(debug=True)
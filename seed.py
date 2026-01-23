# populating db with example data
from app import app
from models import db, Client, Member
from datetime import date

with app.app_context():
    # Clear existing data
    Member.query.delete()
    Client.query.delete()
    
    # Create clients
    client1 = Client(name='ABCD', dashboard_url='abcd-dashboard.healthcare.com')
    client2 = Client(name='XXYY', dashboard_url='xxyy-dashboard.healthcare.com')
    db.session.add_all([client1, client2])
    db.session.commit()
    
    # Create members
    members = [
        Member(member_id='ABCD100001', first_name='John', last_name='Smith', dob=date(1985, 3, 15), client_id=client1.id),
        Member(member_id='ABCD100002', first_name='Jane', last_name='Doe', dob=date(1990, 7, 22), client_id=client1.id),
        Member(member_id='ABCD100003', first_name='Michael', last_name='Johnson', dob=date(1978, 11, 8), client_id=client1.id),
        Member(member_id='XXYY200001', first_name='Sarah', last_name='Williams', dob=date(1995, 1, 30), client_id=client2.id),
        Member(member_id='XXYY200002', first_name='Robert', last_name='Brown', dob=date(1982, 6, 12), client_id=client2.id),
    ]
    
    db.session.add_all(members)
    db.session.commit()

# MC Search Tool

An internal search tool for looking up healthcare members across multiple clients.

## Overview

In healthcare claims management, customer service teams often manage members across multiple client organizations. Each client has their own dashboard, making it cumbersome to locate which client a member belongs to. This tool provides a centralized search interface to quickly find members and access their client's dashboard.

## Screenshot

<img width="1047" height="847" alt="mc_search_image" src="https://github.com/user-attachments/assets/4693d4be-4fd3-48df-b909-509a23d00c54" />



## Features

- Search members by first name, last name, or date of birth
- Partial and case-insensitive name matching
- Direct links to client dashboards
- Single-page interface with results displayed below search form

## Tech Stack

- Python / Flask
- SQLAlchemy ORM
- SQLite database
- HTML / CSS

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python app.py`
6. Open http://127.0.0.1:5000 in your browser

## Database Schema

**Members:** member_id, first_name, last_name, dob, client_id

**Clients:** name, dashboard_url

One-to-many relationship: each client has multiple members.

## Future Enhancements

- User authentication
- Excel import for bulk member data
- Search by member ID
- Audit logging

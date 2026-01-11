# Daily User Log Tracker

This project is a **FastAPI-based backend system written in Python** designed to track users’ daily activity logs. Users can log into the system daily and record their tasks or activities. 

## Project Structure

All the backend code is organized under the `/app` folder:

/app

├── main.py # Entry point of the FastAPI app

├── router/ # All route definitions (user, auth, etc.)

├── services/ # Business logic and service layer

├── models/ # SQLAlchemy models for database

├── database/ # Database initialization and connection

├── utils/ # Helper functions (password, JWT, etc.)

├── dto/ # Data Transfer Objects for responses and requests

└── config/ # Configuration settings


## Getting Started

1. **Set up your database**  
   Make sure to configure your MySQL settings properly in the `.env` file.  

2. **Install dependencies**  
   pip install -r requirements.txt

3. **Run the project**
   uvicorn app.main:app --reload

4. **Access the API**
   By default API should be running at
   http://127.0.0.1:8000



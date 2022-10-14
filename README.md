# Profiles-app

# Requirements
- Python 3.10.8
- Windows 10 (In Linux deployment commands change a bit)

# Deployment

- git clone repo url
in powershell get inside the folder where the repo was cloned and execute the following commands:
- python -m venv .venv
- .env/Scripts/Activate.ps1
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- In the browser enter to http://127.0.0.1:8000/

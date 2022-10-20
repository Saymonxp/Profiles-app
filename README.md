# Profiles-app

## Requirements
- Python 3.10.8
- Windows 10 (In Linux deployment commands change a bit)

## Deployment

- Download the repository .zip in https://github.com/Saymonxp/Profiles-app/archive/refs/heads/master.zip
- Extract the folder and copy the route of the extracted folder
- Open Command Prompt and execute ```cd route_you_just_copied```
- Execute ```python -m venv .env```. If it fails check if you have Python installed.
- Execute the following commands, in order (```pip install``` may take some time):

```.env\Scripts\activate.bat```

```pip install -r requirements.txt```

```python manage.py migrate```

```python manage.py makemigrations```

```python manage.py runserver```

- In the browser enter to http://127.0.0.1:8000/. There you have the site 😀.

## How to use the app

The main functionality is in _Profile list_ page. There you can check the profile of the registered employees.

Profile pictures functionality is implemented using Gravatar. So each employee has to be registered with their email in the username field.

### Create, edit or delete employees

- Log in with admin credentials:

Username:
```admin```

Password:
```factoredbestai```

- Enter to Admin page

- In Employees section you have the options to create, edit and delete employees.

This functionality would be integrated with the main Sign up interface in future releases.

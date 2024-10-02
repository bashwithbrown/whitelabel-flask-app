# Whitelabel Flask App

## Overview

The **Whitelabel Flask App** is a simple application built using Flask. It supports user authentication and file uploads. The app utilizes Flask-Login for user management, SQLAlchemy for database operations, and Jinja2 for templating.

## Features

- **User Authentication:** Sign up, log in, and manage user profiles.
- **User Management:** Update user information and profile pictures.

## Requirements

- Python 3.11
- Flask
- Flask-Login
- SQLAlchemy
- Gunicorn (for production)

## Installation

### Setting Up the Environment

1. **Clone the repository:**

   ```bash
   git clone git@github.com:bashwithbrown/whitwlabel-flask-app.git
   cd chat-app
   ```

2. **Run the setup script in scripts directory to create a virtual environment and install dependencies:**

   ```bash
   ./scripts/setup-venv.sh
   ```

3. **Create your own secrect key using uuid in python for your .env file:**

   ```python
   uuid.uuid4()
   ```

### Configuration

Update the `config.py` file with your database and application settings. The code will run out of the box on default settings.

## Running the Application

### Development

1. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate
   ```

2. **Run the Flask development server:**

   ```bash
   flask run
   ```

### Production

1. **Activate the virtual environment:**

   ```bash
   source venv/bin/activate
   ```

2. **Run the Gunicorn server:**

   ```bash
   ./scripts/run.sh
   ```

   **For background execution:**

   ```bash
   ./scripts/run.sh -d
   ```

## Project Structure

```
.
├── README.md
└── website
    ├── app.py
    ├── core
    │   ├── config.py
    │   └── __init__.py
    ├── database
    │   ├── db_manager.py
    │   ├── __init__.py
    │   ├── logs
    │   │   ├── database.log
    │   │   └── service.log
    │   └── models
    │       ├── __init__.py
    │       └── sqlalchemy_models.py
    ├── functions
    │   ├── __init__.py
    │   ├── logger
    │   │   ├── __init__.py
    │   │   └── logger.py
    │   └── tools
    │       ├── __init__.py
    │       └── utilites.py
    ├── requirements.txt
    ├── routes
    │   ├── admin.py
    │   ├── api.py
    │   ├── auth.py
    │   ├── __init__.py
    │   ├── main.py
    │   └── user.py
    ├── static
    │   ├── css
    │   │   └── styles.css
    │   ├── file_upload
    │   ├── ico
    │   ├── images
    │   └── js
    │       └── script.js
    ├── templates
    │   ├── 404.html
    │   ├── admin
    │   │   ├── admin.html
    │   │   └── settings.html
    │   ├── auth
    │   │   ├── login.html
    │   │   ├── reset-password.html
    │   │   └── signup.html
    │   ├── base.html
    │   ├── main
    │   │   └── home.html
    │   ├── navbar.html
    │   └── user
    │       └── profile.html
    └── wsgi.py
```

- **`website/static/`**: Static files (CSS, JavaScript, images).
- **`website/templates/`**: HTML templates.
- **`website/routes/api.py`**: API endpoints.
- **`website/config.py`**: Configuration settings.
- **`website/database/db_manager.py`**: Database models and manager.
- **`website/functions`**: Utility functions.
- **`website/wsgi.py`**: WSGI entry point for Gunicorn.
- **`scripts/setup-venv.sh`**: Script to set up the environment.
- **`scripts/run.sh`**: Script to run the application.
- **`requirements.txt`**: Python dependencies.

## Routes

### API

- **`POST /alter-user-information/<user_id>`**: Updates user information.
- **`POST /alter-user-profile-picture/<user_id>`**: Updates user profile picture.
- **`POST /login-user`**: Logs in a user.
- **`POST /signup-user`**: Signs up a new user.
- **`POST /alter-user-password/<user_id>`**: Changes user password.
- **`POST /delete-file/<file_name>`**: Deletes a file from the server.

## Usage

1. **Sign Up**: Create a new account.
2. **Log In**: Log into your account.
5. **Manage Profile**: Update your user information and profile picture.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License.

---

## Scripts Explanation

### setup.sh

This script sets up the project environment by creating a virtual environment, installing required packages, and configuring the project for development.

```bash
#!/bin/bash

cd ..

python3.11 -m venv venv
source venv/bin/activate
python -m pip install -U pip

cd website

python -m pip install -r requirements.txt
```

### run.sh

This script runs the application using Gunicorn. It can start the server either in the foreground or as a background process.

```bash
#!/bin/bash

cd ..
source venv/bin/activate
export FLASK_APP=website
export FLASK_DEBUG=1
cd website

if [[ "$#" -eq 0 ]]; then
    gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
elif [[ "$1" == "-d" ]]; then
    gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app &
else
    echo "Invalid option: $1"
    echo "Usage: ./run.sh [-d]"
fi
```

By following this README, you should be able to set up, configure, and run the Whitelabel Flask App both in development and production environments. For any issues or further assistance, feel free to contact the project maintainers.


## Credits

Created By: Tre Brown  
LinkedIn: [www.linkedin.com/in/trebrown100](https://www.linkedin.com/in/trebrown100)  
Contact: [trebrown2238@gmail.com](mailto:trebrown2238@gmail.com)

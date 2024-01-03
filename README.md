# Flask Blog Application

This is a simple Flask blog application that allows users to register, log in, create, edit, and delete posts, and reset their passwords. The application uses Flask, Flask-SQLAlchemy for database management, Flask-Bcrypt for password hashing, Flask-Login for user authentication, and Flask-Mail for sending email notifications.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sawanjr/flask-blog.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-blog
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Directory Structure

The project directory is organized as follows:

```plaintext
flaskblog/
|-- __pycache__/
|-- static/
|   |-- profile_pics/
|   |-- main.css
|-- templates/
|   |-- about.html
|   |-- account.html
|   |-- create_post.html
|   |-- home.html
|   |-- layout.html
|   |-- login.html
|   |-- post.html
|   |-- register.html
|   |-- reset_request.html
|   |-- reset_token.html
|   |-- user_posts.html
|-- __init__.py
|-- forms.py
|-- models.py
|-- routes.py
instance/
|-- site.db
.gitignore
LICENSE
README.md
requirements.txt
run.py
```

### Dependencies

- Flask
- Flask-Bcrypt
- Flask-Login
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Mail
- Pillow

### Configuration

The application uses a SQLite database, and the configuration can be found in the `config.py` file. The database file is located in the `instance` folder.

```python
# config.py

SECRET_KEY = 'your_secret_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/site.db'
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
```

### Running the Application

Run the application using the `run.py` script:

```bash
python run.py
```

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser to access the application.

## Features

- User registration and authentication
- Password hashing with Flask-Bcrypt
- User profile with profile picture upload
- Create, edit, and delete blog posts
- Email notifications for password reset

## Contributing

Feel free to contribute to this project by opening issues or creating pull requests. Your feedback and contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

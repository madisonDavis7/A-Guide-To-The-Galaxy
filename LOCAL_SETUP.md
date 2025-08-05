# Guide to the Galaxy - Local Development Setup

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

1. **Clone or download the project**
   ```
   cd "guide to the galaxy"
   ```

2. **Create a virtual environment (recommended)**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

5. **Set up the database**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```
   python manage.py runserver
   ```

8. **Access the application**
   Open your browser and go to: http://127.0.0.1:8000

## Features
- Stellar object catalog with image slideshow
- Planetary tours with markdown content
- User authentication and profiles
- Star ratings system
- NASA APOD integration

## Notes
- The application uses SQLite database for local development
- Static files are served locally
- Email verification is enabled for user registration
- GitHub OAuth is configured but requires proper credentials in `secrets.yml`

## Troubleshooting
- If you encounter migration issues, delete the `db.sqlite3` file and run migrations again
- Make sure all dependencies are installed with `pip install -r requirements.txt`
- Check that Python virtual environment is activated

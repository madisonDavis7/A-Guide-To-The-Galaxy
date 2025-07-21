# Django Deployment Guide

## Current Deployment: Google Cloud Platform

**✅ Currently Deployed**: Google Cloud Run with Cloud SQL PostgreSQL
**Live URL**: https://guide-to-galaxy-1019331146280.us-central1.run.app
**Admin Panel**: https://guide-to-galaxy-1019331146280.us-central1.run.app/admin/

## Google Cloud Platform Architecture

Your app is currently running on:
- **Google Cloud Run**: Containerized Django application hosting
- **Google Cloud SQL**: PostgreSQL database
- **Docker**: Container-based deployment
- **WhiteNoise**: Static file serving

### Admin Access
- Username: `admin`
- Password: `admin123`

## Alternative Deployment Options

**✅ Heroku**: Traditional choice with good Django support
**✅ DigitalOcean App Platform**: Great balance of features and cost
**✅ Vercel**: Good for simple Django apps

## Heroku Deployment (Alternative)

Traditional platform with excellent Django support.

### Steps:
1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Add PostgreSQL: `heroku addons:create heroku-postgresql:mini`
4. Deploy: `git push heroku main`

## Next Steps for Current Google Cloud Deployment

1. **Monitor your app** in Google Cloud Console
2. **Scale resources** if needed (CPU/Memory)
3. **Set up custom domain** (optional)
4. **Configure automated backups** for Cloud SQL
5. **Monitor logs** via Cloud Logging

## Google Cloud Platform Management

### Useful Commands:
```bash
# Check deployment status
gcloud run services describe guide-to-galaxy --region us-central1

# View logs
gcloud logging read "resource.type=cloud_run_revision" --limit=50

# Update service
gcloud run deploy guide-to-galaxy --image gcr.io/guide-to-galaxy-app-2025/guide-to-galaxy
```

## Using Firebase Services with Django

If you want to use Firebase services (Auth, Firestore, Storage) with your Django app:

### Install Firebase Admin SDK:
```bash
pip install firebase-admin
```

### Configure in settings.py:
```python
import firebase_admin
from firebase_admin import credentials

# Initialize Firebase Admin
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": env.str('FIREBASE_PROJECT_ID'),
    "private_key": env.str('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": env.str('FIREBASE_CLIENT_EMAIL'),
})
firebase_admin.initialize_app(cred)
```

## Using Firebase Services with Django

If you want to use Firebase services (Auth, Firestore, Storage) with your Django app:

### Install Firebase Admin SDK:
```bash
pip install firebase-admin
```

### Configure in settings.py:
```python
import firebase_admin
from firebase_admin import credentials

# Initialize Firebase Admin
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": env.str('FIREBASE_PROJECT_ID'),
    "private_key": env.str('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": env.str('FIREBASE_CLIENT_EMAIL'),
})
firebase_admin.initialize_app(cred)
```

## Database Migration for Production

When moving from SQLite to PostgreSQL:
1. Export your data: `python manage.py dumpdata > data.json`
2. Set up PostgreSQL database
3. Run migrations: `python manage.py migrate`
4. Import data: `python manage.py loaddata data.json`

## Current Project Status

✅ **Deployed on Google Cloud Platform**  
✅ **PostgreSQL database configured**  
✅ **Static files serving via WhiteNoise**  
✅ **HTTPS/SSL enabled**  
✅ **Django admin accessible**  
✅ **CSRF protection configured**  

Your Django astronomy app is successfully running and accessible to users worldwide!

If you want to use Firebase services alongside your Django deployment:
- Use Firebase for frontend features (realtime updates, push notifications)
- Keep Django for backend logic and admin interface
- Use Firebase Admin SDK to integrate services

This gives you the best of both worlds: robust Django backend with Firebase's frontend features.

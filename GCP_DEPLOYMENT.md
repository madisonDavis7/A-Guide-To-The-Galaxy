# Google Cloud Platform Deployment Guide

## 🚀 Deploy Your Django App to Google Cloud

**Yes! Google Cloud will let you:**
- ✅ Use Django admin to add/edit database content
- ✅ Show that data to users worldwide
- ✅ Have a persistent PostgreSQL database
- ✅ Scale automatically based on traffic

## Prerequisites

1. **Google Cloud Account** (Free tier includes $300 credit)
2. **Google Cloud CLI** installed
3. **Docker** installed (for building container)

## Step 1: Set Up Google Cloud Project

### Install Google Cloud CLI
Download from: https://cloud.google.com/sdk/docs/install

### Create Project and Enable APIs
```bash
# Login to Google Cloud
gcloud auth login

# Create a new project
gcloud projects create guide-to-galaxy-app --name="Guide to Galaxy"

# Set as active project
gcloud config set project guide-to-galaxy-app

# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable sql-component.googleapis.com
gcloud services enable sqladmin.googleapis.com
```

## Step 2: Create PostgreSQL Database

```bash
# Create Cloud SQL PostgreSQL instance
gcloud sql instances create guide-galaxy-db \
    --database-version=POSTGRES_15 \
    --tier=db-f1-micro \
    --region=us-central1 \
    --storage-type=SSD \
    --storage-size=10GB

# Create database
gcloud sql databases create guidegalaxy --instance=guide-galaxy-db

# Create database user
gcloud sql users create galaxyuser \
    --instance=guide-galaxy-db \
    --password=your-secure-password
```

## Step 3: Build and Deploy Container

### Build Docker Image
```bash
# Build the container
gcloud builds submit --tag gcr.io/guide-to-galaxy-app/guide-to-galaxy

# Or build locally and push
docker build -t gcr.io/guide-to-galaxy-app/guide-to-galaxy .
docker push gcr.io/guide-to-galaxy-app/guide-to-galaxy
```

## Step 4: Set Up Secrets

```bash
# Generate Django secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Store secrets in Google Secret Manager
gcloud secrets create django_secret_key --data-file=-
# (paste your secret key and press Ctrl+D)

# Create database URL secret
echo "postgresql://galaxyuser:your-secure-password@/guidegalaxy?host=/cloudsql/guide-to-galaxy-app:us-central1:guide-galaxy-db" | gcloud secrets create database_url --data-file=-
```

## Step 5: Deploy to Cloud Run

```bash
# Deploy the service
gcloud run deploy guide-to-galaxy \
    --image gcr.io/guide-to-galaxy-app/guide-to-galaxy \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --add-cloudsql-instances guide-to-galaxy-app:us-central1:guide-galaxy-db \
    --set-env-vars DEBUG=False \
    --set-secrets DATABASE_URL=database_url:latest \
    --set-secrets SECRET_KEY=django_secret_key:latest \
    --port 8080 \
    --memory 512Mi \
    --cpu 1
```

## Step 6: Run Database Migrations

```bash
# Get the service URL
gcloud run services describe guide-to-galaxy --region=us-central1 --format="value(status.url)"

# Run migrations (you'll need to do this via Cloud Run jobs or locally)
gcloud run jobs create migrate-db \
    --image gcr.io/guide-to-galaxy-app/guide-to-galaxy \
    --region us-central1 \
    --add-cloudsql-instances guide-to-galaxy-app:us-central1:guide-galaxy-db \
    --set-secrets DATABASE_URL=database_url:latest \
    --set-secrets SECRET_KEY=django_secret_key:latest \
    --command python \
    --args manage.py,migrate

# Execute the migration job
gcloud run jobs execute migrate-db --region=us-central1
```

## Step 7: Create Superuser

```bash
# Create superuser job
gcloud run jobs create create-superuser \
    --image gcr.io/guide-to-galaxy-app/guide-to-galaxy \
    --region us-central1 \
    --add-cloudsql-instances guide-to-galaxy-app:us-central1:guide-galaxy-db \
    --set-secrets DATABASE_URL=database_url:latest \
    --set-secrets SECRET_KEY=django_secret_key:latest \
    --command python \
    --args manage.py,createsuperuser,--noinput,--username=admin,--email=admin@example.com

# You'll need to set the password separately or modify this command
```

## Step 8: Access Your App

Your app will be available at: `https://guide-to-galaxy-[HASH]-uc.a.run.app`

- **Main app**: Your Cloud Run URL
- **Admin panel**: Your Cloud Run URL + `/admin/`

## 💰 Costs (Free Tier Friendly)

**Cloud Run**: 
- 2 million requests/month FREE
- 400,000 GB-seconds/month FREE
- After free tier: ~$0.40 per million requests

**Cloud SQL**:
- db-f1-micro (shared CPU, 614MB RAM): ~$7/month
- 30GB storage free, then ~$0.17/GB/month

**Total estimated cost**: $7-15/month for small to medium traffic

## 🎯 What You Can Do After Deployment

1. **Add content via Django admin** - All data persists in PostgreSQL
2. **Users see your content** - Anyone can visit your public URL
3. **Automatic scaling** - Handles traffic spikes automatically
4. **Custom domain** - Add your own domain name
5. **SSL/HTTPS** - Automatically provided by Google

## Benefits Over Other Platforms

✅ **No cold starts** (unlike serverless functions)
✅ **Full Django support** (admin, file uploads, etc.)
✅ **Persistent database** (PostgreSQL)
✅ **Automatic scaling** (0 to millions of users)
✅ **Google's reliability** (99.95% uptime SLA)
✅ **Easy CI/CD** integration

## Troubleshooting

**Build fails?**
- Check Dockerfile syntax
- Ensure all dependencies in requirements.txt

**Database connection fails?**
- Verify Cloud SQL instance is running
- Check database URL format
- Ensure Cloud SQL connector is properly configured

**Static files not loading?**
- Cloud Run automatically runs collectstatic
- Whitenoise serves static files

## Alternative: App Engine

If you prefer fully managed (no Docker):

```bash
# Create app.yaml
gcloud app deploy

# Simpler but less flexible than Cloud Run
```

This setup gives you a production-ready Django app that can handle real users and traffic!

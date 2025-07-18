#!/bin/bash

# Google Cloud Deployment Script
# Run this after setting up your GCP project and database

PROJECT_ID="guide-to-galaxy-app-2025"
REGION="us-central1"
SERVICE_NAME="guide-to-galaxy"

echo "🚀 Deploying Django app to Google Cloud Run..."

# Set project
gcloud config set project $PROJECT_ID

# Build and submit container
echo "📦 Building container..."
gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME

# Deploy to Cloud Run
echo "🌐 Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
    --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --add-cloudsql-instances $PROJECT_ID:$REGION:guide-galaxy-db \
    --set-env-vars DEBUG=False \
    --set-secrets DATABASE_URL=database_url:latest \
    --set-secrets SECRET_KEY=django_secret_key:latest \
    --port 8080 \
    --memory 512Mi \
    --cpu 1

# Get the service URL
SERVICE_URL=$(gcloud run services describe $SERVICE_NAME --region=$REGION --format="value(status.url)")

echo "✅ Deployment complete!"
echo "🌍 Your app is live at: $SERVICE_URL"
echo "🔧 Admin panel: $SERVICE_URL/admin/"
echo ""
echo "Next steps:"
echo "1. Run migrations: See GCP_DEPLOYMENT.md"
echo "2. Create superuser: See GCP_DEPLOYMENT.md"
echo "3. Add content via admin panel"

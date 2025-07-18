# Railway Deployment Guide

## Step 1: Push Your Code to GitHub

If you haven't already, push your project to GitHub:

```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

## Step 2: Create Railway Account

1. Go to **https://railway.app**
2. Click **"Start a New Project"**
3. Sign up with your **GitHub account** (recommended)

## Step 3: Create New Project

1. Click **"Deploy from GitHub repo"**
2. Select your **A-Guide-To-The-Galaxy** repository
3. Railway will automatically detect it's a Django project

## Step 4: Add PostgreSQL Database

1. In your Railway dashboard, click **"+ Add Service"**
2. Select **"Database"** → **"PostgreSQL"**
3. Railway will create a database and provide connection details automatically

## Step 5: Configure Environment Variables

In your Railway project dashboard, go to **Variables** tab and add:

```bash
SECRET_KEY=your-secret-django-key-here
DEBUG=False
PYTHONUNBUFFERED=1
```

**Important**: Railway automatically provides `DATABASE_URL`, so you don't need to set database variables manually.

## Step 6: Generate a Secret Key

Run this command locally to generate a secure secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and use it as your `SECRET_KEY` in Railway.

## Step 7: Deploy

1. Railway will automatically deploy when you push to GitHub
2. Wait for the build to complete (usually 2-3 minutes)
3. Railway will provide you with a public URL

## Step 8: Create Superuser (Admin Account)

Once deployed, you need to create an admin account:

1. In Railway dashboard, go to your **Django service**
2. Click **"Connect"** to open a terminal
3. Run: `python manage.py createsuperuser`
4. Follow the prompts to create your admin account

## Step 9: Access Your App

1. **Main App**: Use the Railway-provided URL (like `your-app.railway.app`)
2. **Admin Panel**: Add `/admin/` to your URL (like `your-app.railway.app/admin/`)
3. Log in with the superuser account you created

## Troubleshooting

### Build Fails?
- Check the **Logs** tab in Railway dashboard
- Common issues: missing dependencies or environment variables

### Database Issues?
- Make sure PostgreSQL service is running
- Railway automatically sets `DATABASE_URL`

### Static Files Not Loading?
- Railway automatically runs `collectstatic` via the Procfile
- Check your `STATIC_URL` and `STATIC_ROOT` settings

## Railway Features You Get For Free

✅ **Automatic HTTPS/SSL**  
✅ **Custom domains** (can add your own later)  
✅ **Auto-scaling**  
✅ **Automatic deploys** from GitHub  
✅ **PostgreSQL database**  
✅ **Environment variable management**  
✅ **Real-time logs**  

## Free Tier Limits

- **512MB RAM**
- **$5 usage credit per month** (usually covers small apps)
- **1GB storage**
- **100GB bandwidth**

Perfect for development and small production apps!

## Next Steps After Deployment

1. **Test all functionality** (admin, user registration, etc.)
2. **Add custom domain** (optional, in Railway dashboard)
3. **Set up monitoring** (Railway provides basic metrics)
4. **Configure backups** (Railway auto-backs up PostgreSQL)

## Railway vs Other Platforms

**Railway Advantages:**
- Easiest Django deployment
- Automatic PostgreSQL setup
- Great free tier
- No cold starts
- Simple pricing

**When to Consider Alternatives:**
- Need more than 512MB RAM → DigitalOcean App Platform
- Need advanced features → AWS/Google Cloud
- Budget is very tight → Render free tier

## Support

If you need help:
- Railway Discord: https://discord.gg/railway
- Railway Docs: https://docs.railway.app
- Check Railway dashboard logs for error details

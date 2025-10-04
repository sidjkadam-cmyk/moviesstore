# Django Movies Store - PythonAnywhere Deployment Guide

This guide will walk you through deploying your Django Movies Store project to PythonAnywhere.

## Prerequisites

1. A PythonAnywhere account (free tier available)
2. Your project code ready for deployment
3. Git repository (recommended) or ability to upload files

## Step 1: Prepare Your Project

### 1.1 Update Settings for Production

The project includes a `settings_production.py` file that's configured for PythonAnywhere. You'll need to:

1. Replace `yourusername` in `settings_production.py` with your actual PythonAnywhere username
2. Set a secure secret key (you can generate one at https://djangosecretkey.com/)

### 1.2 Clean Up Requirements

Use the `requirements_production.txt` file which contains only the essential packages:
- Django==5.0
- Pillow==10.4.0 (for image handling)
- asgiref==3.9.1
- sqlparse==0.5.3

## Step 2: Upload Your Project to PythonAnywhere

### Option A: Using Git (Recommended)

1. Push your code to GitHub/GitLab
2. In PythonAnywhere console, clone your repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

### Option B: Upload Files Directly

1. Create a zip file of your project
2. Upload it through the PythonAnywhere Files tab
3. Extract it in your home directory

## Step 3: Set Up Virtual Environment

1. Open a Bash console in PythonAnywhere
2. Navigate to your project directory:
   ```bash
   cd ~/your-project-directory
   ```
3. Create a virtual environment:
   ```bash
   python3.10 -m venv moviesstore_env
   ```
4. Activate the virtual environment:
   ```bash
   source moviesstore_env/bin/activate
   ```
5. Install requirements:
   ```bash
   pip install --upgrade pip
   pip install -r requirements_production.txt
   ```

## Step 4: Configure Database

1. Run migrations:
   ```bash
   python manage.py migrate --settings=moviesstore.settings_production
   ```
2. Create a superuser:
   ```bash
   python manage.py createsuperuser --settings=moviesstore.settings_production
   ```
3. Collect static files:
   ```bash
   python manage.py collectstatic --settings=moviesstore.settings_production
   ```

## Step 5: Configure Web App

1. Go to the **Web** tab in PythonAnywhere
2. Click **Add a new web app**
3. Choose **Manual Configuration**
4. Select **Python 3.10** (or the latest available)
5. Click **Next**

### 5.1 Configure WSGI File

1. Click on the WSGI configuration file link
2. Replace the contents with:

```python
import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/your-project-directory'  # Replace with your actual path
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'moviesstore.settings_production'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Important:** Replace `yourusername` and `your-project-directory` with your actual values.

### 5.2 Configure Static Files

1. In the **Web** tab, scroll down to **Static files**
2. Add a new mapping:
   - URL: `/static/`
   - Directory: `/home/yourusername/your-project-directory/staticfiles/`
3. Add another mapping for media files:
   - URL: `/media/`
   - Directory: `/home/yourusername/your-project-directory/media/`

## Step 6: Set Up Environment Variables (Optional but Recommended)

1. In the **Web** tab, scroll down to **Environment variables**
2. Add:
   - `SECRET_KEY`: Your secure Django secret key
   - `DEBUG`: `False`

## Step 7: Reload Your Web App

1. Click the **Reload** button in the Web tab
2. Your site should now be live at `yourusername.pythonanywhere.com`

## Step 8: Test Your Deployment

1. Visit your site URL
2. Test the main functionality:
   - Home page loads
   - Movie listings work
   - User registration/login works
   - Cart functionality works
   - Admin panel is accessible

## Troubleshooting

### Common Issues:

1. **Static files not loading:**
   - Ensure `collectstatic` was run
   - Check static file mappings in Web tab
   - Verify `STATIC_ROOT` path is correct

2. **Database errors:**
   - Ensure migrations were run
   - Check database file permissions

3. **Import errors:**
   - Verify virtual environment is activated
   - Check Python path in WSGI file
   - Ensure all dependencies are installed

4. **404 errors:**
   - Check `ALLOWED_HOSTS` in settings
   - Verify URL patterns are correct

### Debugging:

1. Check the error log in the Web tab
2. Use the console to run Django commands
3. Check the Django log file: `django.log` in your project directory

## Security Considerations

1. **Change the secret key** - Never use the default secret key in production
2. **Set DEBUG=False** - Always disable debug mode in production
3. **Use HTTPS** - Consider upgrading to a paid plan for HTTPS support
4. **Regular backups** - Backup your database regularly

## Updating Your Deployment

When you make changes to your code:

1. Upload/update your code
2. Activate virtual environment
3. Install any new requirements: `pip install -r requirements_production.txt`
4. Run migrations: `python manage.py migrate --settings=moviesstore.settings_production`
5. Collect static files: `python manage.py collectstatic --settings=moviesstore.settings_production`
6. Reload your web app

## Free Tier Limitations

- Limited CPU seconds per month
- No custom domains
- No HTTPS
- Limited file storage

Consider upgrading to a paid plan for production use.

## Support

- PythonAnywhere Help: https://help.pythonanywhere.com/
- Django Deployment: https://docs.djangoproject.com/en/5.0/howto/deployment/

# Deployment

## Table of Contents
---
### Setting up a basic Django project and deploying to Heroku 

* [**Deployment**](#deployment)
    * [***Initial Deployment***](#initial-deployment)
    * [***Create Repository***](#create-repository)
    * [***Setting up the Workspace***](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)
    * [***Deploying an app to Heroku***](#deploying-an-app-to-heroku)
        * [***Create a New External Database***](#create-a-new-external-database)
        * [***Create Heroku App***](#create-heroku-app)
        * [***Attach the Database***](#attach-the-database)
        * [***Preparing Environment and settings.py File***](#preparing-environment-and-settings.py-file)
        * [***Store Static and Media Files on Cloudinary***](#store-static-and-media-files-on-cloudinary)
        * [***Final Steps***](#final-steps)
* [***Cloning on a Local Machine or Via Gitpod Terminal***](#cloning-on-a-local-machine-or-via-gitpod-terminal)

## Initial Deployment

I took the following steps to deploy the site to Heroku and have listed any console commands required to initiate it. My aim was to ensure this process was completed as early as possible in the project, to avoid complications or issues as it progressed.

### Create repository:

* Create a new repository in GitHub and clone it locally following [these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    * **Note** - If you are cloning my project, then you can skip all pip installs below and just run the following command in the terminal to install all the required libraries/packages at once:
        * pip install -r requirements.txt
    * **IMPORTANT** - If developing locally on your device, ensure you set up/activate the virtual environment ([see below](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)) before installing/generating the requirements.txt file; failure to do this will pollute your machine and put other projects at risk


### Setting up the Workspace (To be done locally via the console of your chosen editor):
1. Create a virtual environment on your machine (Can be skipped if using gitpod):
    * python -m venv .venv
1. To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
1. Install Django 3.2 alongside gunicorn:
    * `pip3 install 'django<4' gunicorn`
    * **Note:** Django 3.2 is the *LTS* (Long term support) version which is preferable to use over the Django 4 beta.
1. Install supporting libraries:
    * `pip install dj_database_url==0.5.0 psycopg2`
    * `pip install dj3-cloudinary-storage`
1. Create requirements.txt:
    * `pip freeze --local > requirements.txt`
1. Create an empty folder for your project in chosen location.
1. Create a project in the above folder:
    * `django-admin startproject PROJECT_NAME .` (in the case of this project, the project name was "sfportal")
1. Create an app within the project:
    * `python3 manage.py startapp APP_NAME` (in the case of this project, the app name was "sfblog")
1. Add new app to bottom of the list of installed apps in settings.py and save file
1. Migrate changes: 
    * `python3 manage.py migrate`
1. Test server works locally: 
    * `python3 manage.py runserver`  (This should display the default Django success page)


## Deploying an App to heroku
### Create a New External Database:

For the purposes of this project I used ([ElephantSQL](https://www.elephantsql.com/)) and the following assumes you already have an account:
1. Log in to your account
    * Click "Create new instance"
1. Set up your plan:
    * Give your project a name (commonly the name of your project)
    * Select the Tiny Turtle (Free) plan
    * Tag fields can be left blank
1. Select the nearest location:
    * For me, this was Ireland.
    * Click review and then 'Create Instance'
1. Return to the ElephantSQL dashboard:
    * Click on the **database instance name** for this project: 
    * Copy your **ElephantSQL** *database URL* (It will start with postgres://)


### Create Heroku App:

The below works on the assumption that you already have an account with [Heroku](https://id.heroku.com/login) and are already signed in.
1. Create a new Heroku app:
    * Click "New" in the top right-hand corner of the landing page, then click "Create new app."
1. Give the app a unique name:
    * It will form part of the URL (in the case of this project, I called the Heroku app sci-fi-portal)
1. Select the nearest location:
    * For me, this was Europe.
1. Add Database to the Heroku app:
    * Open *settings* tab and click **Reveal Config Vars**
    * Add a Config Var called **DATABASE_URL**
    * **NOTE:** The **value** should be the ElephantSQL database url copied in the previous step.
1. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    * left box under config vars (variable KEY) = SECRET_KEY
    * right box under config vars (variable VALUE) = Value copied from settings.py in project.

### Attach the Database
I used **gitpod** for this project:
1. In **gitpod**:
    * Create a new ***env.py*** file on top level directory
    * in **env.py**:
        * Import os library: `import os`
        * Set environment variables: `os.environ["DATABASE_URL"] = "*Paste in ElephantSQL database URL*"`
        * Add in secret key: `os.environ["SECRET_KEY"] = "*Make up your own secret key*"`
1. In **Heroku**:
    * Add Secret Key to Config Vars: **SECRET_KEY (value:) "Made up secret key"**
    * For this project it was also necessary to add **PORT 8000** 

Preparing **Environment** and **settings.py** File:

1. Reference env.py in settings.py:

    * Below 'from pathlib import Path': 
        
        * `import os`
        `import dj_database_url`
        `if os.path.isfile("env.py"):`
        `    import env`
    * Remove insecure secret key and replace (*links to the SECRET_KEY variable on Heroku*):
        
        * `SECRET_KEY = os.environ.get('SECRET_KEY')`

1. Comment Out Old Databases Section and **ADD NEW** (*links to DATABASE_URL* variable on Heroku):

    * `DATABASES = {`
    `'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))`

1. Save all Files and Make Migrations:

    * `python3 manage.py makemigrations`
    * `python3 manage.py migrate`


### Store Static and Media Files on Cloudinary

These steps assume you have a Cloudinary account and are logged in.

1. In **Cloudinary**:

    * Copy **CLOUDINARY_URL** from Cloudinary Dashboard

1. In **env.py**:

    * Add **CLOUDINARY_URL** to env.py **NOTE:** Paste in correct section of the link:

    `os.environ["CLOUDINARY_URL"] = "cloudinary://*********"`

1. In **Heroku**:

    * Add Cloudinary URL to Heroku Config Vars (settings tab) **NOTE:** Paste in correct section of the link: CLOUDINARY_URL, cloudinary://*********
    * Add **DISABLE_COLLECTSTATIC** to Heroku Config Vars (*this will be removed for deployment*): DISABLE_COLLECTSTATIC, 1

1. In **settings.py**:

    * Add Cloudinary Libraries to installed apps **NOTE: Order is important!!!**:

    `
        INSTALLED_APPS = [
            ...,
            **'cloudinary_storage'**,
            'django.contrib.staticfiles',
            'cloudinary',
            ...,
        ]
    `

    * Tell Django to use Cloudinary to store media and static files by placing this snippet under the comments indicated below:

    `
        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/3.2/howto/static-files/

        STATIC_URL = '/static/'
        STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        MEDIA_URL = '/media/'
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    `

    * Under the line with BASE_DIR, link to templates directory in Heroku via settings.py:

        * `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`

    * Within TEMPLATES array, add 'DIRS':[TEMPLATES_DIR] like the below example:
    `
        TEMPLATES = [
            {
                …,
                'DIRS': [TEMPLATES_DIR],
                …,
                
                },
            },
        ]
   `
    * Add allowed hosts to settings.py:

    `ALLOWED_HOSTS = ["PROJECT_NAME.herokuapp.com", "localhost"]`

### Final Steps

1. In gitpod: 

    * Create Procfile at the top level of the file structure and insert the following:
    `web: gunicorn PROJECT_NAME.wsgi` (In this instance, the project name was **sfportal**)

    * Create *media, static and templates* folders in root directory


1. In the **terminal**: 
    * **SAVE ALL FILES** Make an initial commit and push the code to the GitHub Repository.

    ` git add .
        git commit -m "Initial deployment"
        git push
    `


1. In **Heroku** for use via the console.

    * Deploy content manually through Heroku. In this instance the deployment method was Github on the main branch
Log in to Heroku via the console and enter your details.


### Cloning on a Local machine or Via Gitpod Terminal

1. Navigate to the GitHub repository, and follow these steps to clone the project into your IDE of choice.

    * **Gitpod** only requires you to have the web extension installed and click the green Gitpod button from the repositories main page. If you are using Gitpod, please skip step 2 below as you do not require a virtual environment to protect your machine.

1. Create the virtual environment with the terminal command **`python3 -m venv venv`.** Once complete add the "venv" file to your ".gitignore" file and use the terminal command **`venv\Scripts\activate.bat`** to activate it.

    * ***IMPORTANT*** If developing locally on your device, ensure you *set up/activate the virtual environment before installing/generating the requirements.txt file*; failure to do this will pollute your machine and put other projects at risk.

1. **Install the requirements** listed in *requirements.txt* using the terminal command  **`pip3 install -r requirements.txt`**

Please note that since the project has been developed from scratch, I have installed required libraries as the project progressed. I have already included a requirements.txt for this app by using the **terminal command** `pip3 freeze > requirements.txt` to generate it.

1. **[Create your own Heroku app](create-heroku-app)** and update allowed hosts in settings.py.

1. **[Create your .env file](#attach-the-database)**

1. **Run server locally with `python3 mange.py runserver`**

**[Back to Readme](README.md)**
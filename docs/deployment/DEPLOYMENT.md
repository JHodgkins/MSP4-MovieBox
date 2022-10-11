# Deployment methods  
This guides aim is to help setup and reproduce the project as it was originally produced.   
Gitpod was used to make the project and the instructions describe this below.

## Table of contents  
1. [Requirements](#requirements)  
2. [Cloning the repository (Gitpod)](#cloning-the-repository-gitpod)  
3. [Cloning the repository (VSCode)](#cloning-the-repository-vscode)  
4. [Deploy the application locally](#deploy-the-application-locally)  
    4.1 [Create a Heroku App](#create-a-heroku-app)  
    4.2 [Create a PostgreSQL database](#create-a-postgresql-database)  
    4.3 [Connecting Heroku to the application](#connecting-heroku-to-the-application)  
    4.4 [Configuring the postgreSQL database](#configuring-the-postgresql-database)  
5. [Create AWS S3 Bucket](#create-aws-s3-bucket)  
    5.1 [Adding the AWS S3 bucket to the project](#adding-the-aws-s3-bucket-to-the-project)  


## Requirements
The project relies upon certain technologies, ensure you have these installed or set them up as you need.  

- An IDE (such as [Visual Studio Code](https://code.visualstudio.com/) or [GitPod](https://www.gitpod.io/))
- [Python](https://www.python.org/downloads/) The project uses Python version 3.8.12  
- An [AWS](https://aws.amazon.com/) account and a [S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) this will be needed for storing the static files.
- [Stripe](https://dashboard.stripe.com/register) Sign up for a free account to have access to test card details, this is what is used to process the purchases on the web application.

## Cloning the repository (Gitpod) 

1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/) Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/JHodgkins/MSP4-MovieBox).
5. Select the green "GitPod" button to the right corner of the repository.
This will start a new gitPod workspace to be created using the code in github.

## Cloning the repository (VSCode)  

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/JHodgkins/MSP4-MovieBox).
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be created.
7. Type 'git clone', and then paste the repository URL.
```
git clone https://github.com/USERNAME/REPOSITORY
```
8. Press Enter, the local clone will be created for you.

## Deploy the application locally  

1. Install all project requirments using the following command in the terminal:
```
pip3 install -r requirements.txt
```
2. If there is not one already, create a `.gitignore` file in the project root directory.
3. Create an `env.py` file in the root directory and add `env.py` to the gitignore file.  
4. Enter the required project's environment variables:
```
import os

os.environ.setdefault("SECRET_KEY", <your_secret_key>)
os.environ.setdefault("DEVELOPMENT", '1')
os.environ.setdefault("STRIPE_PUBLIC_KEY", <your_key>)
os.environ.setdefault("STRIPE_SECRET_KEY", <your_key>)
os.environ.setdefault("STRIPE_WH_SECRET", <your_key>)
```
Stripe keys can be found in the Api section within the Stripe dashboard section.  
For the webhook enter the below in the webhook section.  
```
https://<yourhosturl>/basket/wh/
```
Select 'Receive All Events' and 'Add Endpoint' and your signing secret key will be shown.   

5. Migrations be required to setup the local database, run make migrations and then migrate using the commands below.  
```
python3 manage.py makemigrations

python3 manage.py migrate
```
6. (optional) There are fixture files which contain JSON data to populate the database tables, this can be done using the commands below or data can be added using the django admin console later.  
The fixtures file is located in the 'Products' app folder.  

```
python3 manage.py loaddata category

python3 manage.py loaddata products
```

7. A `superuser` account will need to be created to enable access to the Django Admin console, use the commands below in the terminal to set up this account.  

```
python3 manage.py createsuperuser
```
You will be prompted for an email address and password.  
8. Launch the project using the below command in the terminal.  

```
python3 manage.py runserver
```

9. A server should start running at the address http://127.0.0.1:8000/. In running the server, a new SQLite3 database file (`db.sqlite3`) will be created in the root directory.

### Create a Heroku App  

1. Log into [Heroku](https://id.heroku.com/login) or [create an account](https://signup.heroku.com/login).  
2. Select the `New` button on the top-right of the page, and choose `Create New App`. Give your app a unique name and set the region, choose a region closest to you, Then click `Create App`.  
3. Navigate to the `Deploy` tab on the dashboard and select `Connect to GitHub`.  
4. Search for your repository name, then select `Connect`.  

### create a PostgreSQL database  
1. On the Heroku dashboard, navigate to the `Resources` section.  
2. In the search area, enter `heroku postgres` and `Heroku Postgres` should appear, select this one.  
3. For the plan, select `Hobby Dev - Free`.  
4. Once a plan is selected, `Submit Order Form` to complete.  

### Connecting Heroku to the application  
1. On the Heroku dashboard, select `Settings` and locate `Reveal Config Vars` to set the following variables for this project.  

| Key      | Value  |
|--------------|--------------|
| AWS_ACCESS_KEY_ID | `Your AWS Access Key` |
| AWS_SECRET_ACCESS_KEY | `Your AWS Secret Access Key` |
| DATABASE_URL | `Your Database URL` |
| EMAIL_PASS | `Your Email Password` |
| EMAIL_USER | `Your Email Address`|
| SECRET_KEY | `Your Secret Key` |
| STRIPE_PUBLIC_KEY | `Your Stripe Public Key` |
| STRIPE_SECRET_KEY | `Your Stripe Secret Key` |
| STRIPE_WH_SECRET | `Your Stripe WH Key` |
| USE_AWS | `TRUE` |

Ensure the names match those in the env.py file.  

2. Navigate back to the `Deploy` tab and locate `Automatic Deploys`.  
3. Ensure that the `main` branch is selected, then select `Enable Automatic Deploys`, this will allow Heroku to build everytime it sees a change on GitHub repository.  

### Configuring the postgreSQL database  
1. In the terminal, install the following packages to use Postgres:
```
pip3 install dj_database_url

pip3 install psycopg2_binary

pip3 install gunicorn
```
2. Freeze these dependancies using `python3 freeze > requirements.txt`
3. Now create a `Procfile` file so that Heroku knows which file runs the application, to create a Procfile use the following command.  
```
echo web: python app.py > Procfile
```

4. Push the two files to your repository, using the following commands.  
```
git add .
git commit -m "Commit Message"
git push
```
5. In the project's `settings.py` file:
- Add `import dj_database_url` to imports section (top)
- Locate `DATABASES` constant variable within the settings file and add the following information.  
```
if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ ["DATABASE_URL"])}
else:
    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```
6. By backing up the current sqlite database, it can be migrated to the Heroku database.  
```
./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
```
7. Login into your Heroku account through the terminal, there may be a side window that opens to login.   
```
heroku login -i
```
8. Migrate the data to the Postgres database:
```
python3 manage.py makemigrations

python manage.py migrate
```
9. Another `superuser` account will need to be created as the existing one will not exist, use the following to create.  
```
python3 manage.py createsuperuser
```
10. Push the data into the new posgreSQL database with the below code.  
```
./manage.py loaddata db.json
```
12. Add Heroku to the `ALLOWED HOSTS` varible in the `settings.py` file.   
```
ALLOWED_HOSTS = ['127.0.0.1',
                '<your app name>.herokuapp.com',
                'localhost']
```
13. Commit and Push the changes to your Github repository.  
```
git add .
git commit -m "Commit Message"
git push
```
14. Set up auto push to Heroku app.  
```
heroku git:remote -a <your app name>
```
15. Push to Heroku:
```
git push heroku main
```

Heroku will receive the pushed code from the GitHub repository and setup the app for its first proper deployment using all the variables to run.   
The app should be able to be viewed using the view app button.  

## Create AWS S3 Bucket  

All Static and Media files in the production version of this site are hosted on an [Amazon Web Services](https://aws.amazon.com/ "Link to Amazon Web Services")(AWS) S3 Bucket. 

To create a AWS S3 bucket,
1. Log into [Amazon AWS](https://aws.amazon.com/).
2. Navigate to the [S3 Bucket](https://aws.amazon.com/s3/) and create a S3 bucket for your application using the `Create Bucket` button:
- Give your bucket a name (same or similar to Django and Heroku app names)
- Select the region closest to you
- Uncheck Block Public Access and tick to acknowledge that the bucket will be public
- Click `Create Bucket`  

2. On the Dashboard, locate the `Properities` section and set the follwing settings.  
- `Turn on Static Web Hosting`  

3. On your Bucket Dashboard, locate the `Permissions` section and configure the following:
- In `CORS`:
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]

```
- In `Bucket Policy`, click `Generate Policy` and follow the below steps:
- Click `Policy` > `S3 Bucket Policy`
- Add `*` to the `Principal Field` (selects all principals)
- Set `Action` to `Get Object`
- Paste in `ARN` from previous page
- Click `Add Statement`
- Click `Generate Policy`
- Copy and paste new policy into `Bucket Policy`
- Add `*/` to the end of the `Resources Key`
- Click `Save`
    - In `Access Control List` set the `List Objects Permission` to `everyone`  

4. Access `IAM` Dashboard from `Sevices` dropdown list
    - Create an new user group
    - Create a policy from the `Policy` tab
    - Select `Import Managed Policy`
    - Select `S3 Full Access Policy`
    - Continue to `Create Policy`
    - Attach new policy to the user group by locating the group and selecting `Attach Policy` next to your new policy.
    - Navigate to `Users` tab and select `Add User` Create a name and ensure that it has `Programmatic access`.  
    Add the new user to the group.  
    - Once the user is added, a `.csv` file will be provided.
    Add these variables to your Heroku Config Vars, located in sttings.  
5. Navigate to your new AWS S3 Bucket and manually upload all files currently in the `media` folder of the project.  

## Adding the AWS S3 bucket to the project  
1. In the projects terminal, install the following package.  
```
pip3 install boto3

pip3 install django-storages
```
2. Freeze the new packages to the requirements file using `python3 freeze > requirements.txt`
3. In the `settings.py` file, add `storages` to INSTALLED_APPS variable.
4. In order to link the new AWS S3 Bucket to the project, use this code snippet.  
```
if 'USE_AWS' in os.environ:
    # Enable cache, if required
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # AWS Configaration
    AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
    AWS_S3_REGION_NAME = 'your_region'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. Create a `custom_storages.py` file in the project root directory and within the file add the following code.  
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
location = settings.MEDIAFILES_LOCATION
```
6. Delete the `DISABLE_COLLECTSTATIC` variable from your Heroku Config Vars if you added this before, now commit and push the changes so Heroku will pick up and deploy the new app using Amazon S3 server media and static files.  
```
$ git add .
$ git commit -m "Commit Message"
$ git push
```
By visiting the heroku app website address, you should now see the project running as expected.  

[Back to Repository](https://github.com/JHodgkins/MSP4-MovieBox)   
# The Red Crayon - API
The Red Crayon is a News platform for the artistic world. Users can read the latest articles on what is occurring in the art scene, as well as interact with other users via posts, comments, and following. This section of the project is to support the backend API database, and it is powered by the Django Rest Framework.

#### DEPLOYED API HEROKU [LINK](project5-drf-api.herokuapp.com)
#### DEPLOYED FRONTEND HEORKU [LINK - LIVE SITE](https://red-crayon.herokuapp.com/)
#### DEPLOYED FRONTEND [REPOSITORY](https://github.com/CluelessBiker/project5-red-crayon)

## Table of Contents
+ [User Stories](#user-stories "User Stories")
+ [Database](#database "Database")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Media](#media "Media")

## Usesr Stories:
![]()

## Database:
![SQL Database model](/static/images-readme/readme-models.png)

## Testing:
### Validator Testing: 
- All files passed through [PEP8](http://pep8online.com/) without error.
- Four errors were left unresolved in `settings.py` file, as they were supplied by Django.
![PEP8](/static/images-readme/readme-pep8.png)

### Manual Testing:
1. Manually verified each url path created works & opens without error.
2. Verified that the CRUD functionality is available in each app: Articles, Comments, Followers, Likes, Posts, Profiles
 - Checked this by going to each link.
 - Creating a new item.
 - Checking new item URL path. 
 - Editing the item (not available for Likes, Followers or Users)
 - Deleting the item (Not available for Users or Profiles)
3. Ensured search feature for Posts & Articles apps returns results.

### Unfixed Bugs
- None

## Technologies Used:
### Main Languages Used:
- Python

### Frameworks, Libraries & Programs Used:
- Django
- Django RestFramework
- Cloudinary
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Cors Headers
- DrawSQL

## Deployment:
### Project creation:
- Create the GitHub repository.
- Create the project app on [Heroku](heroku.com).
- under the Resources tab, add Heroku Postgres.
- Once the GitHub repository has opened on GitPod, install the following packages using the `pip install` command:
```
'django<4'
dj3-cloudinary-storage
Pillow
djangorestframework
django-filter
dj-rest-auth
'dj-rest-auth[with_social]'
djangorestframework-simplejwt
dj_database_url psycopg2
gunicorn
django-cors-headers
```
- Create the Django project with the following command:
```
django-admin startproject project_name .
```
- navigate back to [Heroku](heroku.com), and under the Settings tab, add the following configvars:
1. Key: SECRET_KEY | Value: hidden
2. Key: CLOUDINARY_URL | Value: cloudinary://hidden
3. Key: DISABLE_COLLECTSTATIC | Value: 1
4. Key: ALLOWED_HOST | Value: api-app-name.herokuapp.com
- Add two additional configvars once the ReactApp has been created:
5. Key: CLIENT_ORIGIN | Value: https://react-app-name.herokuapp.com
6. Key: CLIENT_ORIGIN_DEV | Value: https://gitpod-browser-link.ws-eu54.gitpod.io
- Check that the trailing slash `\` at the end of both links has been removed.
- Gitpod occasionally updates the browser preview link. Should this occur, the CLIENT_ORIGIN_DEV value shall need to be updated.

- create the env.py file, and add the following variables. The value for DATABASE_URL will be obtained from the Heroku configvars in the previous step:
```
import os

os.environ['CLOUDINARY_URL'] = 'cloudinary://hidden'
os.environ['DEV'] = '1'
os.environ['SECRET_KEY'] = 'hidden'
os.environ['DATABASE_URL'] = 'postgres://hidden'
```
### In settings.py: 
<!-- For reference, refer to: [DRF-API walkthrough settings.py](https://github.com/Code-Institute-Solutions/drf-api/blob/2c0931a2b569704f96c646555b0bee2a4d883f01/drf_api/settings.py) -->
- Add the following to INSTALLED_APPS to support the newly installed packages:
```
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
'rest_framework',
'django_filters',
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
'corsheaders',
```
- Import the database
```
import dj_database_url
```
- Import the regular expression module:
```
import re
```
- Import the env.py settings:
```
import os
if os.path.exists('env.py')
    import env
```
- Below the import statements, add the following variable for Cloudinary:
```
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'
```
- Below INSTALLED_APPS, set site ID:
```
SITE_ID = 1
```
- Below BASE_DIR, create the REST_FRAMEWORK, and inclue page pagination to improve app loading times, pagination count, and date/time format:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
```
- Set the default renderer to JSON:
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
- Underneath that, add the following:
```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```
- Then add:
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
```
- update DEBUG in settings.py to
```
DEBUG = 'DEV' in os.environ
```
- update the DATABASES:
```
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}
```
- Add Heroku app to the ALLOWED_HOSTS, underneath DEBUG
```
os.environ.get('ALLOWED_HOST'),
'localhost',
```
- Below ALLOWED_HOST, add the CORS_ALLOWED as shown in [DRF-API walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/a6250c9e9b284dbf99e53ac8e8b68d3e/0c9a4768eea44c38b06d6474ad21cf75/?child=first):
```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
- It must also be added to the top of MIDDLEWARE:
```
'corsheaders.middleware.CorsMiddleware',
```
- During a deployment issue, it was suggested by a fellow student, Johan, to add the following lines of code below CORS_ALLOW_CREDENTIALS:
```
CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
CSRF_TRUSTED_ORIGINS = [os.environ.get(
    'CLIENT_ORIGIN_DEV', 'CLIENT_ORIGIN',
)]
```
- In addition, Johan also suggested to add the following import statement at the top of the settings.py file:
```
from corsheaders.defaults import default_headers, default_methods
```

### Final requirements:
- create a Procfile, & added the following two lines:
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi
```
- migrate the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
- freeze requirements:
```
pip3 freeze --local > requirements.txt
```
- Add, commit & push the changes to GitHub
- Navigate back to heroku, and under the ‘Deploy’ tab, connect the GitHub repository.
- Deploy the branch.

## CREDITS:

### Content:
- The creation of this API database was provided through the step by step guide of the C.I. DRF-API walkthrough project.
- All classes & functions have been credited.
- Modifications have been made to the 'Profiles' & 'Posts' app models, and an additional app along with models, serializers & views have abeen created by me.

### Media:
- Default post image Photo by Artem Podrez from [Pexels](https://www.pexels.com/photo/image-of-a-whale-made-of-scrap-materials-7048043/)
- Default profile image from [Favicon](https://favicon.io/emoji-favicons/alien-monster)
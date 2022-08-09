# The Red Crayon - API

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
1. Key: SECRET_KEY | Value: arandomsecretkey
2. Key: CLOUDINARY_URL | Value: cloudinary://hidden
3. Key: DISABLE_COLLECTSTATIC | Value: 1
4. Key: ALLOWED_HOST | Value: api-app-name.herokuapp.com
- Add two additional configvars once the ReactApp has been created:
5. Key: CLIENT_ORIGIN | Value: https://react-app-name.herokuapp.com
6. Key: CLIENT_ORIGIN_DEV | Value: https://gitpod-browser-link.ws-eu54.gitpod.io
- Remember to remove the trailing slash `\` at the end of both links!
- Also, gitpod occasionally updated the browser preview link. Should this occur, the CLIENT_ORIGIN_DEV value shall need to be updated.

- create the env.py file, and add the following variables. The value for DATABASE_URL will be obtained from the Heroku configvars in the previous step:
```
import os

os.environ['CLOUDINARY_URL'] = 'cloudinary://hidden'
os.environ['DEV'] = '1'
os.environ['SECRET_KEY'] = 'arandomsecretkey'
os.environ['DATABASE_URL'] = 'postgres://hidden'
```
### In settings.py: 
For reference, refer to: [DRF-API walkthrough settings.py](https://github.com/Code-Institute-Solutions/drf-api/blob/2c0931a2b569704f96c646555b0bee2a4d883f01/drf_api/settings.py)
- Add the following to INSTALLED_APPs to support the newly installed packages:
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
- Import the env.py cloudinary settings:
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
<!-- - Add page pagination within the REST_FRAMEWORK to improve loading times:
```
'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
'PAGE_SIZE': 10,
```
- Add DATETIME_FORMAT to REST_FRAMEWORK to adjust readability.
```
'DATETIME_FORMAT': '%d %b %Y',
``` -->
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
- Below ALLOWED_HOST, add the CORS_ALLOWED as shown in lines 67-74 in the [DRF-API walkthrough](https://github.com/Code-Institute-Solutions/drf-api/blob/2c0931a2b569704f96c646555b0bee2a4d883f01/drf_api/settings.py).
- IMPORTANT!: this code has now been modified, as indicated in the final lesson of the [DRF-API walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/a6250c9e9b284dbf99e53ac8e8b68d3e/0c9a4768eea44c38b06d6474ad21cf75/?child=first), and needs to instead be:
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

## CONFIGURE DRF API
### STEPS : [HERE]()
### DEPLYED HEROKU [LINK](project5-drf-api.herokuapp.com)


- Default image Photo by Artem Podrez from [Pexels](https://www.pexels.com/photo/image-of-a-whale-made-of-scrap-materials-7048043/)
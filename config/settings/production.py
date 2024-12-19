

from os import getenv,path

from dotenv import load_dotenv 


from .base import * 

from .base import BASE_DIR


local_env_file=path.join(BASE_DIR,".env",".env.local")


if path.isfile(local_env_file):
    load_dotenv


# SECURITY WARNING: don't run with debug turned on in production!


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=getenv("DJANGO_SECRET_KEY",)


ADMIN_URL=getenv("DJANGO_ADMIN_URL")
ALLOWED_HOSTS = []




EMAIL_BACKEND="djcelery_email.backends,CeleryEmailBackend"

# EMAIL_HOST=getenv("EMAIL_HOST")
# EMAIL_PORT=getenv("EMAIL_PORT")
# DEFAULT_FROM_EMAIL=getenv("DEFAULT_FROM_EMAIL")
# DOMAIN=getenv("DOMAIN")  

ADMINS=[('Ashraf',"ashrafulislamcsediu@gmail.com"),]

 


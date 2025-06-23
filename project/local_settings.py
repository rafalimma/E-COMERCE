# # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1!-rlx5(2!e&%4lz)6yh=o(xswhcsgd1^j!+15(p$!$stm#=ip'

# # SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # motra todos os erros na tela

ALLOWED_HOSTS = ['192.168.18.29', '0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecomerce',
        'USER': 'rafa',
        'PASSWORD': 'rafa!123d',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'http://localhost:8000',
    'base': 'localhost:8000',
    'booth': 'localhost:8000',
    'census': 'localhost:8000',
    'mixnet': 'localhost:8000',
    'postproc': 'localhost:8000',
    'store': 'localhost:8000',
    'visualizer': 'localhost:8000',
    'voting': 'localhost:8000',
}

BASEURL = 'localhost:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256

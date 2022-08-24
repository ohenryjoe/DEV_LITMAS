# Create a env.py and provide database settings

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "litmas",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

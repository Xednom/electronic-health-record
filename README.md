# electronic-health-record
Sample project that uses the Vuex and Vue router(centralized router for each apps)

# Project setup
Inside the project folder do ```pipenv install```

Fill up the credentials in the .env to your local dev, I've included my personal .env just edit it to your use. 
Below is the sample
```
DEBUG=True
DJANGO_SECRET_KEY='<django secret key>'

# Database
DATABASE_NAME=<database name>
DATABASE_USER=<database user>
DATABASE_PASSWORD=<database password>
DATABASE_HOST=<database host>
DATABASE_PORT=<database port>
```

Migrate DB
``` python manage.py migrate ```

start local server
``` python manage.py runserver ```

# Access to the API Endpoint
To access the API root go to **<localhost:8000>/api/v1/** or **<127.0.0.1:8000>/api/v1/**

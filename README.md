# Hospital-Management-system
This project is done by using Django python framework.

## Connection to MysQL database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hospitalinfy',
        'USER': 'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3308',
    }
}

**Requirements:**

  - crispyforms installation:
      ```pip install django-crispy-forms```
   
  - mysql client installation:
      ```pip install mysqlclient```
      
**Project set up:**
  - navigate to the project folder and run following command:
  
      ```python manage.py runserver```
          
  - migrating the models:
  
    ```python manage.py migrate
       python manage.py makemigrations
       python manage.py migrate```

# Full stack developer masterclass
Creating websites using Python and Django4 (I'm using Django5). The purpose of this repository is to learn front-end tools such as HTML, CSS and, Bootstrap combined with Django framework in python. The end goal for me is to create a website that will showcase my skills.

This course `Django 4 and Python Full-Stack Developer Masterclass` can be found on Udemy. 
```link
https://www.udemy.com/course/django-and-python-full-stack-developer-masterclass/?couponCode=LEADERSALE24B
``` 

This repository contains a devcontainer that is has Python 3.12 with a few vscode extensions I felt was useful (List of extensions can be found in the .devcontainer/devcontainer.json under customizations -> vscode -> extensions). The only prerequisite you would require to run this repository on your system would be to install docker and docker compose. After installing these, you should be able to open the repo in vscode and a prompt will pop up asking if you want to open the repo in the devcontainer. Click "Yes".


## Steps to setup a new project and create an app using Django:
1. Assuming you are in the directory of choice to create your Django project, run the following command to create a project called `my_site` and go into that directory:
    ```cmd
    django-admin startproject my_site
    ```
    ```cmd
    cd my_site/
    ```
2. Create a new app called my_app
    ```cmd
    python manage.py startapp my_app
    ```
3. Create a new file in the my_app folder called `urls.py`
    ```cmd
    cd my_app/ && touch urls.py && cd ..
    ```
4. You can create a new view in the `views.py` in my_app directory and create the url_pattern list similar to the `views.py` in my_site directory.
5. Add the path to my_app urlpatherns in the `urls.py` in the my_site directory using the following syntax:
    ```python
    path('my_app/', include('my_app.urls')),
    ```
6. Run the migration using the following command and you should see `OK` on the terminal. Go to `apps.py` in my_app directory 
    ```cmd
    python manage.py migrate
    ```
7. You need to install the new app you have created `my_app` on the django project `my_site`. Copy the class name and paste it under the `INSTALLED_APPS` list in the `settings.py` file in the following format:
    ```python
    'my_app.apps.MyAppConfig',
    ```
    Now run the following command:
    ```cmd
    python manage.py makemigrations my_app
    ```
8. Once you are happy with the changes, you can apply the changes using the following command:
    ```cmd 
    python manage.py migrate
    ```
    Once this is done, you dont have to specify the template directory in the setting and django will search for the `temaplates` directory in  `my_app` directory.
9. Now in the `my_app` directory, you can create a folder called `templates` and inside this create another folder called `my_app`. This will house all the templates for the app.

10. Finally you can run the server using the following command: 
    ```cmd
    python manage.py runserver
    ```

## Note:
1. To create a super user, you need to be in the Django project directory you created and run the following command:
```python
python manage.py createsuperuser
```
    You would need to enter a username, password and an email_id (This is useful if you need to request a change in password)

## Known Issues:
1. Sometime when you run the server, the content may not refresh. This can be due to two reason in my experience:
    1. You would need to restart the server for the changes to be updated.
    2. It can be a browser related caching issue, try using incognito mode.
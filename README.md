# Setting up this project for testing and a Virtual Environment (venv):
* You need Python installed
1. Download the project
2. With your Terminal of choice go into the 'architect-hub' folder:
        cd [path]/[to]/[the]/[folder]/architect-hub
-  Install virtualenv via pip (can skip if you have it installed):
        pip install virtualenv
3. Create a (venv):
        virtualenv venv
4. Activate the (venv):
        venv/scripts/activate
5. Install all the project dependencies:
        pip install -r dependencies.txt


# Running the APP:
* First you need to have your (venv) activated as shown above.
* You also need to navigate to the project folder:
        cd [path]/[to]/[the]/[folder]/architect-hub/project
  This is the folder containing the manager file 'manage.py' so you can use django-specific commands.


- If you want everything to work properly, you have to set up some things in the settings.py:
        1. Fill in 'email_username' and 'email_password' with a working email (preferably gmail). This will be the 'system' email to send emails like verification codes and etc.
        2. 'admin_email' is used to receive requests for verification after a verification form is sent from a user


- If you need to make migrations:
        py manage.py makemigrations
        py manage.py migrate

- To start the server use:
        py manage.py runserver



* There is a superuser created with the credentials:
        username:       admin@admin.admin
        password:       password
You can create other superusers with the command:
        py manage.py createsuperuser








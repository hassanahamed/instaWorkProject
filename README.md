## Overview

The project is to implement a simple team-member management application that allows the
user to view, edit, add, and delete team members. The app consists of 3 pages

### List page
This page shows a list of all team members. Note that the subtitle should reflect the number
of team members (the screenshot is wrong, it should say 4). Also note that if the team
member is an admin, that is listed next to their name. Clicking a team member should show
the Edit page. Clicking the plus at the top should show the Add page.

### Add page
The Add page appears when the user clicks the "+" on the List page. The user enters a team
member's first & last name, their phone number, and email. Additionally, they can choose the
team member's role (it defaults to regular). Hitting save adds the team member to the list
and shows the List page.
### Edit page
The Edit page appears when the user clicks a team member on the List page. This shows a
form where the user can edit the details of the team member, including changing their role.
Clicking save edits the team member information and shows the List page. Clicking Delete
removes the team member and returns to the List page.

## Structure
```

Dockerfile
README.md
core
   |-- __init__.py
   |-- __pycache__
   |-- admin.py
   |-- appConstants.py
   |-- apps.py
   |-- forms.py
   |-- mapper_config.py
   |-- migrations
   |   |-- __init__.py
   |-- models.py
   |-- team_management_exception.py
   |-- tests.py
   |-- urls.py
   |-- validators.py
   |-- views.py
db.sqlite3
manage.py
requirements.txt
static
   |-- style-delete.css
   |-- style-edit.css
   |-- style.css
teamManagementApp
   |-- __init__.py
   |-- __pycache__
   |   |-- __init__.cpython-310.pyc
   |-- asgi.py
   |-- settings.py
   |-- urls.py
   |-- wsgi.py
templates
   |-- delete.html
   |-- edit.html
   |-- index.html
   |-- new.html

```


## Running

We can run this application using docker - 


    a) Install docker from https://docs.docker.com/get-docker/

    b) Pull the repository and navigate to instaWorkProject folder where the docker file is located.

    c) Run following commands

        docker build -t team_management_app .

        docker run team_management_app:latest

    d) Open browser and go to http://127.0.0.1:8000/




### Time taken - ~12 hours
    



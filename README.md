Simple Survey App
=================

Welcome to a sample Django 2.0 app that does some basic surveying.

Installation
------------
This app runs on mysql, so our installation instructions assumes you already have that installed and the appropriate python dependencies. If you don't, the installation will fail.

1. Clone Repo: `git clone git@github.com:nickburns2006/survey-sample.git`
2. Change directories into where you cloned it.
3. Install requirements: `pip install -r requirements.txt`
4. Update the local `survey/settings.ini` file to have the settings for your specific environment:

```
[settings]
TIMEZONE=UTC
GITHUB_KEY=... # Retrieve by creating app at: https://github.com/settings/applications/new
GITHUB_SECRET=... # Also retrieved from created app
DB_HOST=... # MySQL DB Host
DB_NAME=... # MySQL Database Name. Ensure that the Server already has this created before moving on.
DB_USER=...
DB_PASS=...
```

5. Create local admin user: `python manage.py createsuperuser`. This will allow you to login and set any other user as superuser.
6. Run the migrations: `python manage.py migrate`
7. Run the Django server: `python manage.py runserver`
8. View survey page at: (http://localhost:8000/surveys)

GitHub OAuth Integration
------------------------
The app has integration with GitHub's OAuth2 framework using [social-app-django](https://github.com/python-social-auth/social-app-django).

Managing Surveys
-----------------
To manage the surveys on the system, as a staff/superuser in Django, navigate to http://localhost:8000/surveys/responses/

You will have a list of the questions that are already in the system (and the number of responses so far). You can click on any question and it will take you to the summary/count of the responses for this question.

Adding Survey Questions
~~~~~~~~~~~~~~~~~~~~~~~
From the responses page, you can also click on "+ New Question" to add a new question. This will take you to a form that will have two fields:

* Question: This is the question you'd like a response to
* Survey Answer Options: This `textarea` will allow you to add in the available options for this question. Please place each available choice on its own line.

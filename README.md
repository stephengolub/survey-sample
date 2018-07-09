Simple Survey App
=================

Welcome to a sample Django 2.0 app that does some basic surveying.

Installation
------------
This app runs on mysql, so our installation instructions assumes you already have that installed and the appropriate python dependencies. If you don't, the installation will fail.

1. Clone Repo: `git clone git@github.com:nickburns2006/survey-sample.git`
2. Change directories into where you cloned it.
3. Install requirements: `pip install -r requirements.txt`
4. Update the local `ini` file to have the settings for your specific environment:

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
7. Run the djnago server: `python manage.py runserver`

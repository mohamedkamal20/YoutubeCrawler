# Youtube Crawler

### Overview
This a simple youtube crawler task that crawl videos periodically and save them to database.
### Goals
* Crawl videos from youtube channel/playlist url using [youtube data API](https://developers.google.com/youtube/v3/getting-started).
* Save videos details to database.
* Crawl videos periodically and update the database.
### Requirements
In order to run the application please follow the steps:
- Ubuntu running OS.
- Install Python version 2.7\
`sudo apt install python2`
- Install Python pip for python2\
`sudo apt-get install python-pip`
- Install virtual env. for python2\
`sudo apt install python2 virtualenv`
- Update google APIs\
`pip install --upgrade google-api-python-client`\
`pip install --upgrade google-auth-oauthlib google-auth-httplib2`
- Install Flask\
`pip install flask`
- Install flask-apscheduler\
`pip install Flask-APScheduler`
### Quick start
* Clone the project.
* Create virtual env. inside project folder.\
`virtualenv -p python2.7 env`
* Activate it.\
`source env/bin/activate`
* Install python packages using this command.\
`pip install -r requirements.txt`\
This will install all the python packages which is required for this project to run




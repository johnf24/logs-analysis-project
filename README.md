# Logs Analysis Project
Analyzes the logs of a web service to answer three questions...
1. What are the most popular three articles of all time?
2. Who are the most popular authors of all time?
3. On which days did more than 1% of requests lead to errors?
## Requirements
VirtualBox, Vagrant, PostgreSQL, Python
## Installation
1. Place 'newsdata.sql' inside the vagrant folder
2. Then navigate to the directory inside a vagrant environment and run 'psql -d news -f newsdata.sql' to create database
3. Then run 'psql -d news -f views.sql' to create views
4. Finally run 'python logs.py'
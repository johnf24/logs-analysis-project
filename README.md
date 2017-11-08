# Logs Analysis Project
Analyzes the logs of a web service useing advanced SQL queries to answer three questions...
1. What are the most popular three articles of all time?
2. Who are the most popular authors of all time?
3. On which days did more than 1% of requests lead to errors?

This is the third project for the [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) co-created by Amazon Web Services, GitHub, AT&T and Google.

## Software Requirements
VirtualBox 5.1.18, Vagrant 2.0.0, PostgreSQL 9.3.18, Python 2.7

## Installation Instructions
1. Download the News Data Database [Database](https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip). Then place the 'newsdata.sql' file inside the vagrant folder
2. Then navigate to the directory inside a vagrant environment and run 'psql -d news -f newsdata.sql' to create database
3. Then run 'psql -d news -f views.sql' to create views
4. Finally run 'python logs.py'
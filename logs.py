#!/usr/bin/env python

# Database library
import psycopg2


# Connects to PostgreSQL database
def connect():
    return psycopg2.connect("dbname=news")


# Queries
def queryone():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("select * from pop_articles")

    results = cursor.fetchall()
    print('\n' + "The most popular three articles of all time:" + '\n')
    for i in results:
        print('{} - {}' .format(i[0], i[1]) + " views")

    conn.close()


def querytwo():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("select * from pop_authors")

    results = cursor.fetchall()
    print('\n' + "The most popular article authors of all time:" + '\n')
    for i in results:
        print('{} - {}' .format(i[0], i[1]) + " views")

    conn.close()


def querythree():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("select * from error_rate where percent > 1")

    results = cursor.fetchall()
    print('\n' + "Days when more than 1% of requests lead to errors:" + '\n')
    for i in results:
        print('{0:%B %d, %Y} - {1:2.2f}' .format(i[0], i[1]) + '% errors\n')

    conn.close()


# Calls functions
if __name__ == '__main__':
    queryone()
    querytwo()
    querythree()
    print "Queries generated!"

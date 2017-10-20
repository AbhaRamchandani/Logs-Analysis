#!/usr/bin/env python3

# Goal: Create a reporting tool that prints out reports (in plain text) based
# on the data in the database. This reporting tool is a Python program using
# the psycopg2 module to connect to the database.

import psycopg2

DBNAME = "news"

# Define variables: (i) report, (ii) query, for the 3 reports

report_1 = "The most popular three articles of all time"
query_1 = ("SELECT title AS Title, count(*) AS Views "
           "FROM articles LEFT JOIN log "
           "ON log.path LIKE CONCAT('%', articles.slug, '%') "
           "WHERE log.status LIKE '%200%'"
           "GROUP BY articles.title "
           "ORDER BY Views DESC LIMIT 3 ")

report_2 = "The most popular article authors of all time"
query_2 = ("SELECT authors.name AS Author, count(*) AS Views "
           "FROM articles LEFT JOIN authors "
           "ON articles.author = authors.id "
           "LEFT JOIN log "
           "ON log.path like CONCAT('%', articles.slug, '%') "
           "WHERE log.status LIKE '%200%' "
           "GROUP BY authors.name "
           "ORDER BY views DESC")

report_3 = "Days on which more than 1% of requests led to errors"
query_3 = ("SELECT day, percentERR "
           "FROM "
           "(SELECT day, ROUND(100.0*errcount/hits,2) AS percentERR "
           "FROM "
           "(SELECT date(time) AS day, "
           "SUM(CASE log.status WHEN '200 OK' THEN 0 ELSE 1 END) AS errcount, "
           "COUNT(log.status) AS hits "
           "FROM log "
           "GROUP BY day) AS errorcount "
           "ORDER BY percentERR desc ) as errpercent "
           "WHERE percentERR >1 ")

# Initialize query result variables
# Each query is returning 2 column values
# Use dict() as key-value store for the 2 2 column values
result_1 = dict()
result_2 = dict()
result_3 = dict()


# Return query results for a query - any of query_1, query_2, query_3
def get_stats(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    return results
    db.close()


# Print results of the queries
def print_stats(results):
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' views')
    print '\n'


def print_error_stats(results):
    for result in results:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + '%')
    print '\n'


if __name__ == '__main__':
    print '\n'
    print report_1
    result_1 = get_stats(query_1)
    print_stats(result_1)
    print report_2
    result_2 = get_stats(query_2)
    print_stats(result_2)
    print report_3
    result_3 = get_stats(query_3)
    print_error_stats(result_3)

#!/usr/bin/env python

import psycopg2

dbname = "news"


#def before_query():
#    db = psycopg2.connect(database=dbname)
#    c = db.cursor()
#    return db, c


#def after_query(query, db, cursor):
#    cursor.execute(query)
#    result = cursor.fetchall()
#    db.close()
#    return result
	
def after_query(query):
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


# The most popular three articles of all time
def article():
    # Print titles and number of views of the articles
   # db, c = before_query()
    query = "SELECT title, COUNT(title) AS views \
    FROM articles, log \
    WHERE log.path = concat( '/article/' , articles.slug ) \
    GROUP BY title ORDER BY views DESC LIMIT 3"
    q_result = after_query(query)
    print("\nThe most popular three articles of all time:\n")
    print("Article                            " + "|" + " # of views   ")
    for i in range(0, len(q_result), 1):
        print("\"" + str(q_result[i][0]) + "\" | " + str(q_result[i][1]))


# The most popular article authors of all time
def authors():
    # Print authors and number of views
 #   db, c = before_query()
    query = "SELECT * FROM \
    (SELECT authors.name, COUNT(articles.author) AS views \
    FROM authors, articles, log \
    WHERE authors.id = articles.author \
    and log.path = concat( '/article/' , articles.slug ) \
    GROUP BY authors.name ORDER BY views DESC) AS authors_subq"
    q_result = after_query(query, db, c)
    print("\n\nThe most popular article authors of all time:\n")
    print("Author's name   " + "|" + " # of views  ")
    for i in range(0, len(q_result), 1):
        print(q_result[i][0] + " | " + str(q_result[i][1]))


# Days with more than 1% of requests lead to errors
def log_errors():
    # Print days with more than 1% of requests lead to errors
 #   db, c = before_query()
    query = "SELECT * FROM \
    (SELECT TO_CHAR(date, 'Mon DD, YYYY'), Error, Total, \
    ROUND((Error * 100.0)/Total, 2) \
    AS Percent \
    FROM (SELECT time::timestamp::date AS Date, COUNT(status) AS Total, \
    SUM(case WHEN status = '404 NOT FOUND' THEN 1 else 0 end) AS Error \
    FROM log GROUP BY time::timestamp::date) AS result \
    WHERE (Error * 100.0)/Total > 1.0 \
    ORDER BY Percent DESC) AS errors_subq"
    q_result = after_query(query, db, c)
    print("\n\nDays with more than 1% of requests lead to errors:\n")
    print("Date         " + "|" + " % of errors  ")
    for i in range(0, len(q_result), 1):
        print(q_result[i][0] + " | " + str(q_result[i][3]))


if __name__ == '__main__':
    print("\nLog analysis report\n")
    article()
    authors()
    log_errors()
    print("\n\n\n")

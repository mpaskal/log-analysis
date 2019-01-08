#!/usr/bin/env python

import psycopg2

dbname = "news"


def run_query(query):
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def article():
    """
    The most popular three articles of all time.
    Print titles and number of the articles.
    """
    query = """
            SELECT title, COUNT(title) AS views \
            FROM articles, log \
            WHERE log.path = concat( '/article/' , articles.slug ) \
            GROUP BY title ORDER BY views DESC LIMIT 3;
            """
    q_result = run_query(query)
    print("\nThe most popular three articles of all time:\n")
    print('{:<40}|{:>20}'.format("Article", "# of views"))
    print('-' * 61)
    for article, views in q_result:
        print('{:<40}|{:>20}'.format(article, views))


def authors():
    """
    The most popular article authors of all time.
    Print authors and number of views.
    """
    query = """
            SELECT authors.name, COUNT(articles.author) AS views \
            FROM authors, articles, log \
            WHERE authors.id = articles.author \
            and log.path = concat( '/article/' , articles.slug ) \
            GROUP BY authors.name ORDER BY views DESC
            """
    q_result = run_query(query)
    print("\n\nThe most popular article authors of all time:\n")
    print('{:<40}|{:>20}'.format("Author's name", "# of views"))
    print('-' * 61)
    for authors, views in q_result:
        print('{:<40}|{:>20}'.format(authors, views))


def log_errors():
    """
    Days with more than 1% of requests lead to errors
    Print days with more than 1% of requests lead to errors
    """
    query = """
            SELECT TO_CHAR(date, 'Mon DD, YYYY') AS Day, Error,
            Total, ROUND((Error * 100.0)/Total, 2) \
            AS Percent \
            FROM (SELECT time::timestamp::date AS Date, \
            COUNT(status) AS Total, \
            SUM(case WHEN status = '404 NOT FOUND' THEN 1 else 0 end) \
            AS Error \
            FROM log GROUP BY time::timestamp::date) AS result \
            WHERE (Error * 100.0)/Total > 1.0 \
            ORDER BY Percent DESC
            """
    q_result = run_query(query)
    print("\n\nDays with more than 1% of requests lead to errors:\n")
    print('{:<40}|{:>20}'.format("Date", "# of errors"))
    print('-' * 61)
    for day, error, total, percent in q_result:
        print('{:<40}|{:>20}'.format(day, percent))


if __name__ == '__main__':
    print("\nLog analysis report\n")
    article()
    authors()
    log_errors()
    print("\n\n\n")

#!/usr/bin/python3

"""
loganalysis.py: an analysis tool for access logs.

Prints out reports (in plain text) based on the data in the "news" database.
"""

import psycopg2
import psycopg2.extras

DBNAME = "news"

qry1 = """
select
    a.title article_title,
    count(l.id) num_views
from
    articles a
join
    log l
on
    a.slug = substring(l.path,10)
where
    l.path != '/'
    and l.status = '200 OK'
group by
    1
order by
    2 desc
limit 3;
"""

qry2 = """select
    au.name author,
    count(l.id) num_views
from
    articles a
join
    log l
on
    a.slug = substring(l.path,10)
join
    authors au
on
    a.author = au.id
where
    l.path != '/'
    and l.status = '200 OK'
group by
    1
order by
    2 desc
limit 100;
"""


qry3 = """
select
    date(time) dt,
    sum(case when status = '404 NOT FOUND' then 1 else 0 end)::real /
    count(1)::real * 100 as error_percentage
from
    log
group by
    1
having
    sum(case when status = '404 NOT FOUND' then 1 else 0 end)::real /
    count(1)::real * 100 > 1;
"""


def query(query):
    """
    Execute a query on the database stored in the global variable DBNAME.

    Parameters
    ----------
    query : str
        The query to be executed on the database

    Returns
    -------
    dict
        The results of the database query

    """
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results


results1 = query(qry1)
results2 = query(qry2)
results3 = query(qry3)

print('\nMost popular three articles of all time:')
for item in results1:
    print('"{0}" — {1} views'.format(
        item['article_title'].title(), item['num_views']))

print('\nMost popular article authors of all time:')
for item in results2:
    print('{0} — {1} views'.format(
        item['author'], item['num_views']))

print('\nDays that more than 1 percent of requests led to errors:')
for item in results3:
    date_formatted = item['dt'].strftime("%B %d, %Y")
    error_percentage_formatted = round(item['error_percentage'], 1)
    print('{0} — {1}% errors'.format(
        date_formatted, error_percentage_formatted))

print()

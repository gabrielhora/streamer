import ujson
import logging

import psycopg2
import psycopg2.extras

import config

FETCH_SIZE = 1000
CONN_STRING = "host='{}' dbname='{}' user='{}' password='{}'".format(
    config.DB_HOST, config.DB_NAME, config.DB_USERNAME, config.DB_PASSWORD)


def execute(query, conn=None, params=None):
    params = params or []
    conn = conn or psycopg2.connect(CONN_STRING)
    conn.autocommit = True
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    logging.info('Running query "%s" with params %s', query, params)
    cursor.execute(query, params)
    return conn, cursor


def gen(query, params):
    def generator():
        conn, cursor = (None, None)
        try:
            conn, cursor = execute(query, params=params)
            yield from __dumps(cursor)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return generator()


def __dumps(cursor):
    while True:
        rows = cursor.fetchmany(FETCH_SIZE)
        if not rows:
            break
        for row in rows:
            yield ujson.dumps(row,
                              ensure_ascii=False,
                              escape_forward_slashes=False) + '\n'

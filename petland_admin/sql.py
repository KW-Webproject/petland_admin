import mariadb


def get_conn():
    conn = mariadb.connect(user="root",
                           password="000000",
                           host="193.123.233.236",
                           port=3306,
                           database="test_petland")
    return conn



#!/usr/bin/python3
''' THE File Doc'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''init by filename'''
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )
    cursor = database.cursor()
    state_name = argv[4]
    query = 'SELECT * FROM states WHERE name = "{}" ORDER BY id ASC'.format(
        state_name
    )
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        if state[1] == state_name:
            print(state)
    cursor.close()
    database.close()

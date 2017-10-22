#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


con = lite.connect('test002.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Readings WHERE (Sensor_name like 'temp') AND (Segment_name Like 'Room')")

    rows = cur.fetchall()

    for row in rows:
        x= row[4]
        print x



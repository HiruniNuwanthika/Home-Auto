#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
    con = lite.connect('test002.db')

    cur = con.cursor()

    cur.executescript("""
        DROP TABLE IF EXISTS Readings;
        CREATE TABLE Readings(Sensor_Id INT, dt datetime default current_timestamp, Segment_name TEXT, Sensor_name TEXT, Value REAL);
        INSERT INTO Readings VALUES(001001,CURRENT_TIMESTAMP,'Room','Temp',26.9);
        INSERT INTO Readings VALUES(001002,CURRENT_TIMESTAMP,'Room','Humidity',81.0);
        INSERT INTO Readings VALUES(001002,CURRENT_TIMESTAMP,'Room','PIR',1);


        """)

    con.commit()

except lite.Error, e:

    if con:
        con.rollback()

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()

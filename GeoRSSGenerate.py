import MySQLdb
import urllib.request
def NaturalFeature():
    try:

        # First, create a DB connection:
        connection = MySQLdb.connect(
            host='smartcity1.cwir7vtofu6m.us-west-2.rds.amazonaws.com',
            user='bpasmartcity1',
            passwd='pass1234',
            db='Watershed',
            port=3306)

        # Next, obtain a cursor:
        cursor = connection.cursor()

        # Now we can execute SQL code via our cursor:
        cursor.execute('SELECT * FROM NaturalFeature')

        from xml.sax.saxutils import escape

        with open('NaturalFeature.xml', encoding='utf-8', mode='w') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write('<feed>\n')
            f.write('<title>Watershed_NaturalFeature</title>\n')
            for i in range(cursor.rowcount):
                row = cursor.fetchone()
                f.write('<entry>\n')
                f.write('<title>' + row[2] + '</title>\n')
                f.write('<id>' + row[1] + '</id>\n')
                f.write('<summary>' + row[3] + '</summary>\n')
                f.write('<georss:point>' + row[4] + ' ' + row[5] + '</georss:point>\n')
                f.write('</entry>\n')
            f.write('</feed>\n')
            f.close()

    finally:
        # Don't forget to close DB connection
        if connection:
            connection.close()

def ManmadeFeature():
    try:

        # First, create a DB connection:
        connection = MySQLdb.connect(
            host='smartcity1.cwir7vtofu6m.us-west-2.rds.amazonaws.com',
            user='bpasmartcity1',
            passwd='pass1234',
            db='Watershed',
            port=3306)

        # Next, obtain a cursor:
        cursor = connection.cursor()

        # Now we can execute SQL code via our cursor:
        cursor.execute('SELECT * FROM ManmadeFeature')

        from xml.sax.saxutils import escape

        with open('ManmadeFeature.xml', encoding='utf-8', mode='w') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write('<feed>\n')
            f.write('<title>Watershed_NaturalFeature</title>\n')
            for i in range(cursor.rowcount):
                row = cursor.fetchone()
                f.write('<entry>\n')
                f.write('<title>' + row[2] + '</title>\n')
                f.write('<id>' + row[1] + '</id>\n')
                f.write('<summary>' + row[3] + '</summary>\n')
                f.write('<georss:point>' + row[4] + ' ' + row[5] + '</georss:point>\n')
                f.write('</entry>\n')
            f.write('</feed>\n')
            f.close()

    finally:
        # Don't forget to close DB connection
        if connection:
            connection.close()

def GoodObservation():
    try:
        # First, create a DB connection:
        connection = MySQLdb.connect(
            host='smartcity1.cwir7vtofu6m.us-west-2.rds.amazonaws.com',
            user='bpasmartcity1',
            passwd='pass1234',
            db='Watershed',
            port=3306)

        # Next, obtain a cursor:
        cursor = connection.cursor()

        # Now we can execute SQL code via our cursor:
        cursor.execute('SELECT * FROM Observation')

        from xml.sax.saxutils import escape

        with open('GoodObservation.xml', encoding='utf-8', mode='w') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write('<feed>\n')
            f.write('<title>Watershed_NaturalFeature</title>\n')
            for i in range(cursor.rowcount):
                row = cursor.fetchone()
                if int(row[4]) > 50:
                    f.write('<entry>\n')
                    f.write('<title>' + row[0] + '</title>\n')
                    f.write('<watershed>' + row[1] + '</watershed>\n')
                    f.write('<date>' + row[2] + '</date>\n')
                    f.write('<test>' + row[3] + '</test>\n')
                    f.write('<description>' + row[4] + '</description>\n')
                    f.write('<georss:point>' + row[5] + ' ' + row[6] + '</georss:point>\n')
                    f.write('</entry>\n')
            f.write('</feed>\n')
            f.close()
    finally:
        # Don't forget to close DB connection
        if connection:
            connection.close()

def BadObservation():
    try:
        # First, create a DB connection:
        connection = MySQLdb.connect(
            host='smartcity1.cwir7vtofu6m.us-west-2.rds.amazonaws.com',
            user='bpasmartcity1',
            passwd='pass1234',
            db='Watershed',
            port=3306)

        # Next, obtain a cursor:
        cursor = connection.cursor()

        # Now we can execute SQL code via our cursor:
        cursor.execute('SELECT * FROM Observation')

        from xml.sax.saxutils import escape

        with open('BadObservation.xml', encoding='utf-8', mode='w') as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write('<feed>\n')
            f.write('<title>Watershed_NaturalFeature</title>\n')
            for i in range(cursor.rowcount):
                row = cursor.fetchone()
                if int(row[4]) <= 50:
                    f.write('<entry>\n')
                    f.write('<title>' + row[0] + '</title>\n')
                    f.write('<watershed>' + row[1] + '</watershed>\n')
                    f.write('<date>' + row[2] + '</date>\n')
                    f.write('<test>' + row[3] + '</test>\n')
                    f.write('<description>' + row[4] + '</description>\n')
                    f.write('<georss:point>' + row[5] + ' ' + row[6] + '</georss:point>\n')
                    f.write('</entry>\n')
            f.write('</feed>\n')
            f.close()
    finally:
        # Don't forget to close DB connection
        if connection:
            connection.close()



def GeoRssGenerator():
    NaturalFeature()
    ManmadeFeature()
    GoodObservation()
    BadObservation()

GeoRssGenerator()

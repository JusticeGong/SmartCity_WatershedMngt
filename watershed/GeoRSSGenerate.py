import MySQLdb

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

    # # And fetch query results one by one:
    # for i in range(cursor.rowcount):
    #     row = cursor.fetchone()
    #     print(row)
    #     for j in range(len(row)):
    #         print(row[j])

    from xml.sax.saxutils import escape

    with open('GeoRSS.xml', encoding='utf-8', mode='w') as f:
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



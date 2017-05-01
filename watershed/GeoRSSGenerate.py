from lxml import etree as ET

import _mysql

db=_mysql.connect(host="smartcity1.cwir7vtofu6m.us-west-2.rds.amazonaws.com", user="bpasmartcity1", passwd="pass1234", db="Watershed", port =3306)

c=

c.execute("""SELECT * FROM Watershed""")

# root = ET.Element('background')
# starttime = ET.SubElement(root, 'starttime')
# hour = ET.SubElement(starttime, 'hour')
# # allw = Watershed.objects.get(watershedID="020600030406")
# # print(allw)
# # hour.text = allw
# #
# #
# # print(ET.tostring(root, pretty_print=True, xml_declaration=True))

from lxml import etree as ET
# from watershed import models

root = ET.Element('background')
starttime = ET.SubElement(root, 'starttime')
hour = ET.SubElement(starttime, 'hour')
# allw = Watershed.objects.get(watershedID="020600030406")
# print(allw)
# hour.text = allw
#
#
# print(ET.tostring(root, pretty_print=True, xml_declaration=True))

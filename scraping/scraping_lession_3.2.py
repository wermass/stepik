import xmltodict

fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()  # он в видое обхесняет, но я не докнца понял почему тут 3 строки
fin.close()

estb = 0
net = 0
parsedxml = xmltodict.parse(xml)  # че эт такое
# print(parsedxml['osm']['node'])
for slovar_v_node in parsedxml['osm']['node']:
    if 'tag' in slovar_v_node:
        estb += 1
        # print(slovar_v_node)
    else:
        net += 1
print(estb, net)

#!/usr/local/bin/python3

import sys, json
reload(sys)
sys.setdefaultencoding('utf8')

jsonFile = open("fich.json")

dados = json.load(jsonFile)
jsonFile.close()

output = open("output.ttl","w")

for d in dados:
    ident = d["category"]+d["year"]
    output.write('###  http://prc2019.di.uminho.pt/2019/Prize#'+ident+'\n')
    output.write(':'+ident+' rdf:type owl:NamedIndividual , :Prize ;\n')
    output.write('  :category  "'+ d["category"]+'" ;\n')
    if 'overallMotivation' in d:
        output.write('  :overallMotivation  '+ d["overallMotivation"]+' ;\n')
    
    for laureate in d["laureates"]:
        output.write('  :hasLaureate  :L'+laureate["id"]+" ;\n")
    output.write('  :year  '+ d["year"]+" .\n\n")

for d in dados:
    for l in d["laureates"]:
        output.write('###  http://prc2019.di.uminho.pt/2019/Prize#L'+l["id"]+'\n')
        output.write(':L'+l["id"]+' rdf:type owl:NamedIndividual , :Laureate ;\n')
        output.write('  :firstname  "'+ l["firstname"]+'" ;\n')
        output.write('  :surname  "'+ l["surname"]+'" ;\n')
        if 'motivation' in l:
            output.write('  :motivation  '+ l["motivation"]+' ;\n')
        output.write('  :share  '+l["share"]+' .\n\n')
 
output.close()

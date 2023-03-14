import json

f = open("un_archivo.json", "w")
f.write('{"nombre": "German", "edad": 35}')
f.close()

f = open("un_archivo.json", "r")
content = f.read()
print(content)
f.close()

f = open("un_archivo.json")
dict_desde_json = json.load(f)
f.close()

dict_desde_json["Nombre"] = "Federico"

f = open("un_archivo.json", "w")
json.dump(dict_desde_json,f)
f.close()
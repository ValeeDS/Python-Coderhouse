f = open("un_archivo.txt", "w", encoding='utf-8')
f.write("Mi primera línea de texto\n")
f.write("Esto es otra secuencia de texto\n")
f.write("Sigo otra cosa\n")
f.close()

f = open("un_archivo.txt", "r", encoding='utf-8')
content = f.read()
print(content)
f.close()

print("----------")

f = open("un_archivo.txt", "r", encoding='utf-8')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

print("----------")

f = open("un_archivo.txt", "r", encoding='utf-8')
lineas = f.readlines()
f.close()

lineas_upper = []

for linea in lineas:
    lineas_upper.append(linea.upper())
    
f = open("un_archivo.txt", "w", encoding='utf-8')

for linea in lineas_upper:
    f.write(linea)
    
f.close()
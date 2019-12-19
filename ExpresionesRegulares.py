import re

palabra = input("Ingrese una Palabra: ")
print(palabra)
if(re.match('[A-Za-z_ÑñÁáÉéÍíÓóÚú]', palabra)):
    print("Coincidencia")
else:
    print("Sin Coincidencia")

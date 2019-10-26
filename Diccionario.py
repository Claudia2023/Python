
DicPalb = input('Ingresar una Palabra: ')
Diccionario = {'Door':'Puerta', 'Map':'Mapa', 'Hello':'Hola', 'Scissors':'Tijeras', 'Calendar':'Calendario'}
pal = input('Ingresar una Palabra2: ')

if DicPalb == 'Door': print ('Palabra 1 Traducida:',Diccionario['Door'])
elif DicPalb == 'Map': print ('Palabra 1 Traducida:',Diccionario['Map'])
elif DicPalb == 'Hello': print ('Palabra 1 Traducida:',Diccionario['Hello'])
elif DicPalb == 'Scissors': print ('Palabra 1 Traducida:',Diccionario['Scissors'])
elif DicPalb == 'Calendar': print ('Palabra 1 Traducida:',Diciomario['Calendar'])
else:print('ERROR::Palabra no Encontrada')


for key, value in Diccionario.items(): 
    if value == pal:
        print('Palabra 2 Traducida:',key)

print('Gracias Por su Visita')        
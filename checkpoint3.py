#Ejercicio 1: Tipos de datos
name = "Maria Esther"
modulos_aprendidos = 2
lenguajes_aprendidos = ["html", "python", "javascript"]
alta_en_full_stack= True

#Ejercicio 2: Index
name = "Maria Esther"
abbreviation_name = name[:3]
print (abbreviation_name)

#Ejercicio 3: primer elemento de lista
lenguajes_aprendidos = ["html", "python", "javascript"]
primer_lenguaje = lenguajes_aprendidos [0]
print (primer_lenguaje)

#Ejercicio 4: sumar 10
modulos_aprendidos = 2
nuevos_modulos = modulos_aprendidos + 10
print (nuevos_modulos)

#Ejercicio 5: Index -1
lenguajes_aprendidos = ["html", "python", "javascript"]
ultimo_lenguaje = lenguajes_aprendidos [-1]
print (ultimo_lenguaje)

#Ejercicio 6: Split function
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split (',')
print (names_list)

#Ejercico 7: Upper function with strings
name = "Maria Esther"
name_first = name [0:5]
name_mayus = name_first.upper() + 'Esther'
print (name_mayus)

#Ejercicio 8: utilizar string interpolation
avance_curso = f"He aprendido {modulos_aprendidos} modulos en el curso"
print (avance_curso)

#Ejercicio 9: print "Hello world"
print ("Hello world")

#Ejercicio 10: cambiar saludo por despedida
saludo = "Hola mundo"
saludo = saludo.replace ("Hola", "Adiós")
print (saludo)
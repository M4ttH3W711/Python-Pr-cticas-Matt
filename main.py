print("Hello CodeSandbox!")
""" print = Escribir """
print("Matthew")
print("Jovany")
print("Mayo")
print("Fernando")
print("Eduardo")
print("Giovanni")
print("Axel")
print("Dante")
print("Miguel")
print("Jair")

""" Vamos a concatenar """
nombre = "Matthew"
apellido = "Jiménez"
print("Hola, mi nombre es: ", nombre) # Hola, mi nombre es:  Matthew
print("Hola, mi nombre es: ",nombre, apellido) # Hola, mi nombre es:  Matthew Jiménez
print("Hola, mi nombre es: ",nombre,"y mi apellido es: ",apellido) # Hola, mi nombre es:  Matthew y mi apellido es:  Jiménez

""" Concatenación con diferentes tipos de datos """
mi_edad=18
mi_nombre="Matthew"
mi_apellido_paterno="Jiménez"
mi_apellido_materno="Silva"
soy_maestro= False
soy_alumno= True

""" Uso de type - Averigua que tipo de dato recibes """
print(type(mi_edad)) # <class 'int'>
print(type(mi_nombre)) # <class 'str'>
print(type(soy_alumno)) # <class 'bool'>
print("Hola, mi edad es:",mi_edad,", mis apellidos son:",mi_apellido_paterno,mi_apellido_materno,"¿Soy alumno?",soy_alumno)

""" Operaciones matemáticas """
numero_uno=10
numero_dos=5

print(numero_uno+numero_dos) #15
print(numero_uno-numero_dos) #5
print(numero_uno*numero_dos) #50
print(numero_uno/numero_dos) #2.0
print(numero_uno%numero_dos) #0

""" TAREA """
print("Escribe 2 números:")
num_1 = int(input("Primer término: "))
num_2 = int(input("Segundo término: "))
print(num_1 + num_2) #"Suma:",
print(num_1 - num_2) #"Resta:",
print(num_1 * num_2) #"Multiplicación:",
print(num_1 / num_2) #"División:",
print(num_1 % num_2) #"Residuo:",
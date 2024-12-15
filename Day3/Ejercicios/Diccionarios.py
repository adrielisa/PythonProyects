diccionario = {'c1':'valor1','c2':'valor2'}
print(diccionario)

resultado = diccionario['c1']
print(resultado)


#Diccionario sobre datos de un cliente, podemos obtener cualquier valor y mostrarlos
cliente = {'nombre':'Juan', 'Apellido':'Chan','Estatura':'1.68'}
estatura_cliente = cliente['Estatura']
nombre_cliente = cliente['nombre']
print(f' La estatura de {nombre_cliente} es {estatura_cliente}')

#Dentro de un diccionario podemos agregar listas e íncluso otros diccionarios
dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100,'s2':'ala','s3':1221}}
print(dic['c2'][1]) #Busca el valor número 2 del diccionario y selecciona el índice 1 de esa lista

#Hacer mayúscula un valor que está dentro de una lista en el diccionario
reto_dic = {'c1':['a','b','c'], 'c2':['d','e','f']}
mayuscula = (reto_dic['c2'][1])
mayuscula2 = mayuscula.upper()
print(mayuscula2)


#Añadir elementos/claves al diccionario
añadir_dic = {1:'a', 2:'b'}
print(añadir_dic)

añadir_dic[5] = 'c' #Creo una nueva clave en el diccionario
añadir_dic[2] = 'uwu' #Modifico una clave en el diccionario

print(añadir_dic)
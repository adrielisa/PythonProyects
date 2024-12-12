nombre = input("Ingrese su nombre: ")
venta_mes = input("Ingrese la cantidad vendida en el mes: ")
venta_mes = float(venta_mes)
comision = round((venta_mes * 13) /100,2)

print(f"Bienvenido {nombre}, tu comisión del mes es de {comision}")
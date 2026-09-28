#Ejercicio 1 · Quitar duplicados conservando el orden
#Dada ciudades = ["Quito","Guayaquil","Quito","Cuenca","Guayaquil"],
#obtén una lista sin repetidos respetando el orden de aparición 
#(un set solo no alcanza).

ciudades = ["Quito", "Guayaquil", "Quito", "Cuenca", "Guayaquil"]

vistas = set()      #conjunto de control: para preguntar rápido si ya apareció
unicas = []         #lista de resultado: conserva el orden
for ciudad in ciudades:
    if ciudad not in vistas:
        vistas.add(ciudad)
        unicas.append(ciudad)

print(unicas)   #['Quito', 'Guayaquil', 'Cuenca']

#Ejercicio 2 · Contar con un diccionario
#Con la misma lista, arma un diccionario 
#{"Quito": 2, "Guayaquil": 2, "Cuenca": 1}.

conteo = {}
for ciudad in ciudades:
    conteo[ciudad] = conteo.get(ciudad, 0) + 1     # .get evita el KeyError la primera vez

print(conteo)

#El más repetido:
mas_repetida = max(conteo, key=conteo.get)
print(mas_repetida)

#Ejercicio 3 · Conjuntos en acción
#inscritos_matematica = 
#{"Ana","Luis","Sol","Marco"} y inscritos_ingles = {"Luis","Marco","Ruth"}. 
#Responde con código: ¿quiénes están en las dos?, ¿quiénes solo en matemática?, 
#¿cuántos estudiantes distintos hay en total?

ambas       = inscritos_matematica & inscritos_ingles     #{'Luis','Marco'}
solo_mate   = inscritos_matematica - inscritos_ingles     #{'Ana','Sol'}
total       = len(inscritos_matematica | inscritos_ingles)  #5

print(sorted(ambas), sorted(solo_mate), total)

#Ejercicio 4 · De lista de diccionarios a índice
#Con clientes = [{"id":1,"nombre":"Ana"},{"id":2,"nombre":"Luis"}], 
#crea un diccionario {id: cliente} para acceder por id sin recorrer la lista.
#Luego imprime el nombre del id 2.

indice = {cliente["id"]: cliente for cliente in clientes}
print(indice[2]["nombre"])       #'Luis'

#Diferencia de costo:
#recorrer la lista  -> revisa hasta N registros
#indice[2]          -> una sola operación, sin importar cuántos haya

#Ejercicio 5 · Tuplas como registros inmutables
#Dada ventas = [("enero", 1500), ("febrero", 1800), ("marzo", 1200)], 
#imprime el mes con mayor venta y el total, usando desempaquetado de tuplas.

total = sum(monto for _mes, monto in ventas)

mejor_mes, mejor_monto = max(ventas, key=lambda venta: venta[1])

print(f"Total: {total}")
print(f"Mejor mes: {mejor_mes} con {mejor_monto}")

for mes, monto in ventas:              # desempaquetado en el for
    print(f"{mes:<10} {monto}")

#Ejercicio 6 · Sobre el proyecto
#Agrega al Controlador la función clientes_por_ciudad() 
#que devuelva un diccionario {"Guayaquil": ["Ana", "Luis"], "Quito": ["Sol"]}.

def clientes_por_ciudad():
    agrupados = {}
    for registro in gestor.leer():
        ciudad = registro.get("ciudad", "").title() or "Sin ciudad"
        #setdefault: si la ciudad no estaba, crea la lista vacía y luego agrega
        agrupados.setdefault(ciudad, []).append(registro["nombre"])
    return agrupados
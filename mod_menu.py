# Modulos de Funciones
import json
import os

# Definir el nombre del archivo JSON
ARCHIVO_ORDENES = "ordenes_trabajo.json"

# Cargar las órdenes de trabajo desde el archivo JSON o crear una lista vacía si no existe
if os.path.exists(ARCHIVO_ORDENES):
    with open(ARCHIVO_ORDENES, "r", encoding="utf-8") as f:
        guardar_orden = json.load(f)
else:
    guardar_orden = []

# Función para guardar las órdenes en el archivo JSON
def guardar_ordenes_json():
    with open(ARCHIVO_ORDENES, "w", encoding="utf-8") as f:
        json.dump(guardar_orden, f, ensure_ascii=False, indent=4)
        
#Menu Principal
def menu():
    print("1. Crear una nueva orden de trabajo")
    print("2. Consultar una orden de trabajo")
    print("3. Modificar una orden de trabajo")
    print("4. Eliminar una orden de trabajo")
    print("5. Generar reporte de órdenes de trabajo del día")
    print("6. Generar reporte de Ingresos del Mes")
    print("7. Generar reporte de uso de impresoras")
    print("8. Salir")
    opcion = input("Seleccione una opción:  ")
    return opcion


def crear_orden_trabajo():
    print("Crear una nueva orden de trabajo")
    # Generar un ID consecutivo automáticamente
    if guardar_orden:
        ultimo_id = max(int(o["id_orden"]) for o in guardar_orden)
        id_orden = str(ultimo_id + 1)
    else:
        id_orden = "1"
    print(f"ID de la nueva orden de trabajo: {id_orden}")
    cliente = input("Ingrese el nombre del cliente: ")
    fecha = input("Ingrese la fecha de creación (DD-MM-AAAA): ")
    fecha2 = input("Ingrese la fecha de entrega (DD-MM-AAAA): ")
    descripcion = input("Tipo de Producto: ")
    medidas = input("Medidas: ")
    cantidad = input("Cantidad: ")
    diseñador = input("Nombre del diseñador: ")
    impresora = input("Nombre de la impresora: ")
    obcervaciones = input("Observaciones: ")
    precio= input("Precio: ")
    estado = input("Ingrese el estado de la orden (Pendiente/Completada/Entregada): ")
    nueva_orden = {
        "id_orden": id_orden,
        "cliente": cliente,
        "fecha": fecha,
        "fecha2": fecha2,
        "descripcion": descripcion,
        "medidas": medidas,
        "cantidad": cantidad,
        "diseñador": diseñador,
        "impresora": impresora,
        "obcervaciones": obcervaciones,
        "precio": precio,
        "estado": estado      
       
    }
    guardar_orden.append(nueva_orden)
    guardar_ordenes_json()
    print(f"Orden de trabajo {id_orden} creada con éxito.\n")
    
    

def modificar_orden_trabajo():
    print("Modificar una orden de trabajo")
    id_orden = input("Ingrese el ID de la orden de trabajo: ")
    orden = next((o for o in guardar_orden if o["id_orden"] == id_orden), None)
    if orden:
        print(f"Orden de trabajo encontrada: {orden}")
        print("Ingrese los nuevos datos (deje en blanco para no modificar):")
        cliente = input(f"Cliente ({orden['cliente']}): ") or orden["cliente"]
        descripcion = input(f"Descripción ({orden['descripcion']}): ") or orden["descripcion"]
        fecha2 = input(f"Fecha de entrega ({orden['fecha2']}): ") or orden["fecha2"]
        cantidad = input(f"Cantidad ({orden['cantidad']}): ") or orden["cantidad"]
        obcervaciones = input(f"Observaciones ({orden['obcervaciones']}): ") or orden["obcervaciones"]
        estado = input(f"Estado ({orden['estado']}): ") or orden["estado"]
        orden["cliente"] = cliente
        orden["descripcion"] = descripcion
        orden["fecha2"] = fecha2
        orden["cantidad"] = cantidad
        orden["obcervaciones"] = obcervaciones
        orden["estado"] = estado
        guardar_ordenes_json()
        print(f"Orden de trabajo {id_orden} modificada con éxito.\n")
    else:
        print(f"No se encontró una orden de trabajo con ID {id_orden}.\n")
        
        
        
def consultar_orden_trabajo():
    print("Consultar una orden de trabajo")
    while True:
        criterio = input("¿Desea buscar por nombre de cliente (1), por fecha (2) o (3) para volver al menú principal: ")
        if criterio == "1":
            cliente = input("Ingrese el nombre del cliente: ")
            ordenes = [o for o in guardar_orden if o["cliente"].lower() == cliente.lower()]
            if ordenes:
                for orden in ordenes:
                    print(f"Orden de trabajo encontrada: {orden}")
                break
            else:
                print(f"No se encontró una orden de trabajo con el cliente {cliente}. Intente de nuevo.")
        elif criterio == "2":
            fecha = input("Ingrese la fecha de la orden (DD-MM-AAAA): ")
            ordenes = [o for o in guardar_orden if o["fecha"] == fecha]
            if ordenes:
                for orden in ordenes:
                    print(f"Orden de trabajo encontrada: {orden}\n")
                break
            else:
                print(f"No se encontró una orden de trabajo con la fecha {fecha}. Intente de nuevo.")
        elif criterio == "3":
            print("Volviendo al menú principal...\n")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")



def eliminar_orden_trabajo():
    print("Eliminar una orden de trabajo")
    id_orden = input("Ingrese el ID de la orden de trabajo: ")
    orden = next((o for o in guardar_orden if o["id_orden"] == id_orden), None)
    if orden:
        guardar_orden.remove(orden)
        guardar_ordenes_json()
        print(f"Orden de trabajo {id_orden} eliminada con éxito.\n")
    else:
        print(f"No se encontró una orden de trabajo con ID {id_orden}.\n")
        
def generar_reporte_ordenes_dia():
    print("Generar reporte de órdenes de trabajo del día")
    fecha = input("Ingrese la fecha (DD-MM-AAAA): ")
    ordenes_dia = [o for o in guardar_orden if o["fecha"] == fecha]
    if ordenes_dia:
        print(f"Órdenes de trabajo del día {fecha}:")
        for orden in ordenes_dia:
            print(f"ID: {orden['id_orden']}, Cliente: {orden['cliente']}, Descripción: {orden['descripcion']}, Estado: {orden['estado']}")
    else:
        print(f"No se encontraron órdenes de trabajo para la fecha {fecha}.\n")
        
def generar_reporte_ingresos_mes():
    print("Generar reporte de Ingresos del Mes")
    mes = input("Ingrese el mes (MM-AAAA): ")
    ingresos_mes = sum(float(o["precio"]) for o in guardar_orden if o["fecha"].endswith(mes))
    print(f"Ingresos totales del mes {mes}: ${ingresos_mes:.2f}\n")
    
def generar_reporte_uso_impresoras():
    pass
    
            





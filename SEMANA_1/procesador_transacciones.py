import os

def cargar_ventas(transacciones):
    lista_ventas = [] 
    
    try:
        with open(transacciones, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            
            print(f"--> El archivo tiene internamente {len(lineas)} líneas detectadas.\n")
            
            for i, linea in enumerate(lineas, start=1):
                linea_limpia = linea.strip()
                
                if not linea_limpia:
                    print(f"    [Línea {i}]: Está vacía (Saltada)")
                    continue
                    
                partes = linea_limpia.split(",")
                
                
                if len(partes) != 3:
                    print(f"    [Línea {i}]: ¡Problema! Encontré {len(partes)} partes en vez de 3. Texto leído: '{linea_limpia}'")
                    continue
                
                venta = {
                    "cliente_id": partes[0].strip(),
                    "tipo_transaccion": partes[1].strip().upper(),
                    "monto": int(partes[2].strip()),
                }
                lista_ventas.append(venta)
                
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en: {transacciones}")
                
    return lista_ventas

def calcular_valor_total(lista_ventas):
    total = 0
    for venta in lista_ventas:
        if isinstance(venta, dict) and "monto" in venta:
            total = total + venta["monto"]
    return total

def filtrar_por_categoria(lista_ventas, categoria):
    lista_filtrada = []
    for venta in lista_ventas:
        if isinstance(venta, dict) and venta.get("tipo_transaccion") == categoria:
            lista_filtrada.append(venta)
    return lista_filtrada

def ejecutar_sistema():
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_automatica = os.path.join(carpeta_actual, "transacciones.txt")
    
    print("--- PROCESANDO TRANSACCIONES ---")
    print(f"Buscando archivo en: {ruta_automatica}\n")
    
    ventas = cargar_ventas(ruta_automatica)

    if not ventas:
        print("\n❌ No se cargaron transacciones válidas. Revisa los mensajes de arriba para ver qué falló en el texto.")
        return

    print("\n✅ ¡Datos cargados con éxito!")
    total = calcular_valor_total(ventas)
    print(f"Valor total de las ventas: {total}")

    
    tipo_a_filtrar = "DEBITO"
    tipo_transaccion = filtrar_por_categoria(ventas, tipo_a_filtrar)

    print(f"\nVentas de tipo {tipo_a_filtrar}:")
    if not tipo_transaccion:
        print(f"  No se encontraron transacciones de tipo {tipo_a_filtrar}")
    for venta in tipo_transaccion:
        print(f"  - Cliente: {venta['cliente_id']} | Monto: {venta['monto']}")

if __name__ == "__main__":
    ejecutar_sistema()
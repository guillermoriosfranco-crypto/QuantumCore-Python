# ==========================================
# ESTRUCTURA BASE (Clases de la Semana 4)
# ==========================================

class Transaccion:
    def __init__(self, id_transaccion, tipo):
        self.id_transaccion = id_transaccion
        self.tipo = tipo

class TransaccionEspecifica(Transaccion):
    def __init__(self, id_transaccion, tipo, monto):
        super().__init__(id_transaccion, tipo)
        self.monto = monto

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto):
        if int(nuevo_monto) < 0:
            raise ValueError(f"Monto negativo no permitido (${nuevo_monto})")
        self._monto = int(nuevo_monto)

    def __str__(self):
        return f"[{self.id_transaccion}] {self.tipo} | Monto: ${self.monto}"


# ==========================================
# PASOS 1, 2 y 3: LOGICA DE LECTURA ROBUSTA
# ==========================================

def cargar_transacciones(nombre_archivo):

    transacciones_validas = []
    
    print("--- Iniciando Procesamiento de Archivo ---")
    
    with open(nombre_archivo, "r") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            linea = linea.strip()
            if not linea:  
                continue
                
            try:
                datos = linea.split(",")
                
                if len(datos) < 3:
                    raise TypeError("Datos insuficientes en la línea")
                
                id_tx, tipo, monto_str = datos[0], datos[1], datos[2]
                
                nueva_tx = TransaccionEspecifica(id_tx, tipo, monto_str)
                

                transacciones_validas.append(nueva_tx)
                print(f"  [Éxito] Línea {numero_linea}: Procesada correctamente -> {nueva_tx}")

            except ValueError as error_valor:

                print(f"  [ERROR - ValueError] Línea {numero_linea}: '{linea}'. Detalle: {error_valor}")
                continue  
                
            except TypeError as error_tipo:
   
                print(f"  [ERROR - TypeError] Línea {numero_linea}: '{linea}'. Detalle: {error_tipo}")
                continue  

    return transacciones_validas


# ==========================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================
def ejecutar_programa():
    archivo_datos = "transacciones_corruptas.txt"
    
    lista_final = cargar_transacciones(archivo_datos)
    print("\n--- Resumen de Transacciones Procesadas Exitosamente ---")
    for tx in lista_final:
        print(tx)
        
    print(f"\nProceso finalizado. Total exitosas: {len(lista_final)} de 7 registros.")

if __name__ == "__main__":
    ejecutar_programa()
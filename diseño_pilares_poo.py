import os

class Transaccion:
    """Representa una transacción individual con sus atributos básicos."""
    def __init__(self, cliente_id, tipo_transaccion, monto):
        self.cliente_id = cliente_id.strip()
        self.tipo_transaccion = tipo_transaccion.strip().upper()
        self.monto = int(monto.strip())

    def __str__(self):
        return f"Cliente: {self.cliente_id} | Monto: {self.monto}"

class GestorTransacciones:
    """Gestiona la carga, almacenamiento y operaciones de las transacciones."""
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.lista_ventas = []

    def cargar_datos(self):
        """Carga y valida los datos desde el archivo de texto."""
        try:
            with open(self.nombre_archivo, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()
                print(f"---> El archivo tiene {len(lineas)} líneas detectadas.\n")

                for i, linea in enumerate(lineas, start=1):
                    linea_limpia = linea.strip()
                    if not linea_limpia:
                        continue
                    
                    partes = linea_limpia.split(",")
                    if len(partes) != 3:
                        print(f"[Línea {i}]: Problema! Se esperaban 3 partes, se encontraron {len(partes)}.")
                        continue
                    
                    # Crear objeto y añadir a la lista
                    nueva_transaccion = Transaccion(partes[0], partes[1], partes[2])
                    self.lista_ventas.append(nueva_transaccion)
            
            return len(self.lista_ventas) > 0
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en: {self.nombre_archivo}")
            return False

    def calcular_total(self):
        """Suma el monto de todas las transacciones cargadas."""
        return sum(t.monto for t in self.lista_ventas)

    def filtrar_por_categoria(self, categoria):
        """Retorna una lista de transacciones filtradas por tipo."""
        return [t for t in self.lista_ventas if t.tipo_transaccion == categoria.upper()]

def ejecutar_sistema():
    """Orquestador del sistema (equivalente a la lógica anterior)."""
    ruta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "transacciones.txt")
    
    print("--- PROCESANDO TRANSACCIONES (POO) ---")
    gestor = GestorTransacciones(ruta_archivo)
    
    if gestor.cargar_datos():
        print("✅ Datos cargados con éxito!")
        print(f"Valor total de las ventas: {gestor.calcular_total()}")
        
        tipo = "DEBITO"
        filtradas = gestor.filtrar_por_categoria(tipo)
        
        print(f"\nVentas de tipo {tipo}:")
        for t in filtradas:
            print(f" - {t}")
    else:
        print("\n❌ No se cargaron transacciones válidas.")

if __name__ == "__main__":
    ejecutar_sistema()
class TransaccionBase:
    """Clase base: encapsula el monto y define el comportamiento comun."""

    def __init__(self, id_transaccion, monto):
        self.id_transaccion = id_transaccion
        self.monto = monto                 

    
    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, nuevo_monto):
        if int(nuevo_monto) < 0:
            raise ValueError("El monto no puede ser negativo.")
        self._monto = int(nuevo_monto)

    def calcular_impacto(self):
        raise NotImplementedError("Cada tipo de transaccion define su impacto.")

    def obtener_informacion(self):
        return f"{self.id_transaccion} | {type(self).__name__} | ${self.monto}"

class TransaccionCredito(TransaccionBase):
    def calcular_impacto(self):             
        return round(self.monto * 0.02, 2)  


class TransaccionDebito(TransaccionBase):
    def calcular_impacto(self):             
        return 1500                        


def crear_transaccion(id_transaccion, tipo, monto):
    if tipo == "CREDITO":
        return TransaccionCredito(id_transaccion, monto)
    if tipo == "DEBITO":
        return TransaccionDebito(id_transaccion, monto)
    raise ValueError(f"tipo desconocido '{tipo}'")


def leer_transacciones(nombre_archivo):
    transacciones = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            
            if len(partes) < 3:
                print(f"  [Aviso] Linea ignorada (menos de 3 valores): {linea.strip()}")
                continue
            
            id_transaccion, tipo, monto = partes[0], partes[1], partes[2]
            try:
                transacciones.append(crear_transaccion(id_transaccion, tipo, monto))
            except ValueError as error:
                print(f"  [Aviso] Se ignoro {id_transaccion}: {error}")
    return transacciones


def ejecutar_sistema():
    transacciones = leer_transacciones("transacciones.txt")

    print("\n--- Transacciones cargadas ---")
    for t in transacciones:
        
        print(t.obtener_informacion(), "-> impacto:", t.calcular_impacto())



if __name__ == "__main__":
    ejecutar_sistema()

# librodiario.py

import logging
from typing import List, Dict

logging.basicConfig(filename="logs/log_contable.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Transaccion:
    def __init__(self, tipo: str, monto: float):
        if tipo not in ["ingreso", "egreso"]:
            logging.error(f"Tipo de transacción inválido: {tipo}")
            raise ValueError("Tipo de transacción inválido")
        if monto < 0:
            logging.error(f"Monto negativo no permitido: {monto}")
            raise ValueError("Monto no puede ser negativo")
        self.tipo = tipo
        self.monto = monto

class LibroDiario:
    def __init__(self):
        self.transacciones: List[Transaccion] = []

    def agregar_transaccion(self, tipo: str, monto: float):
        transaccion = Transaccion(tipo, monto)
        self.transacciones.append(transaccion)
        logging.info(f"Transacción registrada: {tipo} - {monto}")

    def calcular_resumen(self) -> Dict[str, float]:
        ingresos = sum(t.monto for t in self.transacciones if t.tipo == "ingreso")
        egresos = sum(t.monto for t in self.transacciones if t.tipo == "egreso")
        return {"ingresos": ingresos, "egresos": egresos}

    def cargar_transacciones_desde_archivo(self, ruta: str):
        try:
            with open(ruta, "r") as archivo:
                for linea in archivo:
                    tipo, monto = linea.strip().split(",")
                    self.agregar_transaccion(tipo, float(monto))
        except Exception as e:
            logging.error(f"Error al cargar archivo: {e}")
            raise

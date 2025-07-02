# librodiario.py

import logging
from typing import List, Dict

# Configuración de logs
logging.basicConfig(
    filename="logs/log_contable.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Transaccion:
    """
    Representa una transacción contable: ingreso o egreso.
    """

    def __init__(self, tipo: str, monto: float) -> None:
        """
        Inicializa una transacción válida o lanza una excepción si hay errores.

        Args:
            tipo (str): Tipo de transacción ("ingreso" o "egreso").
            monto (float): Monto de la transacción. Debe ser positivo.

        Raises:
            ValueError: Si el tipo es inválido o el monto es negativo.
        """
        if tipo not in {"ingreso", "egreso"}:
            logging.error(f"Tipo de transacción inválido: {tipo}")
            raise ValueError("Tipo de transacción inválido")

        if monto < 0:
            logging.error(f"Monto negativo no permitido: {monto}")
            raise ValueError("Monto no puede ser negativo")

        self.tipo: str = tipo
        self.monto: float = monto


class LibroDiario:
    """
    Sistema contable para registrar transacciones y calcular resúmenes.
    """

    def __init__(self) -> None:
        """
        Inicializa el libro con una lista vacía de transacciones.
        """
        self.transacciones: List[Transaccion] = []

    def agregar_transaccion(self, tipo: str, monto: float) -> None:
        """
        Agrega una transacción al libro contable.

        Args:
            tipo (str): Tipo de transacción ("ingreso" o "egreso").
            monto (float): Monto positivo.

        Raises:
            ValueError: Si los datos de entrada son inválidos.
        """
        transaccion = Transaccion(tipo, monto)
        self.transacciones.append(transaccion)
        logging.info(f"Transacción registrada: {tipo} - {monto}")

    def calcular_resumen(self) -> Dict[str, float]:
        """
        Calcula un resumen total de ingresos y egresos.

        Returns:
            Dict[str, float]: Diccionario con totales de ingresos y egresos.
        """
        ingresos: float = sum(
            t.monto for t in self.transacciones if t.tipo == "ingreso"
        )
        egresos: float = sum(
            t.monto for t in self.transacciones if t.tipo == "egreso"
        )
        return {"ingresos": ingresos, "egresos": egresos}

    def cargar_transacciones_desde_archivo(self, ruta: str) -> None:
        """
        Carga transacciones desde un archivo de texto CSV.

        Args:
            ruta (str): Ruta del archivo que contiene las transacciones.
        """
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    tipo, monto = linea.strip().split(",")
                    self.agregar_transaccion(tipo, float(monto))
        except Exception as e:
            logging.error(f"Error al cargar archivo: {e}")
            raise

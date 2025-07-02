import unittest
from librodiario import LibroDiario

class TestLibroDiario(unittest.TestCase):

    def test_creacion_instancia(self):
        libro = LibroDiario()
        self.assertIsInstance(libro, LibroDiario)

    def test_agregar_transaccion_valida(self):
        libro = LibroDiario()
        libro.agregar_transaccion("ingreso", 100)
        self.assertEqual(len(libro.transacciones), 1)

    def test_agregar_transaccion_monto_negativo(self):
        libro = LibroDiario()
        with self.assertRaises(ValueError):
            libro.agregar_transaccion("ingreso", -50)

    def test_agregar_transaccion_tipo_invalido(self):
        libro = LibroDiario()
        with self.assertRaises(ValueError):
            libro.agregar_transaccion("otro", 50)

    def test_calcular_resumen(self):
        libro = LibroDiario()
        libro.agregar_transaccion("ingreso", 200)
        libro.agregar_transaccion("egreso", 100)
        resumen = libro.calcular_resumen()
        self.assertEqual(resumen["ingresos"], 200)
        self.assertEqual(resumen["egresos"], 100)

    def test_cargar_transacciones_desde_archivo(self):
        with open("logs/archivo_prueba.csv", "w") as f:
            f.write("ingreso,300\n")
            f.write("egreso,150\n")

        libro = LibroDiario()
        libro.cargar_transacciones_desde_archivo("logs/archivo_prueba.csv")
        resumen = libro.calcular_resumen()
        self.assertEqual(resumen["ingresos"], 300)
        self.assertEqual(resumen["egresos"], 150)

if __name__ == "__main__":
    unittest.main()

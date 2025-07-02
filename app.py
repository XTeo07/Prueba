# app.py

from librodiario import LibroDiario

def main():
    libro = LibroDiario()

    try:
        libro.agregar_transaccion("ingreso", 1000)
        libro.agregar_transaccion("egreso", 300)
        libro.agregar_transaccion("ingreso", 500)
        libro.agregar_transaccion("egreso", 200)
        
        # Transacción inválida para probar logs de error
        libro.agregar_transaccion("otro", 100)

    except ValueError as e:
        print(f"Error en la transacción: {e}")

    resumen = libro.calcular_resumen()
    print("Resumen contable:")
    print(f"Ingresos: {resumen['ingresos']}")
    print(f"Egresos: {resumen['egresos']}")

if __name__ == "__main__":
    main()

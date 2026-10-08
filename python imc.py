"""
Programa: Calculadora de Índice de Masa Corporal (IMC)
Autor: Jose Murillo
Fecha: 08/10/2026
Descripción: Solicita datos del usuario, valida entradas, calcula el IMC
y muestra un reporte formateado. Maneja campos vacíos y valores incorrectos.
"""

def calcular_imc():
    # Validar Nombre
    while True:
        nombre = input("Ingresa tu nombre: ").strip()
        if nombre:
            nombre = nombre.capitalize()
            break
        print("❌ Error: El nombre no puede quedar vacío. Inténtalo de nuevo.\n")

    # Validar Apellido
    while True:
        apellido = input("Ingresa tu apellido: ").strip()
        if apellido:
            apellido = apellido.capitalize()
            break
        print("❌ Error: El apellido no puede quedar vacío. Inténtalo de nuevo.\n")

    # Validar Edad
    while True:
        edad_texto = input("Ingresa tu edad: ").strip()
        if not edad_texto:
            print("❌ Error: La edad no puede estar vacía.\n")
            continue
        try:
            edad = int(edad_texto)
            if edad > 0:
                break
            print("❌ Error: La edad debe ser mayor a cero.\n")
        except ValueError:
            print("❌ Error: Ingresa un número válido para la edad.\n")

    # Validar Peso
    while True:
        peso_texto = input("Ingresa tu peso en kg: ").strip()
        if not peso_texto:
            print("❌ Error: El peso no puede estar vacío.\n")
            continue
        try:
            peso = float(peso_texto)
            if peso > 0:
                break
            print("❌ Error: El peso debe ser mayor a cero.\n")
        except ValueError:
            print("❌ Error: Ingresa un número válido para el peso.\n")

    # Validar Altura
    while True:
        altura_texto = input("Ingresa tu altura en metros (ej: 1.65): ").strip()
        if not altura_texto:
            print("❌ Error: La altura no puede estar vacía.\n")
            continue
        try:
            altura = float(altura_texto)
            if altura > 0:
                break
            print("❌ Error: La altura debe ser mayor a cero.\n")
        except ValueError:
            print("❌ Error: Ingresa un número válido para la altura.\n")

    # Cálculo del IMC
    imc = peso / (altura ** 2)

    # Reporte final formateado
    print("\n" + "=" * 50)
    print(f"           REPORTE — DATOS PERSONALES")
    print("=" * 50)
    print(f"Nombre:    {nombre} {apellido}")
    print(f"Edad:      {edad} años")
    print(f"Peso:      {peso} kg")
    print(f"Altura:    {altura} m")
    print("-" * 50)
    print(f"Tu IMC es: {imc:.2f}")
    print("=" * 50)
    print("\n✅ Programa finalizado con éxito.")


# Ejecutar el programa
if __name__== "__main__":
    calcular_imc()
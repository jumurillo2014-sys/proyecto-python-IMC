# PASO 1: Capturar datos desde teclado con input()
edad = input("Ingresa tu edad: ")
peso = input("Ingresa tu peso en kg: ")
estatura = input("Ingresa tu estatura en metros: ")

# PASO 2: Convertir tipos (casting)
edad = int(edad)          # → entero
peso = float(peso)        # → decimal
estatura = float(estatura) # → decimal

# PASO 3: Calcular IMC = peso / (estatura²)
imc = peso / (estatura ** 2)

# Mostrar resultados
print("\n═══════════════════════════════")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"Tu IMC es: {imc:.2f}")  # .2f = 2 decimales
print("═══════════════════════════════")
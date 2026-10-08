# 1. Capturar datos del usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

# 2. Calcular IMC
imc = peso / (altura ** 2)

# 3. Formatear nombres con primera letra en mayúscula
nombre_formateado = nombre.strip().capitalize()
apellido_formateado = apellido.strip().capitalize()

# 4. Mostrar reporte con f-strings, limpio y profesional
print("\n" + "="*40)
print(f"        REPORTE DE DATOS PERSONALES")
print("="*40)
print(f"Nombre:    {nombre_formateado} {apellido_formateado}")
print(f"Edad:      {edad} años")
print(f"Peso:      {peso} kg")
print(f"Altura:    {altura} m")
print("-"*40)
print(f"Tu IMC es: {imc:.2f}")
print("="*40)
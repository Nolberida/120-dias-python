

nombre = "Noly"
edad = 31
estatura = 1.59
ciudad = "mexico"
me_gusta_programar = True
promedio_ventas = 2236.571428

# ejercicio 1

print(f"Hola soy {nombre} tengo {edad} años, mido {estatura} mestros, vivo en {ciudad} y ¿me gusta programar? {me_gusta_programar}")


# ejercicio 2

print(f"en 10 años tendre {edad + 10} y mi estatura sera {estatura * 100} cm")


# ejercicio 3

print(f"promedio de ventas: {promedio_ventas:.2f}")
print(f"promedio de ventas: {promedio_ventas:.1f}")
print(f"promedio de ventas: {promedio_ventas:.0f}")


# 2236.57
# 2236.6
# 2237


# ejemplo 4

anio = input("en que año naciste?")
nombre2 = input("cual es tu nombre?")

print(f"hola {nombre2} , tu edad es {2026-int(anio)} años")

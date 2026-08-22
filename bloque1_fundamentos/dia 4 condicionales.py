
#descomentar
#ejercicio 1

#edad = int(input("¿cual es tu edad?: "))

#if edad >= 18:
    #print("eres mayor de edad")

#else: 
    #print("eres menor de edad")


#ejercicio 2

#calificacion = int(input("¿que calificacion es? "))

#No esta mal pero se puede simplificar
#if calificacion >= 90:
    #print("excelente")
#elif calificacion <= 89 and calificacion >= 70:
    #print("aprobada")
#elif calificacion <= 69 and calificacion >= 60:
    #print("vas raspando")
#else:
    #print("reprobado")


#descomentar
#simplificado
#if calificacion >= 90:
    #print("Excelente")
#elif calificacion >= 70:
    #print("Aprobada")
#elif calificacion >= 60:
    #print("Vas raspando")
#else:
    #print("reprobado")

#ejercicio 3

#numero = int(input("inserta un numero:"))

#if numero % 2 == 0:
    #print(f"el numero {numero} es par")
#else:
    #print(f"el numero {numero} es impar")




# ejercicio 4
#numero = 15

#if numero % 3 == 0 and numero % 5 == 0:
    #print("FizzBuzz")
#elif numero % 3 == 0:
    #print("Fizz")
#elif numero % 5 == 0:
    #print("Buzz")
#else:
    #print(numero)



#numero 15: sera fizzBuzz
#numero 8: sera numero
#numero 45: sera fizzbuzz


#ejercicio 5

edad = int(input("¿Cual es tu edad?"))
credencial = input("¿tienes credencial?")


if edad >= 18:
    if credencial.lower() == "si":
        print("pasale")
    else: 
        print("Sin INE no hay fiesta")
else:
    print("regresa en unos años")

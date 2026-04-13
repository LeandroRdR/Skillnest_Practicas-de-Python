print("Ejercicios de bucle for básico")

#Codifica el ejercicio 1. Básico
for I in range(101):
    print(I)

#Codifica el ejercicio 2. Múltiples de 2
for i in range (2,501,2):
    print(i)

#Codifica el ejercicio 3. Contando Vanilla Ice
for i in range(1,101):
   if i % 10 == 0:
        print("baby")
   elif i % 5 == 0:
        print("ice ice")
   else:
        print(i)

Suma_total = 0

#Codifica el ejercicio 4. Wow. Número gigante a la vista
for i in range(0,500001,2):
    Suma_total += i
print(Suma_total)

#Codifica el ejercicio 5. Regrésame al 3
for i in range(2025,2,-3):
    print(i)

#Codifica el ejercicio 6. Contador dinámico
numInicial = 10
numFinal = 50
multiplo = 7

#numFinal + 1 (51) para que el 50 sea incluido en la revisión
for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
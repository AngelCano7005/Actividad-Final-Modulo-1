#10. **Calculadora básica**
    #Crea una función que reciba dos números y una operación (`"suma"`, `"resta"`, `"multiplicación"`, `"división"`) y devuelva el resultado correspondiente.
    
print("Bienvenido a la calculadora, escribe alguna de las opciones que deseas realizar")
print("\n(1). Suma")
print("(2). Resta")
print("(3). Multiplicación")
print("(4). División")

while True:
    try:
        operacion = int(input("\nDigita el número de opción para realizar la operación matemática: "))
        
        if operacion >4:
            continue
        break
    
    except ValueError:
        print("\nEntrada no válida. Intente de nuevo.")

numero_uno = int(input("\nPor favor digite el primer número: "))
numero_dos = int(input("Por favor digite el segundo número: "))

def calculadora(num_operacion:int) ->int:
    
    if num_operacion == 1:
        resultado = numero_uno + numero_dos
        print(f"\nLa suma: {numero_uno} + {numero_dos} = {resultado}")
        
    elif num_operacion == 2:
        resultado = numero_uno - numero_dos
        print(f"\nLa resta: {numero_uno} - {numero_dos} = {resultado}")
    
    elif num_operacion == 3:
        resultado = numero_uno * numero_dos
        print(f"\nLa multiplicación: {numero_uno} * {numero_dos} = {resultado}")
    
    else:
        resultado = numero_uno / numero_dos
        print(f"\nLa división: {numero_uno} / {numero_dos} = {resultado}")

calculadora(operacion)
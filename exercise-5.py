#Create a program that continuously reads numbers from the user until they enter 0. The program should calculate and display the sum of all positive numbers and the sum of all negative numbers entered by the user.

soma_positivos = 0
soma_negativos = 0

while True:
    numero = int(input("Digite um número ou pressione 0 para encerrar: "))
    
    if numero > 0:
        soma_positivos += numero
    elif numero < 0:
        soma_negativos += numero
    else:
        break

    print(f"Soma dos números positivos: {soma_positivos}")
    print(f"Soma dos números negativos: {soma_negativos}")


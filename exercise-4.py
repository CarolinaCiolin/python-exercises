# Create a program that reads the weight and height of a person, calculates their Body Mass Index (BMI), and classifies it as "Underweight", "Ideal weight", or "Overweight" based on the following criteria:   

peso = float(input("Digite seu peso em kg: "))
             
altura = float(input("Digite sua altura em metros: "))

imc =   peso / (altura ** 2)

print(f"Seu IMC é: {imc:.1f}")

if imc < 20:
    print("Abaixo do peso")
elif 20 <= imc < 25:
    print("Peso ideal")
else:
    print("Acima do peso")


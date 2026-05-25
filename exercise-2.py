
compra = float(input("Digite o valor da compra: "))

compra_a_vista = compra - (compra * 0.10)
compra_parcelada = compra + (compra * 0.05)

print(f"Valor da compra à vista: R$ {compra_a_vista:.2f}")
print(f"Valor da compra parcelada: 3x de R$ {(compra_parcelada / 3):.2f} = R$ {compra_parcelada:.2f}")

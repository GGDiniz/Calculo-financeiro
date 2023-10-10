import math 

raio = float(input("Digite o raio do reservatorio em metros: "))

altura = float(input("Informe a altura do reservatorio em metros: "))

preco_tinta = float(input("Informe o valor da tinta em Reais(R$): "))

eficiencia_tinta = float(input("Informe a eficiencia da tinta (Em metros quadrados por litro): "))

area_total = 2 * math.pi * raio * altura + 2 * math.pi * raio ** 2

quantidade_tinta_litros = area_total / eficiencia_tinta


custo_tinta = quantidade_tinta_litros * preco_tinta

print(f"Área Total do Reservatório: {area_total:.2f} metros quadrados")
print(f"Quantidade de Tinta Necessária: {quantidade_tinta_litros:.2f} litros")
print(f"Custo da Tinta: R$ {custo_tinta:.2f}")
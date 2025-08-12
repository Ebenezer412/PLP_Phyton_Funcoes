# Função que calcula o preço com desconto
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        desconto = price * (discount_percent / 100)
        preco_final = price - desconto
        return preco_final
    else:
        return price

# Solicita os dados ao usuário
preco_original = float(input("Digite o preço original do item: R$ "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))

# Calcula o preço final usando a função
preco_final = calculate_discount(preco_original, porcentagem_desconto)

# Mostra o resultado
if preco_final < preco_original:
    print(f"Desconto aplicado! Preço final: R$ {preco_final:.2f}")
else:
    print(f"Nenhum desconto aplicado. Preço original: R$ {preco_original:.2f}")

print('Bem-vindo à Loja do Natan Dos Santos Silva')

# Tratamento de exceção para o valor do produto
try:
    preco_original = float(input('Entre com o valor do produto: '))
except ValueError:
    print('Erro: Por favor, insira um valor numérico para o produto.')
    exit()

# Tratamento de exceção para a quantidade do produto
try:
    quantidade = int(input('Entre com a quantidade do produto: '))
except ValueError:
    print('Erro: Por favor, insira um valor numérico inteiro para a quantidade do produto.')
    exit()

# Sem descontos
sem_desconto = preco_original * quantidade
print('Valor SEM desconto: R${}'.format(sem_desconto))

# Descontos
d2 = sem_desconto - (sem_desconto * 0.03)
d3 = sem_desconto - (sem_desconto * 0.05)
d4 = sem_desconto - (sem_desconto * 0.08)

# Valor com desconto de 0%:
if sem_desconto < 1000:
    print('Não há desconto.')
# Valor com desconto de 3%:
elif 1000 <= sem_desconto < 3000:
    print('O valor COM desconto: R${}'.format(d2))
# Valor com desconto de 5%:
elif 3000 <= sem_desconto < 5000:
    print('O valor COM desconto: R${}'.format(d3))
# Valor com desconto de 8%:
elif sem_desconto >= 5000:
    print('O valor COM desconto: R${}'.format(d4))
# Condição para casos não cobertos pelas condições anteriores:
else:
    print('Condição não prevista. Verifique os valores inseridos.')
import numpy as np

distribuidora_fat = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
estados = ["SP", "RJ", "MG", "ES", "Outros"]
v = c = soma = porcentagem = i = e = 0
percentagens = []
for v in distribuidora_fat:
    soma += v
    c += 1
print(soma)
for i in distribuidora_fat:
    porcentagem = (100*i)/soma
    percentagens.append(porcentagem)
    c += 1

print(percentagens)

for pos, valores in enumerate(percentagens):
    print(f'O estado {estados[pos]} contribuiu com {valores:.2f}% dentro do valor mensal da distribuidora')
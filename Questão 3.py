faturamento = [22174.1664, 24537.6698, 26139.6134, 26742.6612, 42889.2258, 46251.174, 11191.4722, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 25681.8318, 1718.1221, 13220.495, 8414.61]
media = soma = v = c = dias =  0
for v in faturamento:
    soma += v
    c += 1
print(f'A soma é {soma}')
print(f'O menor numero é {min(faturamento)} e o maior numero é {max(faturamento)}')
media = soma/len(faturamento)
print(f'A média é {media}')
for v in faturamento:
    if v > media:
        dias += 1
        c+1
print(f'Dias em que o faturamento diario foi superior à media mensal foram {dias}')







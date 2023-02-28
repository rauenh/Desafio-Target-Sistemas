n = 100
c = presente = naopresente = 0
ultimotermo = 1
penultimotermo = 1
fibo = ultimotermo + penultimotermo
compara = int(input("Digite aqui o número que você deseja consultar na sequência de Fibonacci de até 100 termos:"))

while c <= n:
    if c == 0 or c==1:
        print('1 ->', end='')
    elif c > 1:

        fibo = ultimotermo + penultimotermo
        penultimotermo = ultimotermo
        ultimotermo = fibo
        print('{}-> '.format(fibo), end='')
        if compara == fibo:
            presente += 1
        else:
            naopresente += 1

    c +=1
if presente == 1:
    print(f'\nO número {compara} pertence à sequência.')
else:
    print(f'\nO número {compara} não pertence à sequência.')
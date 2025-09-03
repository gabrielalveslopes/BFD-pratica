a =int(input('digite um numero: '))
b = int(input('digite um segundo numero: '))

maior = (a>b)* a + (b>a)*b + (a == b) * a

print(f'maior valor?{maior}')
soma = int(input())
A = int(input())
B = int(input())

numeros = int()

for i in range(A, B + 1):
    soma2 = 0
    for j in str(i):
        soma2 += int(j)
    else:
        if soma2 == soma:
            numeros += 1

print(numeros)
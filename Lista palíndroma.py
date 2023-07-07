quantidade = int(input())
array = input().split(' ')


contracao = int()

for i in range(len(array)):
    if int(array[i]) != int(array[quantidade - (i + 1)]) and i < quantidade/2:
        contracao += 1



print(contracao)
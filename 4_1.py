n = int(input("Введите количество чисел N: "))
m = int(input("ВВедите число M, которому должны быть кратны числа выше: "))
k = int(input("ВВедите число K, меньше которого должны быть конечные числа: "))
i = 1
counter = 0
while (True):
    if (i % m == 0) and (i < k):
        counter += 1
        if counter > n:
            break
        print(i)
    i += 1
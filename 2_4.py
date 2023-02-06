plus = 0
minus = 0

for i in range(3):
    temp = int(input("Введите число: "))
    if temp > 0:
        plus += 1
    elif temp == 0:
        print(" ты ввёл ноль, алло")
    else:
        minus += 1
print(f"Итак, \n положительных: {plus} \n отрицательных: {minus}")







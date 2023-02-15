n = int(input("Введите число: "))
print("Чётные числа от 2 до n: ")

counter = 0
for i in range(2, n+1,2): # шаг 2, чтоб печатать только чётные, так как начинается всё с 2-ки
     if counter % 5 == 0:
         print()
     counter += 1
     print(i, end=" ")

'''Дан список чисел и на вход поступает число N, необходимо сместить список на
указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]'''
import random
def transform(lst, num) ->list[int]:
    return lst[num:]+lst[:num]

lth = int(input("длина массива: "))
usr_lst = [random.randint(1, 100) for i in range(lth)]
print(f"Исходный список: {usr_lst}")
num = int(input("Введите № индекса: "))
print(f"Результат: {transform(usr_lst, num)}")

'''Дан список рандомных чисел,
необходимо отсортировать его в виде, сначала
четные, потом нечётные'''
import random
def filter_list(usr_lst) -> list[int]:
    even = list(filter(lambda a: a % 2 == 0, usr_lst))  # чётные
    odd = list(filter(lambda a: a % 2 != 0, usr_lst))  # нечётные
    return even+odd

num = int(input("длина массива : "))
usr_lst = [random.randint(1,100) for i in range(num)]
print(f"Исходный список: {usr_lst}")
print(f'отфильтрованный список: \n {filter_list(usr_lst)}')


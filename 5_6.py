'''Дан список рандомных чисел,
необходимо отсортировать его в виде, сначала
четные, потом нечётные'''
import random
def filter_list_mine(usr_lst) -> list[int]:
    even = list(filter(lambda a: a % 2 == 0, usr_lst))  # чётные
    odd = list(filter(lambda a: a % 2 != 0, usr_lst))  # нечётные
    return even+odd

def filter_list_tutors(usr_lst):
    usr_lst.sort(key=lambda x: x % 2 != 0)
    return usr_lst

num = int(input("длина массива : "))
usr_lst = [random.randint(1,100) for i in range(num)]
print(f"Исходный список: {usr_lst}")
print(f'отфильтрованный список: \n {filter_list_tutors(usr_lst)}')


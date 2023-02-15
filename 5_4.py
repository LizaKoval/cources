def filter_to_str(lst):
    return list(filter(lambda a: isinstance(a, str), lst))

usr_lst = [1,2,5.98, 'Liz', [1,2], 'b', 'Python']
print(f"Результат:  {filter_to_str(usr_lst)}")
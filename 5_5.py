def my_reverse(list) -> list[int]:
    return [list[len(list)-1-i] for i in range(len(list))]

lst = [1,2,50,6,7,89]
print( my_reverse(lst))
def neighbors_sum(lst):
    result = []
    for i in range(len(lst)):
        if i != len(lst)-1:
            result.append(lst[i-1]+lst[i+1])
        else:
            result.append(lst[i - 1] + lst[0])  # for the lst element
    return result

usr_lst = [1, 2, 5, 84, 35, 17, 12, 6, 9]
print(neighbors_sum(usr_lst))

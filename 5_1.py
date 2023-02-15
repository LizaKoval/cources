def transfer( num, sys) -> int:
    if sys == 2:  # if into binary
        return bin(num)

    else: # num is dec
        st = str(num)
        res = 0
        for i in range(len(st)):
            res += int(st[i]) * 2**(len(st)-i-1)
        return res


print("Введите число и систему счисления, в которую нужно перевести: ")
num = int(input("число: "))
sys = int(input("систему счисления: "))
print(f'Результат перевода: {transfer(num, sys)}')
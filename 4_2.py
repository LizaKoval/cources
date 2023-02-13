num1 = int(input("Введите первое число: "))
operator = input("Введите операцию(+, -, /, *, ^: ): ")
num2 = int(input("Введите второе число: "))
result = 0
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else: print("Вы ввели некорректные значения")

elif operator == '*':
    result = num1 * num2
else:
    result = num1 ** num2

print(f'Результат {num1} {operator} {num2} = {result}')


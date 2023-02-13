n = int(input("Введите число n: "))
data = {i: {'email': input("email: "),
            'name': input("name: ")}
    for i in range(0, n)}

print(data.values())


text = input("Введите текст, пожалуйста: ")
letters = {a: text.count(a) for a in set(text)}
print(letters)


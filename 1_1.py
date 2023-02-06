msg = input("Введите, пожалуйста, текст с '-': ")
print(f'{msg.replace(" ","-")}')  # 1st way (by replace method)
print(f'{"-".join(list(msg.split()))}')  # 2nd way (splitting string into words by split() method then joining list of words in whole string)
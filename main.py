import re

reg_name = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')

user_name = input("Введите имя пользователя: ")

if reg_name.match(user_name):
    print(f"Имя {user_name} принято!")
else:
    print("Ввод некорректен повторите! Повторите ввод данных!\n")

import re

reg_name = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_surname = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')

user_name = input("Введите имя пользователя: ")
if reg_name.match(user_name):
    print(f"Имя {user_name} принято!")
else:
    print("Ввод некорректен! Повторите ввод данных!\n")

user_surname = input("Введите фамилию пользователя: ")
if reg_name.match(user_surname):
    print(f"Фамилия {user_surname} принята!")
else:
    print("Ввод некорректен! Повторите ввод данных!\n")

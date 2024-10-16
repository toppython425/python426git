import re

reg_name = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_surname = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_phone = re.compile(r'^[+]\d{1,3}\(\d{1,3}\)(\d{7})$')

user_name = input("Введите имя пользователя: ")
if reg_name.match(user_name):
    print(f"Имя {user_name} принято!")
else:
    print("Ввод некорректен! Повторите ввод данных!\n")

user_surname = input("Введите фамилию пользователя: ")
if reg_surname.match(user_surname):
    print(f"Фамилия {user_surname} принята!")
else:
    print("Ввод некорректен! Повторите ввод данных!\n")

user_phone = input("Введите номер телефона пользователя: ")
if reg_name.match(user_phone):
    print(f"Номер телефона {user_phone} принят!")
else:
    print("Ввод некорректен! Повторите ввод данных!\n")

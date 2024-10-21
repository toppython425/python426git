import re

reg_name = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_surname = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_phone = re.compile(r'^[+]\d{1,3}\(\d{1,3}\)(\d{7})$')
reg_email = re.compile(r'^[A-Za-z0-9]+@yandex\.ru$')

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

user_email = input("Введите e-mail пользователя: ")
if reg_name.match(user_email):
    print(f"E-mail {user_email} принят!")
else:
    print("Ввод некорректен! Повторите ввод данных!\n")

print("Выполненная задача от Васи!")

print("Выполненная задача от Петра!")

print("Выполнена задача task_1")
print("Код сделан работоспособным")

print("Код от Васи")


# 1 - commit

def multiply_numbers(a, b):
    return a * b


print(multiply_numbers(3, 5))


# 2 - commit

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "0 ga bo'lish mumkin emas!"


print(divide_numbers(4, 2))

# 3 - commit


def subtract_num(a, b):
    return a - b


print(subtract_num(12, 4))

# 5 - topshiriq (dastur)

import random
import string


def id_generator(length=4):
    numbers = string.digits
    random_id = ""
    for i in range(length):
        random_id += random.choice(numbers)
    return random_id


while True:
    command = input("Foydalanuvchi qo'shish: \"add\"\nDasturni to'xtatish: \"stop\": ").lower()
    if command == 'stop':
        print("Dastur to'xtadi!")
        break
    elif command == 'add':
        while True:
            name = input("Ismingizni kiriting: ").title()
            if name.isalpha():
                break

            print("Ism faqat harflardan iborat bo'lishi kerak!!!")
            continue

        while True:
            surname = input("Familiyangizni kiriting: ").title()
            if surname.isalpha():
                break

            print("Familiya faqat harflardan iborat bo'lishi kerak!!!")
            continue

        while True:
            age = input("Yoshingizni kiriting: ")
            if not age.isdigit():
                print("Yoshingizni faqat butun sonlarda kiriting!")
                continue
            else:
                age = int(age)
                break

        while True:
            phone_number = input("Telefon raqamingizni kiriting: ")
            if phone_number.startswith("+998") and len(phone_number) == 13:
                break

            print("Telefon raqam 13 xonali bo'lishi, hamda \"+998\" bilan boshlanishi kerak!!!")
            continue

        while True:
            email = input("Email manzilingizni kiriting: ")
            if '@' in email and '.' in email:
                break

            print("Emailda \"@\" va \".\" belgilari mavjud bo'lishi kerak!!!")
            continue

        while True:
            address = input("Manzilingizni kiriting: ").title()
            if address:
                break

            print("Siz manzil kiritmadingiz!!!")
            continue

        users_info = f"User: \n\nId: {id_generator()}\nIsm: {name}\nFamiliya: {surname}\nYosh: {age}\nTel:  {phone_number}\nManzil: {address}\n\n"
        with open('users_info.txt', mode='a', encoding='utf-8') as file:
            file.write(str(users_info))

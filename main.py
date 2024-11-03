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

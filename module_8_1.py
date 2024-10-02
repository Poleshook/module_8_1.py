def add_everything_up(a, b):
    #if isinstance(a, (int, float)) and isinstance(b, (int, float)):
    try:
        result = a + b
        return result
    except TypeError:
        result_2 = str(a) + str(b)
        return result_2


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
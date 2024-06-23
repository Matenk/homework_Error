def add_everything_up(a, b):
    try:
        return a + b
    except TypeError as exc:
        print(f'Невозможно сложить, ошибка {exc}')
        print(f'Осуществляем конкатенацию:')
        return str(a) + str(b)


print(add_everything_up(5, 'груша'))
print(add_everything_up(5, 10))
print(add_everything_up(5, 6.4))

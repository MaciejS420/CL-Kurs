def divide(x, y):
    if y == 0:
        raise ValueError(f'Niepoprawna wartość y: {y}')
    return x / y


try:
    result = divide(2, 0)
except ValueError as err:
    print(err)
    result = 0


print(result)



def get_input():
    return input('podaj liczbę:\n')


def show_result(result):
    print(result)


def convert(value):
    return int(value)


def handle_calculation():
    while True:
        x = get_input()

        try:
            value= convert(x)
        except ValueError:
            continue

        result = value ** 2
        show_result(result)
        break


handle_calculation()







x = [1, 2, 3, 4, 5]

x[2]

def safe_get(l, index):
    try:
        return l[index]
    except IndexError:
        return None


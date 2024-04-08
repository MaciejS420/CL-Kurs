













def is_even(number):
    return number % 2 == 0


print(is_even(4))


def iterate_through(number):
    for digit in range(1, number + 1):
        print(is_even(digit))


iterate_through(10)
 
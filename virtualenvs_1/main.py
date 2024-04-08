

def divide(a: 5, b: 10):
    if (not isinstance(a, int) and a >=0) and (not isinstance(b, int) and b < 0):
        raise TypeError(f'a and b must be integer')

    if b == 0:
        raise ValueError(f'b must be greater than 0')

    return a / b


try:
    result = divide(10, 0)
except TypeError:
    result = None
except ValueError:
    result = None

print(result)





#
def get_phone_number(number):
    phone_numbers = [997, 112, 480700]

    if number not in phone_numbers:
        raise Exception("Nie ma takiego numeru!")

    return number

print(get_phone_number(997))






c = 15
def add(a, b):
    return a + b + c

print(add(5, 10))
c = 14
print(add(5, 10))





def sentence(name):
    def full_sentence(city):
        return f"Mam na imię {name} pochodzę z {city}!"

    return full_sentence


result = sentence('Maciej')
print(result('lublin'))
print(result('warszawa'))





def outer():
    counter = 1
    def inner():
        result = counter
        counter += 1
        return 'result'
    return inner

##
##
def upper_case(fn):
    def inner(name):
        return f'Heloł {fn(name.title())}'
    return inner

def reverse(cb):
    def inner(name):
        print(reverse)
        return cb(name)[::-1]
    return inner

@reverse
@upper_case
def get_name(name):
    print(name)
    return name


@upper_case
def get_surname(name):
    return name




print(get_name('maciej'))


##

def hello(name):
    return name


print(hello('Byku'))



def html(tag, css):
    def wrapper(fn):
        def inner(name):
            style = ''
            for key, value in css.items():
                style += f'{key}: {value}<'
            return f'<{tag}>{fn(name)}</{tag}>'
        return inner
    return wrapper


@html('h1', styles)
def hello(name):
    return name


@html('p', styles)
def bye(name):
    return name





print(hello('ide na dwójke'))
print(bye('ide na dwójke'))
























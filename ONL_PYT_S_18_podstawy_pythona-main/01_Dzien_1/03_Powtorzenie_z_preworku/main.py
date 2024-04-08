import random

random_number = random.randint(1, 20)
print(random_number)

no_of_stars = random_number * '*'
print(no_of_stars)



rows = random.randint(5, 15)
columns = random.randint(5, 15)


print(f'rows: [rows], columns: [columns]')

for i in range(rows) :
    print('*' * columns)





size = random.randint(3, 9)
print(f'Size: [size]')

for row in range(1, 2):
    text = ''
    for column in range(1, size + 1):
        print(column * row * "*")

    








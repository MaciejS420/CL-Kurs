from random import randint, choice




print(randint(1, 10))



import random

print(random.randint(2, 10))




def d6(num):
    result = 0

    for i in range(num):
        result +=randint(1, 6)

    return result


print(d6(100))



















from coderslab import coderslab_welcome as yolo, words



print(yolo())





def random_word(w):
    return choice(w)


print(random_word(words))
def dogs_age(dog_age):
    global human_years
    if dog_age <= 2:
        human_years = dog_age * 10.5
    human_years = 2 * 10.5 + (dog_age - 2) * 4
    return human_years


human_years = dogs_age(6)
print("Pies na ludzkie ma lat:", human_years)

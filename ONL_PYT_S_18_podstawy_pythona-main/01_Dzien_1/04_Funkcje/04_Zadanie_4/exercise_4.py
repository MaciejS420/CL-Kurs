
# write the function from exercise 4 here -> object:
def convert_to_usd(euros):
    exchange_rate = 100/82
    return euros * exchange_rate

# the lines below will test your function:
print("385EUR = ", convert_to_usd(385), "USD")
print("100EUR = ", convert_to_usd(100), "USD")
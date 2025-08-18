# print (name)

numbers = [1, 2, 3, 4, 5]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

def is_even(number):
    return number % 2 == 0 # even?


even_numbers = list(filter(is_even, numbers))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers)

prices = [10, 20, 30, 40, 50]

price_increase = list(map(lambda price: price +  10, prices))

print(price_increase)

import modules
from sys import getsizeof
from time import perf_counter


def number_generator(list_of_numbers):
    numbers = []
    previous_number = list_of_numbers[0]
    for number in list_of_numbers:
        if previous_number < number:
            numbers.append(number)
        previous_number = number
    yield numbers


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

start = perf_counter()
print(*number_generator(src), perf_counter() - start, type(number_generator(src)), getsizeof(src))


start = perf_counter()
numbers = []
previous_number = src[0]
for number in src:
    if previous_number < number:
        numbers.append(number)
    previous_number = number
print(numbers, perf_counter() - start, type(numbers), getsizeof(numbers))

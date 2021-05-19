from sys import getsizeof
from time import perf_counter


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def no_repetitions(list_of_numbers):
    no_repeats = []
    repeats = []
    for number in list_of_numbers:
        if number in repeats:
            repeats.append(number)
        elif number in no_repeats:
            repeats.append(number)
            no_repeats.remove(number)
        else:
            no_repeats.append(number)
    yield no_repeats

start = perf_counter()
print(*no_repetitions(src), perf_counter() - start, type(no_repetitions(src)), getsizeof(no_repetitions(src)))

start = perf_counter()
no_repeats = []
repeats = []
for number in src:
    if number in repeats:
        repeats.append(number)
    elif number in no_repeats:
        repeats.append(number)
        no_repeats.remove(number)
    else:
        no_repeats.append(number)
print(no_repeats, perf_counter() - start, type(no_repeats), getsizeof(no_repeats))

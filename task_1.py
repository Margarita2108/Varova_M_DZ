def odd_number_generator(max_num):
    for odd_num in range(1, max_num+1, 2):
        yield odd_num


odd_to_7 = odd_number_generator(7)

print(type(odd_to_7))
print(next(odd_to_7))
print(next(odd_to_7))
print(next(odd_to_7))
print(next(odd_to_7))
print(*odd_to_7)
print(type(odd_number_generator(7)))



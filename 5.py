array = [147.45, 45.14, 558, 222, 254.25, 45.7, 13.55, 538.70, 1254.5, 456.1, 749, 1.2, 77]
# a
for arr in array:
    print(f'{int(arr):02d} руб {int(arr*100%100):02d} коп')
# b
print(f'{sorted(array)} список цен по возрастанию')
print(f'{array} исходный список не изменен')
# c
array_wane = (sorted(array)[::-1])
print(array_wane)
# d
print(sorted(array)[-5:])

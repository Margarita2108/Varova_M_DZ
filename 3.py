array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for arr in array:
    try:
        result = int(arr)
    except ValueError:
        print(arr, end=" ")
    else:
        if arr[0] != '+':
            mes = f'{int(arr):02d}'
            print('"', end="")
            print(mes, end="")
            print('"', end=" ")
        else:
            mes = f'+{int(arr):02d}'
            print('"', end="")
            print(mes, end="")
            print('"', end=" ")

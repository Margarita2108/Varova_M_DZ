array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
array_result = []
for arr in array:
    try:
        result = int(arr)
    except ValueError:
        array_result.append(arr)
    else:
        if arr[0] != '+':
            mes = f'{int(arr):02d}'
            array_result.append('"')
            array_result.append(mes)
            array_result.append('"')
        else:
            mes = f'+{int(arr):02d}'
            array_result.append('"')
            array_result.append(mes)
            array_result.append('"')
print(array_result)
print(" ".join(array_result))

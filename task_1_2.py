def creating_tuple(line_str):
    line = line_str.split()
    remote_addr = line[0]
    request_type = line[5][1:]
    requested_resource = line[6]
    return remote_addr, request_type, requested_resource


file_list = []
file_dict = {}

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line_str in file:
        file_list.append(creating_tuple(line_str))

for line in file_list:
    if file_dict.get(line[0]) is None:
        file_dict[line[0]] = 1
    else:
        number = file_dict.pop(line[0])
        file_dict[line[0]] = number + 1


max_request = max(file_dict.values())

for key, value in file_dict.items():
    if max_request == value:
        print(f'IP адрес спамера: {key}  количество отправленных им запросов {max_request}')

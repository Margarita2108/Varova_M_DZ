def read_by_line(files, file_index):
    with open(files, 'r', encoding='utf-8') as file:
        file.seek(file_index)
        line = file.readline()
        file_index = file.tell()
    return file_index, line


def number_rows(files):
    with open(files, 'r', encoding='utf-8') as file:
        n_line = 0
        line = file.readline()
        while line:
            line = file.readline()
            n_line = n_line+1
    return n_line


def list_from_file(user_file_1, user_file_2, user_file_3):
    numbers_line_1 = number_rows(user_file_1)
    numbers_line_2 = number_rows(user_file_2)
    numbers_line_all = 0
    index_1 = 0
    index_2 = 0
    while numbers_line_all < numbers_line_1:
        if numbers_line_all < numbers_line_2:
            txt = f'{read_by_line(user_file_1, index_1)[1][:-1]}: {read_by_line(user_file_2, index_2)[1][:-1]} \n'
            with open(user_file_3, 'a', encoding='utf-8') as f:
                f.write(txt)
            index_1 = read_by_line(user_file_1, index_1)[0]
            index_2 = read_by_line(user_file_2, index_2)[0]
            numbers_line_all = numbers_line_all + 1
        else:
            txt = f'{read_by_line(user_file_1, index_1)[1][:-1]}: {None} \n'
            with open(user_file_3, 'a', encoding='utf-8') as f:
                f.write(txt)
            index_1 = read_by_line(user_file_1, index_1)[0]
            index_2 = read_by_line(user_file_2, index_2)[0]
            numbers_line_all = numbers_line_all + 1
    if numbers_line_1 < numbers_line_2:
        return 1


def main(argv):
    result = argv
    file_1 = result[1]
    file_2 = result[2]
    file_3 = result[3]
    exit_code = list_from_file(file_1, file_2, file_3)
    if exit_code == 1:
        print(1)
    return


if __name__ == '__main__':
    import sys

    main(sys.argv)

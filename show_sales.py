def reading_file_line(first_line, past_line):
    index = 0
    numbers_line_all = 0
    while numbers_line_all < past_line:
        if numbers_line_all < first_line-1:
            index = task_3_4_5.read_by_line(file_prise, index)[0]
            numbers_line_all = numbers_line_all + 1
        else:
            with open(file_prise, 'r', encoding='utf-8') as f:
                print(task_3_4_5.read_by_line(file_prise, index)[1][:-1])
                index = task_3_4_5.read_by_line(file_prise, index)[0]
                numbers_line_all = numbers_line_all + 1


def main(argv):
    if len(argv) == 3:
        first_position = int(argv[1])
        past_position = int(argv[2])
    elif len(argv) == 2:
        first_position = int(argv[1])
        past_position = int(task_3_4_5.number_rows(file_prise))
    else:
        first_position = 0
        past_position = int(task_3_4_5.number_rows(file_prise))
    reading_file_line(first_position, past_position)
    return


file_prise = 'bakery.csv'
if __name__ == '__main__':
    import sys
    import task_3_4_5

    main(sys.argv)

def change_file_line(line, price):
    index = 0
    numbers_line_all = 1
    while numbers_line_all <= int(task_3_4_5.number_rows(file_prise)):
        if numbers_line_all == line:
            with open('temporary.csv', 'a', encoding='utf-8') as f:
                f.write(price+'\n')
                index = task_3_4_5.read_by_line(file_prise, index)[0]
                numbers_line_all = numbers_line_all + 1
        else:
            with open('temporary.csv', 'a', encoding='utf-8') as f:
                f.write(task_3_4_5.read_by_line(file_prise, index)[1])
                index = task_3_4_5.read_by_line(file_prise, index)[0]
                numbers_line_all = numbers_line_all + 1
    os.remove(file_prise)
    os.rename('temporary.csv', file_prise)


def main(argv):
    position = int(argv[1])
    new_price = argv[2]
    if position < int(task_3_4_5.number_rows(file_prise)):
        change_file_line(position, new_price)
    else:
        print('Нет такой позиции')
    return


file_prise = 'bakery.csv'
if __name__ == '__main__':
    import sys
    import os
    import task_3_4_5

    main(sys.argv)

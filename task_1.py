from itertools import zip_longest


class Matrix:
    def __init__(self, column, my_list):
        self.my_list = my_list
        self.column = column

    def __str__(self):
        numeric_index = 1
        for position in self.my_list:
            if numeric_index % self.column == 0:
                print(position)
                numeric_index += 1
            else:
                print(position, end=' ')
                numeric_index += 1
        return ''

    def __add__(self, other):
        my_list_add = [x+y for x, y in zip_longest(self.my_list, other.my_list, fillvalue=0)]
        my_matrix = Matrix(3, my_list_add)
        return my_matrix


if __name__ == '__main__':
    my_list_1 = [4, 5, 9, 6, 8, 4, 6, 7, 6, 9, 6, 5, 3]
    my_list_2 = [6, -5, -3, -7, 8, 4, 6, 2, 7, 1, 3, 2, 1, 2]
    my_matrix_1 = Matrix(3, my_list_1)
    my_matrix_2 = Matrix(3, my_list_2)
    print(my_matrix_1)
    print(my_matrix_2)
    print(my_matrix_1 + my_matrix_2)




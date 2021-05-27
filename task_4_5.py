def size_statistics(name_dir, rel_path):
    size = getsize(join(name_dir, rel_path))
    extensions = splitext(join(name_dir, rel_path))
    return size, extensions[1]


def selection_file(name_dir):
    root_dir = os.listdir(name_dir)
    list_100 = []
    list_1000 = []
    list_10000 = []
    list_100000 = []
    list_big = []
    for name in root_dir:
        for root, dirs, files in os.walk(join(name_dir, name)):
            for file in files:
                rel_path = relpath(join(root, file), name_dir)
                statistics_file = size_statistics(name_dir, rel_path)
                if statistics_file[0] < 100:
                    list_100.append(statistics_file[1])
                elif statistics_file[0] < 1000:
                    list_1000.append(statistics_file[1])
                elif statistics_file[0] < 10000:
                    list_10000.append(statistics_file[1])
                elif statistics_file[0] < 100000:
                    list_100000.append(statistics_file[1])
                else:
                    list_big.append(statistics_file[1])
    files_quantity ={}
    files_quantity[100] = (len(list_100), list(set(list_100)))
    files_quantity[1000] = (len(list_1000), list(set(list_1000)))
    files_quantity[10000] = (len(list_10000), list(set(list_10000)))
    files_quantity[100000] = (len(list_100000), list(set(list_100000)))
    files_quantity['big'] = (len(list_big), list(set(list_big)))

    with open(f'{name_dir}_summary.json', 'w+', encoding='utf-8') as f:
        f.write(str(files_quantity))
    print(files_quantity)


if __name__ == '__main__':
    import os
    from os.path import getsize, relpath, join, splitext

    name_dir = 'my_project'
    selection_file(name_dir)

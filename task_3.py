def choice_files(name_folder):
    if name_folder.find(separator) != -1:
        new_name_folder = name_folder.replace(rf'\{separator}', '')
        return new_name_folder


def create_files(new_name_file):
    new_dir = new_name_file.split('\\')[0]
    if new_dir != separator:
        try:
            os.makedirs(join(root_dir, separator, new_dir))
        except FileExistsError:
            pass


def selection_file(root_dir):
    name_dir = os.listdir(root_dir)
    for name in name_dir:
        for root, dirs, files in os.walk(join(root_dir, name)):
            for file in files:
                rel_path = relpath(os.path.join(root, file), root_dir)
                new_name_file = choice_files(rel_path)
                if new_name_file is not None:
                    create_files(new_name_file)
                    src = join(root_dir, name, separator, file)
                    dst = join(root_dir, separator, new_name_file)
                    if name != separator:
                        copy2(src, dst)


if __name__ == '__main__':
    import os
    from os.path import relpath, join
    from shutil import copy2

    separator = 'templates'
    root_dir = 'my_project'
    try:
        os.makedirs(join(root_dir, separator))
    except FileExistsError:
        print('Пака создана ранее')
    selection_file(root_dir)

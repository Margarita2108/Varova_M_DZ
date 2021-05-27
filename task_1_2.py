def search_files(name_child_folder):
    if name_child_folder.find('.') != -1:
        with open(name_child_folder, 'tw', encoding='utf-8') as f:
            pass
    else:
        os.makedirs(name_child_folder)


def create_dir(file_structure):
    with open(file_structure, 'r', encoding='utf-8') as f:
        templates = yaml.safe_load(f)
        templates = templates.split()
    new_dirs = templates[0]
    if not os.path.exists(new_dirs):
        os.makedirs(new_dirs)
    else:
        print('Такая папка уже существует')
    for child_folder in templates[1:]:
        if child_folder[:3] == '---':
            name_child_folder = join(address_2, child_folder[3:])
            search_files(name_child_folder)
        elif child_folder[:2] == '--':
            name_child_folder = join(address_1, child_folder[2:])
            address_2 = name_child_folder
            search_files(name_child_folder)
        else:
            name_child_folder = join(new_dirs, child_folder[1:])
            address_1 = name_child_folder
            search_files(name_child_folder)


if __name__ == '__main__':
    import yaml
    import os
    from os.path import join

    structure_dir = 'config.yaml'
    create_dir(structure_dir)

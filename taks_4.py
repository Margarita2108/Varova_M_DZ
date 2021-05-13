import taks_3_f
last_names = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Кирилл Алексеев", "Сергей Иванов")


def thesaurus_adv(last_name):
    """
       Assigns a key by the first letter of the last name,
       inside the dictionary by the first letter of the first name

       :param last_name: list of surname end names
       :return: dictionary of first names by last name
       """
    last_name = []
    key_last_name = {}
    for name in last_names:
        split_name = name.split()
        last_name.append(split_name[1][0])
        last_name = sorted(set(last_name))
        for key_name in last_name:
            result = []
            for name in last_names:
                split_name = name.split()
                split_name = split_name[1]
                if key_name == split_name[0]:
                    result.append(name)
                    key_last_name[key_name] = taks_3_f.thesaurus(result)
    return key_last_name


print(thesaurus_adv(last_names))

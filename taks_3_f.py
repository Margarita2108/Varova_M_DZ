def thesaurus(first_name):
    """
       Assigns a key by the first letter of the name

       :param first_name: list of names
       :return: dictionary of names
       """
    name_key = []
    key_first_name = {}
    for name in first_name:
        name_key.append(name[0])
        name_key = sorted(set(name_key))
    for key in name_key:
        result = []
        result = [idx for idx in first_name if idx.startswith(key)]
        key_first_name[key] = result
    return key_first_name

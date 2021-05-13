digits = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восем',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(digit):
    """
       Translating numbers into Russian

       :param digit: numbers in English
       :return: numbers in Russian
       """
    if digit_users.capitalize() == digit_users:
        digit_users_1 = digit_users.lower()
        if digit_users_1 in digits:
            return digits[digit_users_1].capitalize()
        else:
            return None
    else:
        if digit_users in digits:
            return digits[digit_users]
        else:
            return None


digit_users = input("Напишите числительное,которое нужно перевести:  ")
print(num_translate_adv(digit_users))

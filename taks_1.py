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


def num_translate(digit):
    """
       Translating numbers into Russian

       :param digit: numbers in English
       :return: numbers in Russian
       """
    if digit_users in digits:
        return digits[digit_users]
    else:
        return None


digit_users = input("Напишите числительное,которое нужно перевести:  ")
print(num_translate(digit_users))

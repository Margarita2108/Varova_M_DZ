from random import random, randint

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number_jokes, repeat='yes'):
    """
       Returns jokes formed from three random words
        taken from three lists

       :param number_jokes: number of jokes
       :param repeat: repeatability words
       :return: jokes
       """
    joke = 1
    noun = nouns
    adverb = adverbs
    adjective = adjectives
    while joke <= number_jokes:
        words_joke = (f'{noun[randint(0, (len(noun) - 1))]} {adverb[randint(0, (len(adverb) - 1))]}'
                      f' {adjective[randint(0, (len(adjective) - 1))]}')
        joke += 1
        print(words_joke)
        if repeat != 'yes':
            words_joke = words_joke.split()
            noun.remove(words_joke[0])
            adverb.remove(words_joke[1])
            adjective.remove(words_joke[2])
            if number_jokes > 5:
                number_jokes = 5


get_jokes(4, 'no')

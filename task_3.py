def tutors_in_klasses(tutors, klasses):
    while len(tutors) > len(klasses):
        klasses.append(None)
    tutors_klasses = zip(tutors, klasses)
    for tutor_klass in tutors_klasses:
        yield tutor_klass


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Павел', 'Ольга'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

print(*tutors_in_klasses(tutors, klasses))
print(type(tutors_in_klasses(tutors, klasses)))

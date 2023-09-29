import time
print('Привет, ты попал на викторину!\nТвоя задача набрать как можно больше баллов и получить приз!')

questions = ['Бобры или суслики?',
             'в игре cs можно простреливать стены?',
             'можно ли в игре Apex Legends отпрыгивать от стен??',
             'какой уровень максимальный в игре Genshin Impact??',
             'С помощью какого ресурса можно изучать предметы в верстаке в игре Rust??',
             'Для чего нужен опыт персонажа в игре Genshin Impact?',
             'Какая легенда может лезть по стене дольше всех в игре Apex Legends',
             'Какое самое популярное оружие в cs?',
             'В какой игре весь мир состоит из блоков?']

answers = ['суслики',
           'да',
           'да',
           '60',
           'скрап',
           'прокачка',
           'Ревенант',
           'AK',
           'майнкрафт']

score = 0

print(questions[0])
user_answer = input('Введи свой ответ: ')
if user_answer.lower() == answers[0].lower():
    score += 1
    print('Молодец ты правильно ответил!! Ты все ближе к призу))')
else:
    print('это не правильный ответ((')

time.sleep(1)

print(questions[1])
user_answer = input('Введи свой ответ: ')
if user_answer.lower() == answers[1].lower():
    score += 1
    print('Молодец ты правильно ответил!! Ты все ближе к призу))')
else:
    print('это не правильный ответ((')

time.sleep(1)

print(questions[2])
user_answer = input('Введи свой ответ: ')
if user_answer.lower() == answers[2].lower():
    score += 1
    print('Молодец ты правильно ответил!! Ты все ближе к призу))')
else:
    print('это не правильный ответ((')

time.sleep(1)

print(questions[3])
user_answer = input('Введи свой ответ: ')
if user_answer.lower() == answers[3].lower():
    score += 1
    print('Молодец ты правильно ответил!! Ты все ближе к призу))')
else:
    print('это не правильный ответ((')

time.sleep(1)

print(questions[4])
user_answer = input('Введи свой ответ: ')
if user_answer.lower() == answers[4].lower():
    score += 1
    print('Молодец ты правильно ответил!! Ты все ближе к призу))')
else:
    print('это не правильный ответ((')

time.sleep(1)

print(questions[5])
user_answer = input('Введи свой ответ: ')
if user_answer.lower() == answers[5].lower():
    score += 1
    print('Молодец ты правильно ответил!! Ты все ближе к призу))')
else:
    print('это не правильный ответ((')

time.sleep(1)

print(questions[6])
user_answer = input('Введи свой ответ: ')
if user_answer.lower() == answers[6].lower():
    score += 1
    print('Молодец ты правильно ответил!! Ты все ближе к призу))')
else:
    print('это не правильный ответ((')

time.sleep(1)

print(questions[7])
user_answer = input('Введи свой ответ: ')
if user_answer.lower() == answers[7].lower():
    score += 1
    print('Молодец ты правильно ответил!! Ты все ближе к призу))')
else:
    print('это не правильный ответ((')

time.sleep(1)

print(questions[8])
user_answer = input('Введи свой ответ: ')
if user_answer.lower() == answers[8].lower():
    score += 1
    print('Молодец ты правильно ответил!! Ты все ближе к призу))')
else:
    print('это не правильный ответ((')

print(f'Ты набрал {score} баллов из 9')

if score >= 8:
    print(' Молодец да ты геймер. У тебя 1000+ часов в доте????')
elif score >= 5:
    print('Молодец ты наверно частенько играешь, но тебе есть к чему стремиться))')
else:
    print('Ну ты пытался(((')


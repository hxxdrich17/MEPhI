from telebot import *
import random

bot = telebot.TeleBot("6264267997:AAFwOecmXSSMT3kz_72_gD8pB9D1OfYfqOg",
                      parse_mode=None)  # присваиваем API-токен библиотеке

questions = {
    'Какой у тебя рост?': ['100 - 150 см', '151 - 160 см', '161 - 170 см',
                           '171 - 180 см', '181 - 220 см'],
    'Что у тебя получается лучше всего?': ['Рисовать',
                                           'Играть на музыкальном инструменте',
                                           'Скалолазание', 'Фотографировать',
                                           'Плавать'],
    'Какая характеристика подходит тебе больше всего?': ['Артистичная(ый)',
                                                         'Решительная(ый)',
                                                         'Застенчивая(ый)',
                                                         'Уверенная(ый) в себе',
                                                         'Честная(ый)'],
    'Как предпочитаешь расслабляться?': ['За чтением книг', 'Поход в спортзал',
                                         'Пение или прослушивание музыки',
                                         'Сочинение стихов',
                                         'Поход по магазинам'],
    'Как ты относишься к учебе?': ['Мне все равно на учебу',
                                   'Стараюсь, но в жизни есть дела поважнее учебы',
                                   'Я отличница(ик) и обожаю учиться',
                                   'Учеба дается мне с трудом',
                                   'Мне без особых усилий даются все предметы'],
    'Какого цвета твои волосы?': ['Блонд', 'Шатен(ка)',
                                  'Брюнет(ка)', 'Рыжий(ий)',
                                  'Окрашены в неестественный цвет'],
    'Чего ты боишься больше всего?': ['Одиночества',
                                      'Быть некрасивой(ым), непопулярной(ым)',
                                      'Выражать свои искренние эмоции',
                                      'Что не смогу быть той(ем), кем являюсь на самом деле',
                                      'Что не смогу защитить своих близких'],
    'Какие люди тебя привлекают?': ['Веселые и открытые',
                                    'Милые и застенчивые',
                                    'Безответственные, но добрые',
                                    'Мудрые и воспитанные',
                                    'Отзывчивые и преданные'],
    'Какую черту в людях считаешь худшей?': ['Самовлюбленность', 'Ранимость',
                                             'Нерешительность', 'Скромность',
                                             'Упрямство'],
    'Какой у тебя цвет глаз?': ['Голубые', 'Черные', 'Зеленые',
                                'Серые', 'Карие']
}  # Вопросы и ответы в тесте

fairies = [['Блум', 
            'https://kartinkin.net/uploads/posts/2022-03/1646325473_62-kartinkin-net-p-blum-kartinki-65.jpg'],
           ['Стелла',
            'https://slovnet.ru/wp-content/uploads/2019/09/2-6.png'],
           ['Текна',
            'http://www.youloveit.ru/uploads/gallery/main/7/youloveit_ru_novye_oboi_s_volshebnicami__8.jpg'],
           ['Лейла',
            'https://i.pinimg.com/originals/db/f3/88/dbf388dfa85adc34cca2a664c060e954.jpg'],
           ['Муза',
            'https://vibirai.ru/image/1463573.jpg'],
           ['Флора',
            'https://slovnet.ru/wp-content/uploads/2019/09/6-7.png'],
           ['Сторми',
            'https://i.pinimg.com/originals/3c/87/93/3c879342eda0685a24cdb0b90a3684d2.jpg'],
           ['Рокси',
            'https://avatanplus.com/files/resources/original/5c05b9457995b167765bb77a.png'],
           ['Дарси',
            'http://pm1.narvii.com/8010/6cfa8ce1496e3fd14558ff51d5442bbe091ebe7ar1-1080-1069v2_uhq.jpg'],
           ['Айси',
            'https://slovnet.ru/wp-content/uploads/2019/09/4-45.jpg']]  # Результат и картинка

answers = [2, 0, 2, 4, 1, 2, 3, 0, 0, 4]  # "Правильные" ответы
# ans - переменная для поодсчёта кол-ва правильных ответов
t, ans = 0, 0  # t - переменная для перехода к следующему вопросу
flag = False  # flag - переменная boolean для активации и дизактивации опросника


# обработчик сообщений для конкретных комманд (в нашем случае старт бота)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()  # инициализируем кнопки и их тип
    markup.add(types.KeyboardButton(text='Да!'))  # добавляем кнопку
    # получаем имя пользователя (делаем первую букву заглавной)
    user_name = message.from_user.first_name[0].upper(
    ) + message.from_user.first_name[1:]
    bot.send_message(
        message.chat.id,
        f"Привет, {user_name}! Я бот, который расскажет, кто ты из феечек Винкс.Для этого нужно ответить на 10 моих вопросов. Ты готов(а)?",
        reply_markup=markup)  # приветствие


# обработчик для всех остальных сообщений
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # вводим глобальные переменные в функцию, дабы мы могли обращаться к ним и изменять их
    global t, flag, ans, answers, fairies
    if (message.text.lower() == 'да!'):  # условие, которое начинает тест
        markup = types.ReplyKeyboardMarkup()  # инициализируем кнопки и их тип
        for i in range(5):  # с помощью цикла for добавляем кнопки-ответы, обращаясь к ответам по вопросу из словаря questions
            markup.add(types.KeyboardButton(
                text=f'{questions.get(list(questions.keys())[t])[i]}'))
        # отправляем вопрос с кнопками-ответами
        bot.send_message(
            message.chat.id, f"{t+1}. {list(questions.keys())[t]}", reply_markup=markup)
        flag = True  # выставляем True (мы начали тест)
    # если тест начался и сообщение содержит ответ из словаря questions то мы продолжаем
    if (message.text in questions.get(list(questions.keys())[t]) and flag):
        # проверяет совпадает ли ответ пользователя с "правильным" ответом (сверяемся по индексу)
        if (questions.get(list(questions.keys())[t]).index(message.text) == answers[t]):
            ans += 1  # засчитываем ответ
        t += 1  # переход к следующему вопросу
        if (t == 10):  # проверяет закончились ли вопросы
            if (ans == 0):  # если пользователь набрал 0 правильных ответов, то выберем результат рандомно, чтобы его не обижать :)
                # рандомный выбор результатов
                whoami = fairies[random.randint(0, 9)]
            else:
                # если все нормально, то результат выбирается по индексу
                whoami = fairies[ans - 1]
            # отправляем фото исходя из результата
            bot.send_photo(message.chat.id, f'{whoami[1]}')
            # отправляем сообщение-результат
            bot.send_message(
                message.chat.id, f'Ого! Да ты настоящая {whoami[0]}!')
            markup = types.ReplyKeyboardMarkup()  # инициализируем кнопки
            markup.add(types.KeyboardButton(text='Да!'))  # добавляем кнопки
            markup.add(types.KeyboardButton(text='Нет. Пока!'))
            # справшиваем о возобновлении теста
            bot.send_message(
                message.chat.id, f"Хочешь начать заново?", reply_markup=markup)
            flag = False  # возвращаем переменные в исходный вид
            t, ans = 0, 0
        else:  # если вопросы не закончились то переходим к следующим
            markup = types.ReplyKeyboardMarkup()  # инициализируем кнопки
            # с помощью цикла for добавляем кнопки-ответы, обращаясь к ответам по вопросу из словаря questions
            for i in range(5):
                markup.add(types.KeyboardButton(
                    text=f'{questions.get(list(questions.keys())[t])[i]}'))
            # отправляем вопрос с кнопками-ответами
            bot.send_message(
                message.chat.id, f"{t+1}. {list(questions.keys())[t]}", reply_markup=markup)
    # проверяет хочет ли пользователь закончить
    elif ((message.text.lower() == 'нет. пока!' or message.text.lower() == 'нет') and not flag):
        markup = types.ReplyKeyboardRemove()  # убирает кнопки
        # отправляет сообщение и убирает кнопки
        bot.send_message(
            message.chat.id, "Пишите ещё! Я буду ждать Вас.", reply_markup=markup)
    # если сообщение пользователя не прошло другие условия
    elif (message.text not in questions.get(list(questions.keys())[t]) and message.text.lower() != "да!" or not flag):
        # отправляет сообщение
        bot.send_message(message.chat.id, "Простите, не могу понять Вас.")


bot.infinity_polling()  # запускает бота в бесконечный цикл
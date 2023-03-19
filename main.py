#Импорт библиотек
import time
import telebot
from telebot import types
import requests
import webbrowser

#Подключение к телеграмму
bot = telebot.TeleBot('6114337491:AAHhfiyqwsbMGs4iDJOYXbmrasEuvPc8RA8')

@bot.message_handler(commands = ['start'])
# Приветствие пользователя
def start(message):
    bot.send_message(message.from_user.id,f'Привет, {message.from_user.first_name}! Я Мап, твой персональный помощник в школьной жизни')
    time.sleep(2)
    mp = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("ГДЗ")
    btn1 = types.KeyboardButton("Справочные материалы")
    mp.add(btn, btn1)
    bot.send_message(message.from_user.id, "Выбери что хочешь сделать", reply_markup=mp)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id, "Команды: /start, /help")


@bot.message_handler(commands=['restart'])
def restart(message):
    mp = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("ГДЗ")
    btn1 = types.KeyboardButton("Справочные материалы")
    mp.add(btn, btn1)
    bot.send_message(message.from_user.id, "Выбери что хочешь сделать", reply_markup=mp)

@bot.message_handler(content_types = ['text'])
# Поиск гдз
def tem(message):

    if message.text == "ГДЗ":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("Алгебра")
        btn1 = types.KeyboardButton("Русский Язык")
        btn8 = types.KeyboardButton("Физика(вопросы)")
        btn2 = types.KeyboardButton("Физика(упражнения)")
        btn3 = types.KeyboardButton("Литература")
        btn7 = types.KeyboardButton("Литература 2 часть")
        btn4 = types.KeyboardButton("История")
        btn6 = types.KeyboardButton("История 2 часть")
        btn5 = types.KeyboardButton("Геометрия")


        markup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id,"Выбери предемет", reply_markup = markup)

#Выполнение команд
    #Поиск справочных материалов
    elif message.text == 'Справочные материалы':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = "Таблица квадратов"
        btn1 = "Таблица синусов, косинусов, тангенсов"
        markup.add(btn, btn1)
        bot.send_message(message.from_user.id,"Выбери", reply_markup = markup)

    elif message.text == "Таблица квадратов":
        bot.send_photo(message.from_user.id,
                       "https://i.pinimg.com/originals/c4/de/eb/c4deeb14d049adb026138bca4e2c9da6.png")

    elif message.text == "Таблица синусов, косинусов, тангенсов":
        bot.send_photo(message.chat.id, "https://fs01.urokimatematiki.ru/e/00136b-00a.jpg")

    #Поиск гдз по предметам
    elif message.text == "Алгебра":
        nom = bot.send_message(message.from_user.id, "Введите номер задания:")
        bot.register_next_step_handler(nom,search)


    elif message.text == "Русский Язык":
        nom = bot.send_message(message.from_user.id, "Введите номер задания:")
        bot.register_next_step_handler(nom, searchr)


    elif message.text == "Физика(вопросы)":
        nom = bot.send_message(message.from_user.id, "Введите номер задания:")
        bot.register_next_step_handler(nom, searchf)

    elif message.text == "Физика(упражнения)":
        nom = bot.send_message(message.from_user.id, "Введите номер задания:")
        bot.register_next_step_handler(nom, searchfy)

    elif message.text == "Литература 2 часть":
        nom = bot.send_message(message.from_user.id, "Введите номер задания:")
        bot.register_next_step_handler(nom, search)
        num = message.text.split()[0]
        webbrowser.open_new_tab(f"https://gdz.ru/class-9/literatura/korovina/2-prt-{num}/")

    elif message.text == "Литература":
        nom = bot.send_message(message.from_user.id, "Введите номер задания:")
        bot.register_next_step_handler(nom, search)

    elif message.text == "История":
        btn = types.KeyboardButton("Думаем, сравнимаем, размышляем")
        btn1 = types.KeyboardButton("Вопросы и задания")
        btn2 = types.KeyboardButton("Работаем с картой")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn, btn1, btn2)
        nim = 1
        if message.text == "Думаем, сравнимаем, размышляем":
            nim = 3
        elif message.text == "Работаем с картой":
            nim = 2
        nom = bot.send_message(message.from_user.id, "Введите номер задания:")
        bot.register_next_step_handler(nom, searchh)
        num = message.text.split()[0]

    elif message.text == "История 2 часть":
        btn = types.KeyboardButton("Думаем, сравнимаем, размышляем")
        btn1 = types.KeyboardButton("Вопросы и задания")
        btn2 = types.KeyboardButton("Работаем с картой")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn, btn1, btn2)

        nom = bot.send_message(message.from_user.id, "Введите номер задания:")
        bot.register_next_step_handler(nom, searchh)
        num = message.text.split()[0]

    elif message.text == "Геометрия":
        nom = bot.send_message(message.from_user.id, "Введите номер задания:")
        bot.register_next_step_handler(nom, searchg)


    # Комплимент пользователю за его остроумие
    else:
        bot.send_message(message.from_user.id, "?")

#Выполнение поиска и возврата данных с созданием ссылок
def searchh(message):
    nim = 1
    if message.text == "Думаем, сравнимаем, размышляем":
        nim = 3
    elif message.text == "Работаем с картой":
        nim = 2
    num = message.text.split()[0]
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Номер {num}",
                                         url=f"https://gdz.ru/class-9/istoriya/arsentjev/1-{nim}-item-{num}")
    markup.add(button1)
    bot.send_message(message.from_user.id, f"Упражнение {num}", reply_markup=markup)

def searchh2(message):
    nim = 1
    if message.text == "Думаем, сравнимаем, размышляем":
        nim = 3
    elif message.text == "Работаем с картой":
        nim = 2
    num = message.text.split()[0]
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Номер {num}",
                                         url=f"https://gdz.ru/class-9/istoriya/arsentjev/2-{nim}-item-{num}")
    markup.add(button1)
    bot.send_message(message.from_user.id, f"Упражнение {num}", reply_markup=markup)

def search(message):
    num = message.text.split()[0]
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Номер {num}",
                                         url=f"https://gdz.ru/class-9/algebra/kolyagin/{num}-nom/")
    markup.add(button1)
    bot.send_message(message.from_user.id, f"Упражнение {num}", reply_markup=markup)

def searchl(message):
    num = message.text.split()[0]
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Номер {num}",
                                         url=f"https://gdz.ru/class-9/literatura/korovina/1-prt-{num}/")
    markup.add(button1)
    bot.send_message(message.from_user.id, f"Упражнение {num}", reply_markup=markup)

def searchl2(message):

    num = message.text.split()[0]
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Номер {num}",
                                         url=f"https://gdz.ru/class-9/literatura/korovina/2-prt-{num}/")
    markup.add(button1)
    bot.send_message(message.from_user.id, f"Упражнение {num}", reply_markup=markup)

def searchg(message):
    num = int(message.text.split()[0])
    chap = 1
    if num < 87:
        chap = 2
    elif 87 < num < 186:
        chap = 3
    elif 186 < num < 223:
        chap = 4
    elif 223 < num < 363:
        chap = 5
    elif 363 < num < 445:
        chap = 6
    elif 445 < num < 533:
        chap = 7
    elif 533 < num < 737:
        chap = 8
    elif 737 < num < 910:
        chap = 9
    elif 910 < num < 1010:
        chap = 10
    elif 1010 < num < 1077:
        chap = 11
    elif 1077 < num < 1147:
        chap = 12
    elif 1147 < num < 1183:
        chap = 13
    elif 1183 < num < 1310:
        chap = 14
    else:
        bot.send_message("Нет такого номера")

    num = message.text.split()[0]
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Номер {num}",
                                         url=f"https://gdz.ru/class-7/geometria/atanasyan-7-9/{chap}-chapter-{num}/")
    markup.add(button1)
    bot.send_message(message.from_user.id, f"Упражнение {num}", reply_markup=markup)

def searchfy(message):
    tib = message.text.split()[0]

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Упр {tib}",
                                         url=f"https://gdz.ru/class-9/fizika/peryshkin-gutnik/{tib}-2-1/")
    markup.add(button1)
    bot.send_message(message.from_user.id, f"Упражнение {tib}", reply_markup=markup)

def searchf(message):
    tib = message.text.split()[0]

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Упр {num}",
                                         url=f"https://gdz.ru/class-9/fizika/peryshkin-gutnik/{tib}-1-1/")
    markup.add(button1)
    bot.send_message(message.from_user.id, f"Упражнение {tib}", reply_markup=markup)

def searchr(message):
    num = message.text.split()[0]
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(f"Упр {num}",
                                         url=f"https://gdz.ru/class-9/russkii_yazik/razumovskaja/nomer-{num}/")
    markup.add(button1)
    bot.send_message(message.from_user.id, f"Упражнение {num}", reply_markup=markup)


#Зацикливание бота
bot.polling(none_stop=True, interval=0)
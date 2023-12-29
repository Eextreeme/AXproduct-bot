'''
Telegram bot of AXproduct team and about project InSightWindow
'''
import telebot
from telebot import types


bot = telebot.TeleBot('6486600364:AAEhExDVIsh8LtkXmVei99m0FEEsPNYIBdg')


@bot.message_handler(commands=['start'])
def start(message):
    '''

    :param message:
    :return: procesing /start command
            Adding buttons under keyboard
    '''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)
    btn1 = types.KeyboardButton('Учасники команди')
    btn2 = types.KeyboardButton('Про проект InSightWindow')
    markup.row(btn1, btn2)

    bot.send_message(message.chat.id, 'Доброго дня, що вам цікаво про проект <b>InSightWindow</b>',
                     parse_mode='HTML', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    '''

    :param message:
    :return: Aswers on underkeyboard buttons
    '''

    if message.text == 'Учасники команди':
        command_info(message)
    elif message.text == 'Про проект InSightWindow':
        project_info(message)

    elif message.text.lower() == 'привіт':
        bot.send_message(message.chat.id, f'Привіт <b>{message.from_user.first_name} '
                                          f'{message.from_user.last_name}</b>',
                         parse_mode='HTML')
        bot.send_message(message.chat.id, '👋')
    else:
        bot.send_message(message.chat.id, f'Щось явно пішло не так...', parse_mode='HTML')
        bot.send_message(message.chat.id, '😪')
@bot.message_handler(func=lambda message: True)
def command_info(message):
    '''

    :param message:
    :return: message buttons about command
    '''
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Aрсен Павлюк: Тімлід', callback_data='pavluk_info'))
    markup.add(types.InlineKeyboardButton('Aрсен Шулак: Аналітик', callback_data='shulak_info'))
    markup.add(types.InlineKeyboardButton('Ігор Суменков: Дизайнер', callback_data='igor_info'))
    markup.add(types.InlineKeyboardButton('Роман Пилипців:  Продукт Овнер',
                                          callback_data='roman_info'))
    markup.add(types.InlineKeyboardButton('Максим Вацлав: Скрам Майстер',
                                          callback_data='waclaw_info'))
    bot.reply_to(message, 'Оберіть Учасника Команди, якого ви шукаєте', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_message(callback):
    '''
    :param callback:
    :return: fucntion which callbacks inside message
    '''
    if callback.data == 'pavluk_info':
        bot.send_message(callback.message.chat.id,' <b>Арсен Павлюк🧑‍💻</b>:', parse_mode='HTML' )
        ars = open('/Users/prabwa/Telegram-bots/AXproduct-bot/photos/Pavliuk.jpeg', 'rb')
        bot.send_photo(callback.message.chat.id, photo = ars, caption='В нашій команді є Тім Лідер,'
                                                   '\nЗнає мову C# і Python,'
                                                   ' розуміється в Arduino. Запрограмував прототип проекту'
                                                   '\n<b>Контактна інформація</b>:'
                                                   '\nЕлектронна пошта: arsenii.pavliuk.ir.2023@lpnu.ua',
                                                    parse_mode='HTML',
                                                    )

    elif callback.data == 'roman_info':
        bot.send_message(callback.message.chat.id,' <b>Роман Пилипців🧑‍💻</b>:', parse_mode='HTML')
        roma = open('/Users/prabwa/Telegram-bots/AXproduct-bot/photos/roman.jpeg', 'rb')
        bot.send_photo(callback.message.chat.id, photo = roma, caption='В нашій команді є Продукт Овнер,'
                                                   ' \nДобре знає мову Python, запрограмував цього бота.'
                                                   ' Написав текст до виступу'
                                                   '\n<b>Контактна інформація</b>:'
                                                   '\nтелеграм: @r_pylyptsiv '
                                                   '\nНомер телефону: +380995351702'
                                                   '\nЕлектронна пошта: romkapyl@gmail.com',
                                                    parse_mode='HTML',)

    elif callback.data == 'waclaw_info':
        bot.send_message(callback.message.chat.id,' <b>Максим Вацлав💪</b>:', parse_mode='HTML' )
        #ars = open('/Users/prabwa/Telegram-bots/AXproduct-bot/photos/Pavliuk.jpeg', 'rb')
        #bot.send_photo(callback.message.chat.id, photo = ars)
        bot.send_message(callback.message.chat.id, 'В нашій команді є Скрам майстер, '
                                                   '\nРозробив макет, запропонував ідею проекту'
                                                   '\n<b>Контактна інформація</b>:'
                                                   '\nтелеграм: @RowLinsee'
                                                   '\nНомер телефону: +380981731521',
                                                    parse_mode='HTML',
                                                    )
    elif callback.data == 'igor_info':
        bot.send_message(callback.message.chat.id,' <b>Ігор Суменков👨‍🎨</b>:', parse_mode='HTML')
        igor = open('/Users/prabwa/Telegram-bots/AXproduct-bot/photos/igor.jpeg', 'rb')
        bot.send_photo(callback.message.chat.id, photo = igor, caption='В нашій команді є Дизайнером'
                                                   '\nРозробив логотип, Робив презентацію'
                                                   '\n<b>Контактна інформація</b>:'
                                                   '\nтелеграм: @Ihorchu_k '
                                                   '\nНомер телефону: +380634683923  '
                                                    , parse_mode='HTML',
                                                    )

    elif callback.data == 'shulak_info':
        bot.send_message(callback.message.chat.id,' <b>Арсен Шулак👨‍🎨</b>:', parse_mode='HTML' )
        ars = open('/Users/prabwa/Telegram-bots/AXproduct-bot/photos/shulak.jpeg', 'rb')
        bot.send_photo(callback.message.chat.id, photo = ars, caption='В нашій команді є Аналітиком, '
                                                   '\nРобив презентацію, провів опитування, зробив першу версію макету'
                                                   '\n<b>Контактна інформація</b>:'
                                                   '\nЕлектронна пошта: arsen.shulak.ir.2024@lpnu.ua',
                                                    parse_mode='HTML',)

    elif callback.data == 'get_presentation':
        get_presentation(callback.message)
    elif callback.data == 'get_feedback_photo':
        get_survey(callback.message)
    elif callback.data == 'more_info':
        bot.send_message(callback.message.chat.id, 'InSightWindow')
    elif callback.data == 'Get_test':
        bot.send_message(callback.message.chat.id, 'Зараз буде...')
def project_info(message):
    '''
    :param message:
    :return: message buttons about the project InSightWindow
    '''
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Файл презентації', callback_data='get_presentation'))
    markup.add(types.InlineKeyboardButton('Отримати Відео прототипу', callback_data='Get_test'))
    markup.add(types.InlineKeyboardButton('Отримати результати опитування', callback_data='get_feedback_photo'))
    markup.add(types.InlineKeyboardButton('Детальна інформація про InSightWindow', callback_data='more_info'))
    bot.reply_to(message, 'Що вас цікавить?', reply_markup=markup)

def get_presentation(message):
    '''

    :param message:
    :return: opens presetation file
    '''
    file_path = './AXproduct_presentation.pptx'
    with open(file_path, 'rb') as file:
        bot.send_document(message.chat.id, file, caption='Ось презентація')

def get_survey(message):
    '''

    :param message:
    :return: opens survey file
    '''
    file_path = '/Users/prabwa/Telegram-bots/AXproduct-bot/photos/survey.png'
    with open(file_path, 'rb') as file:
        bot.send_photo(message.chat.id, file, caption='Ось опитування')

def get_test_video(message):
    pass

def get_project_info(message):
    bot.reply_to(message, 'InSightWindow')


bot.polling(non_stop=True)

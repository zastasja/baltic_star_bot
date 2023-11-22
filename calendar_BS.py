import os
from os.path import join, dirname
import telebot
from telebot import types
from dotenv import load_dotenv
from src.calendar import Text, Calendar


# GETTING TOKEN
def get_from_env(key):
    dotenv_path = join(dirname(__file__), "bs_token.env")
    load_dotenv(dotenv_path)
    return os.environ.get(key)


# BOT
def bs_calendar_bot():
    token = get_from_env("debug_token")
    bot = telebot.TeleBot(token, parse_mode='HTML')

    @bot.message_handler(commands=["start"])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(Text.calendar)
        btn2 = types.KeyboardButton(Text.top)
        btn3 = types.KeyboardButton(Text.whats_brevet)
        markup.add(btn1, btn2, btn3)
        bot.send_message(
            message.chat.id,
            text="Привет, {0.first_name}! Я бот велоклуба Балтийская Звезда".format(
                message.from_user
            ),
            reply_markup=markup,
        )

    @bot.message_handler(content_types=["text"])
    def func(message):
        if message.text == Text.calendar:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            december = types.KeyboardButton(Text.dec)
            january = types.KeyboardButton(Text.jan)
            february = types.KeyboardButton(Text.feb)
            march = types.KeyboardButton(Text.mar)
            april = types.KeyboardButton(Text.apr)
            may24 = types.KeyboardButton(Text.may)
            june = types.KeyboardButton(Text.jun)
            july = types.KeyboardButton(Text.jul)
            august = types.KeyboardButton(Text.aug)
            sept = types.KeyboardButton(Text.sep)
            octob = types.KeyboardButton(Text.oct)
            y = types.KeyboardButton(Text.year)
            back = types.KeyboardButton(Text.backwards)
            markup.add(december, january, february, march, april, may24, june, july, august, sept,
                       octob, y, back)
            bot.send_message(
                message.chat.id,
                text=Text.choose_month.format(message.from_user), reply_markup=markup,
            )

        elif message.text == Text.year:
            bot.send_message(
                message.chat.id, text=Text.whole_year
            )

        elif message.text == Text.dec:
            bot.send_message(message.chat.id, text=Calendar.DECEMBER)

        elif message.text == Text.jan:
            bot.send_message( message.chat.id, text=Calendar.JANUARY)

        elif message.text == Text.feb:
            bot.send_message(message.chat.id, text=Calendar.FEBRUARY)

        elif message.text == Text.mar:
            bot.send_message(message.chat.id, text=Calendar.MARCH)

        elif message.text == Text.apr:
            bot.send_message(message.chat.id, text=Calendar.APRIL)

        elif message.text == Text.may:
            bot.send_message(message.chat.id, text=Calendar.MAY)

        elif message.text == Text.jun:
            bot.send_message(message.chat.id, text=Calendar.JUNE)

        elif message.text == Text.jul:
            bot.send_message(message.chat.id, text=Calendar.JULY)

        elif message.text == Text.aug:
            bot.send_message(message.chat.id, text=Calendar.AUGUST)

        elif message.text == Text.sep:
            bot.send_message(message.chat.id, text=Calendar.SEPTEMBER)

        elif message.text == Text.oct:
            bot.send_message(message.chat.id, text=Calendar.OCTOBER)

        elif message.text.lower() in ["вы психи", "фрики", "психи"]:
            bot.send_message(
                message.chat.id, text="Отклонение от общепринятой нормы не является сумасшествием :D")

        elif message.text == Text.whats_brevet:
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton(Text.newcomers, Text.new_url)
            )
            markup.add(
                types.InlineKeyboardButton(Text.reglament, url=Text.reg_url)
            )
            bot.send_message(
                message.chat.id, text=Text.brevet_desc.format(message.from_user),
                reply_markup=markup,
            )

        elif message.text == Text.top:
            markup = types.InlineKeyboardMarkup()
            markup.add(
                types.InlineKeyboardButton(Text.top_intruction, url=Text.top_inst_url)
            )
            markup.add(
                types.InlineKeyboardButton(Text.top_site, url=Text.top_site_url)
            )
            markup.add(
                types.InlineKeyboardButton(Text.top_chat, url=Text.top_chat_url)
            )
            bot.send_message(
                message.chat.id,
                text=Text.top_decs.format(message.from_user),
                reply_markup=markup,
            )
        elif message.text == Text.backwards:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(Text.calendar)
            btn2 = types.KeyboardButton(Text.top)
            btn3 = types.KeyboardButton(Text.whats_brevet)
            markup.add(btn1, btn2, btn3)
            bot.send_message(
                message.chat.id,
                text=Text.back_main_menu.format(message.from_user),
                reply_markup=markup,
            )

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(Text.calendar)
            btn2 = types.KeyboardButton(Text.top)
            btn3 = types.KeyboardButton(Text.whats_brevet)
            markup.add(btn1, btn2, btn3)
            bot.send_message(
                message.chat.id, text=Text.dont_understand_click.format(message.from_user), reply_markup=markup,
            )

    bot.polling(none_stop=True)


if __name__ == '__main__':
    bs_calendar_bot()

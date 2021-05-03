import datetime
from time import sleep

from bot_object import bot
from database import session
from models import User
from keyboards import *
from languages import DICTIONARY


def login_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(
            message.chat.id,
            DICTIONARY['ru']['welcome_msg'].format(user.first_name),
            reply_markup=categories_inline_keyboard()
        )
    else:
        return True, 'main_menu_state'
    return False, ''


def main_menu_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(
            message.chat.id, DICTIONARY['ru']['mainmenu_msg'],
            reply_markup=get_main_menu_keyboard(language='ru'))
    else:
        if message.text == DICTIONARY['ru']['my_events_btn']:
            bot.send_message(message.chat.id, "Тут будут ивенты, на которые ты подпишешься")
            return True, 'main_menu_state'
        elif message.text == DICTIONARY['ru']['settings_btn']:
            bot.send_message(message.chat.id, "Тут будут твои настройки")
            return True, 'main_menu_state'
        else:
            bot.send_message(message.chat.id, DICTIONARY['ru']['no_button'])

    return False, ''


def set_city_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(
            message.chat.id, DICTIONARY['ru']['set_city_msg'],
            reply_markup=get_skip_keyboard(language='ru'))
    else:
        if message.text == DICTIONARY['ru']['skip_btn']:
            bot.send_message(message.chat.id, DICTIONARY['ru']['signed_up_msg'])
            return True, 'main_menu_state'
        else:
            # TODO: check if given city exists in Ukraine
            user.city = message.text
            session.commit()
            bot.send_message(message.chat.id, DICTIONARY['ru']['signed_up_msg'])
            return True, 'main_menu_state'

    return False, ''


from config import bot
from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import client_kb
from database import bot_db


async def hello(message: types.Message):
    await message.reply('Hello World')
    await bot.send_message(message.chat.id,
                           'Hello im your first bot',
                           reply_markup=client_kb.start_markup)


async def help(message: types.Message):
    await message.reply(f'Hello {message.from_user.first_name}! 😄😄😄\n'
                        f'I\'m your bot filter messages, so that\'s why be careful, '
                        f'i can ban you for curse words 😈😈😈\n'
                        f'Also i have some commands \n'
                        f'1. /quiz1 this command for hilarious quiz questions,'
                        f' quiz has continue by clicking '
                        f'button *Следующая Викторина* \n'
                        f'2. Also u can share location or info about u \n'
                        f'3. /shows U can watch collection of tvshows')


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Следующая Викторина', callback_data='button_call_1')
    markup.add(button_call_1)
    question = 'Who invented Python'
    answer = [
        'Valli',
        'Harry Potter',
        'Linus Torvalds',
        'Guido van Rossum'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='this is easy, not gonna explain',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def get_all_tvshows(message: types.Message):
    await bot_db.sql_select(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(quiz_1, commands=['quiz1'])
    dp.register_message_handler(get_all_tvshows, commands=['shows'])

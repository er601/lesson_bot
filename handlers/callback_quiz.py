from aiogram import types
from aiogram.types import ParseMode
from config import bot
from aiogram import Dispatcher


async def quiz_2(call: types.CallbackQuery):
    question = 'Who invented Linux'
    answer = [
        'Cheep',
        'Mario',
        'Linus Torvalds',
        'James Bond'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='this is easy, not gonna explain',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


def register_handlers_callback_quiz(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")

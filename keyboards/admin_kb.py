from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

upload_button = KeyboardButton('/upload')
cancel_button = KeyboardButton('/cancel')
delete_button = KeyboardButton('/delete')


admin_markup = ReplyKeyboardMarkup(resize_keyboard=True)

admin_markup.row(
    upload_button,
    cancel_button,
    delete_button
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callback_data import main_menu_callback
import emoji

grinning_cat = emoji.emojize(":grinning_cat:")
heart = emoji.emojize(":growing_heart:")

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=f"время до события x{grinning_cat}",
                              callback_data=main_menu_callback.new(type="x_time"))],
        [InlineKeyboardButton(text=f"время до события Y{grinning_cat}",
                              callback_data=main_menu_callback.new(type="y_time"))],
        [InlineKeyboardButton(text=f"Случайное сообщение{heart}",
                              callback_data=main_menu_callback.new(type="random_message"))],
        [InlineKeyboardButton(text=f"Посмотреть фотографии котят{grinning_cat}",
                              callback_data=main_menu_callback.new(type="kitty_photo"))],
        [InlineKeyboardButton(text=f"посмотреть фотографии тигров {heart}",
                              callback_data=main_menu_callback.new(type="tiger_photo"))],
        [InlineKeyboardButton(text=f"посмотреть фотографии кошек{grinning_cat}",
                              callback_data=main_menu_callback.new(type="cat_photo"))]

    ]
)

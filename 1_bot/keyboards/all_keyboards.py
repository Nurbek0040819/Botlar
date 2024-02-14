from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import DB_NAME
from utils.database import Database

db = Database(DB_NAME)

kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Categories'),
         KeyboardButton(text='Categories_1')]

    ],
    resize_keyboard=True,
    input_field_placeholder='Tugmani bosing...',
    one_time_keyboard=True
)


def get_categories() -> ReplyKeyboardMarkup:
    categories = db.get_categories()
    cats = []
    for i in categories:
        cats.append(
            KeyboardButton(text=i[1])
        )
    markup = ReplyKeyboardMarkup(
            keyboard=[cats],
            resize_keyboard=True,
            input_field_placeholder='Iltioms,quyidagi mahsulotni tanlang!',
            one_time_keyboard=True
        )
    return markup


def get_categories_1() -> ReplyKeyboardMarkup:
    categories = db.get_categories_1()
    cats = []
    for i in categories:
        cats.append(
            KeyboardButton(text=i[1])
        )
    markup = ReplyKeyboardMarkup(
            keyboard=[cats],
            resize_keyboard=True,
            input_field_placeholder='Iltioms,quyidagi mahsulotni tanlang',
            one_time_keyboard=True
        )
    return markup

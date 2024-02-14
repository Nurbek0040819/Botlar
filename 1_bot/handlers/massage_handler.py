from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import DB_NAME
from keyboards.all_keyboards import get_categories, get_categories_1, kb_start
from utils.database import Database

db = Database(DB_NAME)
massage_router = Router()


@massage_router.message(F.text == 'Categories')
async def category_button(message: Message):
    await message.answer(text="Select category, please select one ",
                         reply_markup = get_categories()
    )

@massage_router.message(F.text == 'Categories_1')
async def category_button(message: Message):
    await message.answer(text="Select category, please select one ",
                         reply_markup = get_categories_1()
    )


@massage_router.message(F.text.in_({'Smartphone', 'Notebook'}))
async def product_button(message: Message):
    cats = db.get_categories()
    for i in cats:
        if message.text == i[1]:
            products = db.get_products(i[0])
            break
    await message.answer_photo(
        photo=products[0][3],
        caption=f"<b>{products[0][1]}</b>:\nprice:{products[0][2]}$",
    )


@massage_router.message(F.text.in_({'Muzlatkich', 'Kir yuvish mashinasi'}))
async def product_button_1(message: Message):
    cats = db.get_categories_1()
    for i in cats:
        if message.text == i[1]:
            products = db.get_products_1(i[0])
            break
    await message.answer_photo(
        photo=products[0][3],
        caption=f"<b>{products[0][1]}</b>:\nprice:{products[0][2]}$",
    )
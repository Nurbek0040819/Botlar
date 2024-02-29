from typing import List, Tuple

from aiogram import Router, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from config import admins, DB_NAME
from utils.database import Database
db = Database(DB_NAME)

from utils.my_commands import user_commands, admin_commands


cmd_router = Router()


@cmd_router.message(CommandStart())
async def start_handler(message: Message):
    print(message.from_user.id)
    if message.from_user.id in admins:
        await message.bot.set_my_commands(commands=admin_commands)
        await message.answer("Dear admin, welcome!")
    else:
        await message.bot.set_my_commands(commands=user_commands)
        await message.answer("Welcome")

# @cmd_router.message(Command('asus f15'))
# async def asus_f15(message: Message):
#     products = db.get_all_products()
#     print(products)
#     if products:
#         if len(products) == 1:
#             product = products[0]
#             await message.answer_photo(
#                 photo=product[3],
#                 caption=f"<b>{product[1]}</b>\n\n<b>{product[2]}</b>\n\nPrice: {product[4]}\n\nContact: {product[-1]}"
#             )


async def send_product_info(message: Message, product: Tuple):
    try:
        await message.answer_photo(
            photo=product[3],
            caption=f"<b>{product[1]}</b>\n\n<b>{product[2]}</b>\n\nPrice: {product[4]}\n\nContact: {product[-1]}"
        )
    except:
        print(f"Error sending product info:")


async def asus_f15_handler(message: Message):
    products = db.get_all_products()  # Assuming you have a function to fetch all products from the database
    if products:
        asus_products = [product for product in products if "asus" in product[1].lower()]
        if asus_products:
            if len(asus_products) == 1:
                await send_product_info(message, asus_products[0])
            else:
                # If there are multiple Asus products, you may choose how to handle it
                await message.answer("Multiple Asus products found. Please specify which one you want.")
        else:
            await message.answer("No Asus products found.")
    else:
        await message.answer("No products available.")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(asus_f15_handler, commands=['asus_f15'])

@cmd_router.message(Command('cancel'))
async def cancel_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("All actions cancelled!")
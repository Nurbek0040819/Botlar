from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from config import DB_NAME
from keyboards.admin_inline_keyboards import categories_kb_4_products
from states.admin_states import ProductStates
from utils.database import Database

product_router = Router()
db = Database(DB_NAME)


# @product_router.message(Command('products'))
# async def product_list_handler(message: Message):
#
#     await message.answer(
#         text="All products:",
#         reply_markup=categories_kb_4_products()
#     )


@product_router.message(Command('add_product'))
async def add_product_handler(message: Message, state: FSMContext):
    await state.set_state(ProductStates.add_SelectCategoryProdState)
    await message.answer(
        text="Please choose a category which you want add product:",
        reply_markup=categories_kb_4_products()
    )


@product_router.callback_query(ProductStates.add_SelectCategoryProdState)
async def add_product_category_handler(query: CallbackQuery, state: FSMContext):
    await state.update_data(product_category=query.data)
    await state.set_state(ProductStates.add_TitleCategoryProdState)
    await query.message.answer('Please, send title for your product...')
    await query.message.delete()


@product_router.message(ProductStates.add_TitleCategoryProdState)
async def add_product_title_handler(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(product_title=message.text)
        await state.set_state(ProductStates.add_TextCategoryProdState)
        await message.answer('Please, send full description text for your product...')
    else:
        await message.answer('Please,send only text....')


@product_router.message(ProductStates.add_TextCategoryProdState)
async def add_product_text_handler(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(product_text=message.text)
        await state.set_state(ProductStates.add_ImageCategoryProdState)
        await message.answer('Please, send photo for your product...')
    else:
        await message.answer('Please,send only text....')


@product_router.message(ProductStates.add_ImageCategoryProdState)
async def add_product_image_handler(message: Message, state: FSMContext):
    if message.photo:
        await state.update_data(product_image=message.photo[-1].file_id)
        await state.set_state(ProductStates.add_PriceCategoryProdState)
        await message.answer('Please, send price for your product:')
    else:
        await message.answer('Please,send only photo...')


@product_router.message(ProductStates.add_PriceCategoryProdState)
async def add_product_price_handler(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(product_price=int(message.text))
        await state.set_state(ProductStates.add_PhoneCategoryProdState)
        await message.answer('Please, send phone number for contact with you:')
    else:
        await message.answer('Please,send only price...')


@product_router.message(ProductStates.add_PhoneCategoryProdState)
async def add_product_contact_handler(message: Message, state: FSMContext):
    if message.text or message.contact:
        phone = message.text if message.text else message.contact.phone_number
        all_data = await state.get_data()
        print(all_data)
        result = db.add_product(
            title=all_data.get('product_title'),
            text=all_data.get('product_text'),
            image=all_data.get('product_image'),
            price=all_data.get('product_price'),
            phone=phone,
            cat_id=all_data.get('product_category'),
            u_id=message.from_user.id,
        )
        if result:
            await message.answer('Your product successfully added!')
            product = db.get_my_last_product(message.from_user.id)
            await message.answer_photo(
                photo=product[3],
                caption=f"{product[1]}\n\n{product[2]}\n\nprice:{product[4]}\n\ncontact:{product[-1]}"
            )
        else:
            await message.answer('something went wrong, please try again')
        await state.clear()
    else:
        await message.answer('Please,send contact or phone number...')


# Edit product uchun funksiyalar
@product_router.message(Command('edit_product'))
async def edit_product_handler(message: Message, state: FSMContext):
    await state.set_state(ProductStates.edit_SelectCategoryProdState)
    await message.answer(
        text="Please choose a category which you want edit product:",
        reply_markup=categories_kb_4_products()
    )

@product_router.callback_query(ProductStates.edit_SelectCategoryProdState)
async def edit_product_category_handler(query: CallbackQuery, state: FSMContext):
    product = db.get_my_all_product(query.from_user.id)
    print(product)
    await state.update_data(product_category=query.data)
    await state.set_state(ProductStates.edit_TitleCategoryProdState)
    await query.message.answer('Please, send title for your edit product...')
    await query.message.delete()

@product_router.message(ProductStates.edit_TitleCategoryProdState)
async def edit_product_title_handler(message: Message, state: FSMContext):
    product = db.get_my_all_product(message.from_user.id)
    print(product)
    if message.text:
        await state.update_data(product_title=message.text)
        await state.set_state(ProductStates.edit_TextCategoryProdState)
        await message.answer('Please, send full description text for your edit product...')
    else:
        await message.answer('Please,send only text....')

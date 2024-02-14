from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from keyboards.all_keyboards import kb_start

command_router = Router()


@command_router.message(CommandStart())
async def start_tugmasi(message: Message):
    await message.answer(text="<b>Assalomu alaykum!</b>\nBotimga xush kelibsiz!",
                         reply_markup = kb_start
    )


@command_router.message(Command('help'))
async def help_tugmasi(message: Message):
    await message.answer(text="<b>Hali botim mukkammal emas!</b>")


@command_router.message(Command('new'))
async def new_tugmasi(message: Message):
    await message.answer(text="<b>Botim zor ishlashiga gap bolishi mumkin emas!</b>")





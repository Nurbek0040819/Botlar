from aiogram.types import BotCommand
from aiogram.filters import Command

admin_commands = [
    BotCommand(command='start', description='Start/restart bot'),
    BotCommand(command='categories', description='All categories list'),
    BotCommand(command='add_category', description='Add a new category'),
    BotCommand(command='edit_category', description='Update any category'),
    BotCommand(command='del_category', description='delete any category'),
    BotCommand(command='products', description='All products list'),
    BotCommand(command='add_product', description='Add a new product'),
    BotCommand(command='all_products', description='all product'),
]

user_commands = [
    BotCommand(command='start', description='Start/restart bot'),
    BotCommand(command='help', description='Manual for using bot'),
]
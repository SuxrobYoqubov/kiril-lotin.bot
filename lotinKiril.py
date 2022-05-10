import logging
from transliterate import to_cyrillic, to_latin

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5356935895:AAGfABRPh8xenPNE5Kz-kwc2DO2qRoE4z8g'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.answer("Kiril 🔁 Lotin botiga xush kelibsiz!\n\n 🟢 Kiril alifbosidan lotin alifbosiga  \n 🟢 Lotin alifbosidan kiril alifbosiga \n\nO'tkazish imkoniyati mavjud")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):

    await message.reply("Botdan foydalanish uchun so'z yuboring")



@dp.message_handler()
async def lotinKiril(message: types.Message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # bot.reply_to(message, javob(msg))
    await message.answer(javob(msg))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
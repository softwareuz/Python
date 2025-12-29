import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

# Bot tokeningiz
API_TOKEN = '' #Token
ADMIN_ID =  '' # Admin ID

# Logging yoqish
logging.basicConfig(level=logging.INFO)

# Bot va dispatcher yaratish
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher(storage=MemoryStorage())

# Foydalanuvchi tillari uchun dictionary tlni saqlashga
user_languages = {}


# Til tanlash tugmalari
def language_keyboard():
    buttons = [
        [InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang_uz")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


# Javob tugmasi yaratish Inline Button
def reply_keyboard(user_id, lang):
    if lang == "uz":
        text = "✉️ Javob yozish"
    elif lang == "ru":
        text = "✉️ Ответить"
    else:
        text = "✉️ Reply"

    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=text, callback_data=f"reply_{user_id}")]])


# /start komandasi
@dp.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("🌍 Iltimos, tilni tanlang:\n\n🌍 Пожалуйста, выберите язык:\n\n🌍 Please select a language:",
                         reply_markup=language_keyboard())


# Tilni tanlash menusi
@dp.callback_query(F.data.startswith("lang_"))
async def set_language(call: CallbackQuery):
    user_id = call.from_user.id
    lang = call.data.split("_")[1]  # lang_uz → uz

    user_languages[user_id] = lang

    if lang == "uz":
        text = "✅ Til o'zbek tiliga o'zgartirildi!\n✍️ Xabaringizni yozing."
    elif lang == "ru":
        text = "✅ Язык изменен на русский!\n✍️ Напишите ваше сообщение."
    else:
        text = "✅ Language changed to English!\n✍️ Write your message."

    await call.message.answer(text)


# Foydalanuvchi xabari adminga ga uzatish
@dp.message()
async def send_to_admin(message: Message):
    user_id = message.from_user.id
    lang = user_languages.get(user_id, "uz")

    if lang == "uz":
        text = f"📩 *Yangi xabar!*\n👤 *Foydalanuvchi:* {message.from_user.full_name} (@{message.from_user.username})\n🆔 *ID:* `{user_id}`\n\n✉️ *Xabar:*\n{message.text}"
    elif lang == "ru":
        text = f"📩 *Новое сообщение!*\n👤 *Пользователь:* {message.from_user.full_name} (@{message.from_user.username})\n🆔 *ID:* `{user_id}`\n\n✉️ *Сообщение:*\n{message.text}"
    else:
        text = f"📩 *New Message!*\n👤 *User:* {message.from_user.full_name} (@{message.from_user.username})\n🆔 *ID:* `{user_id}`\n\n✉️ *Message:*\n{message.text}"

    await bot.send_message(chat_id=ADMIN_ID, text=text, reply_markup=reply_keyboard(user_id, lang))


# Admin javob berishi
@dp.callback_query(F.data.startswith("reply_"))
async def ask_reply(call: CallbackQuery, state: FSMContext):
    user_id = int(call.data.split("_")[1])
    await state.update_data(user_id=user_id)

    await call.message.answer("✍️ Foydalanuvchiga javob yozing:")


# Admin foydalanuvchiga javob yozsa
@dp.message(F.text)
async def reply_to_user(message: Message, state: FSMContext):
    if message.chat.id == ADMIN_ID:
        data = await state.get_data()
        user_id = data.get("user_id")

        if not user_id:
            await message.answer("⚠️ Avval xabarga 'Javob berish' tugmasini bosing!")
            return

        response_text = f"📩 *Admin javobi:*\n\n{message.text}"
        await bot.send_message(chat_id=user_id, text=response_text)
        await message.answer("✅ Xabaringiz foydalanuvchiga yuborildi!")
        await state.clear()


# Botni ishga tushirish
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

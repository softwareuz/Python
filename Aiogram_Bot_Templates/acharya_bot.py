import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand, BotCommandScopeDefault, MenuButtonCommands
TOKEN =   # Bot tokenini shu yerga

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_language = {}

async def set_bot_menu():
    commands = [
        BotCommand(command="start", description="start bot"),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())

def main_menu(language):
    buttons = {
        "uz": [
            ("📌 Biz haqimizda", "about"),
            ("📑 Hujjat topshirish", "apply"),
            ("📚 Fakultetlar", "faculties"),
            ("✒️ Habar Yozish", "contact"),
            ("📞Qo'ng'iroq qiling","call_centr"),
            ("🤖Bot orqali habar yozish","robot"),
            ("👨‍💻 Dasturchi haqida", "developer"),
        ],
        "ru": [
            ("📌О нас", "about"),
            ("📑Подать документы", "apply"),
            ("📚Факультеты", "faculties"),
            ("✒️Напишите сообщение", "contact"),
            ("📞Позвонить","call_centr"),
            ("🤖Напишите сообщение через бота","robot"),
            ("👨‍💻О разработчике", "developer")
        ],
        "en": [
            ("📌About Us", "about"),
            ("📑Apply", "apply"),
            ("📚Faculties", "faculties"),
            ("✒️Send a Message", "contact"),
            ("📞Make a call","call_centr"),
            ("🤖Write a message via bot","robot"),
            ("👨‍💻 About Developer", "developer")
        ]
    }
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=data)] for text, data in buttons[language]
        ] #+ #[[InlineKeyboardButton(text="⬅️", callback_data="back")]]
    )
    return keyboard

@dp.message(F.text == "/start")
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz")],
            [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
            [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")]
        ]
    )
    await message.answer("Tilni tanlang \n Choose lang \n выберите язык:", reply_markup=keyboard)

@dp.callback_query()
async def handle_callback(call: types.CallbackQuery):
    data = call.data
    user_id = call.from_user.id

    if data.startswith("lang_"):
        language = data.split("_")[1]
        user_language[user_id] = language
        await call.message.edit_text("😊Kerakli bo‘limni tanlang⤵️\n😊Select considered section⤵️\n😊Выберите нужный раздел⤵️", reply_markup=main_menu(language))

    elif data == "faculties":
        lang = user_language.get(user_id, "uz")
        faculty_data = {
            "uz": [
                ("Kompyuter injiniringi (B.Tech)", "https://www.acharya.uz/btech/computer-science-and-engineering"),
                ("Data Science (B.Tech)", "https://www.acharya.uz/btech/data-science"),
                ("Sun'iy Intelekt(B.Tech)","https://www.acharya.uz/btech/artificial-intelligence-and-machine-learning"),
                ("Ma'lumotlar tahlili(B.Ca)","https://www.acharya.uz/bca/data-analytics"),
                ("Bulutli Hisoblash","https://www.acharya.uz/bca/cloud-computing"),
                ("Raqamli Marketing","https://www.acharya.uz/bba/digital-marketing"),
                ("UI va UX Dizayn (B.Ca)","https://www.acharya.uz/bca/ui-and-ux-design"),
            ],
            "ru": [
                ("Компьютерная инженерия (B.Tech)", "https://www.acharya.uz/ru/btech/computer-science-and-engineering"),
                ("Наука о данных (B.Tech)", "https://www.acharya.uz/ru/btech/data-science"),
                ("Искусственный интеллект (B.Tech)","https://www.acharya.uz/ru/btech/artificial-intelligence-and-machine-learning"),
                ("Аналитика данных (B.Ca)","https://www.acharya.uz/ru/bca/data-analytics"),
                ("ОБЛАЧНАЯ ОБРАБОТКА ДАННЫХ","https://www.acharya.uz/ru/bca/cloud-computing"),
                ("Цифровой маркетинг","https://www.acharya.uz/ru/bba/digital-marketing"),
                ("Ui и ux дизайн","https://www.acharya.uz/ru/bca/ui-and-ux-design"),
            ],
            "en": [
                ("Computer Science & Engineering", "https://www.acharya.uz/en/btech/computer-science-and-engineering"),
                ("Data Science", "https://www.acharya.uz/en/btech/data-science"),
                ("Artificial Intelligence","https://www.acharya.uz/en/btech/artificial-intelligence-and-machine-learning"),
                ("Data Analytics","https://www.acharya.uz/en/bca/data-analytics"),
                ("Cloud Computing","https://www.acharya.uz/en/bca/cloud-computing"),
                ("Digital Marketing","https://www.acharya.uz/en/bba/digital-marketing"),
                (" UI & UX Design","https://www.acharya.uz/en/bca/ui-and-ux-design"),

            ]
        }
        faculties_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=text, url=url)] for text, url in faculty_data[lang]
            ] + [[InlineKeyboardButton(text="⬅️", callback_data="back")]]
        )
        await call.message.edit_text("📚Fakultetlar ro‘yxati⤵️\n📚List Of Faculties⤵️\n📚Список факультетов⤵️", reply_markup=faculties_keyboard)

    elif data == "contact":
        lang = user_language.get(user_id, "uz")
        contacts = {
            "uz":[
                ("📧Elektron Pochta","https://mail.google.com/mail/?view=cm&fs=1&to=info@acharya.uz"),
                ("📱Telegram","https://t.me/acharya_support"),
                ("📍Bizning manzilimiz","https://maps.app.goo.gl/WoG5RTDuoyvD5ShTA"),
                   ],
            "ru":[
                 ("📧 Эл. почта","https://mail.google.com/mail/?view=cm&fs=1&to=info@acharya.uz"),
                 ("📱Телеграм","https://t.me/acharya_support"),
                 ("📍Наш адрес","https://maps.app.goo.gl/WoG5RTDuoyvD5ShTA"),
            ],
            "en":[
                ("📧E-mail","https://mail.google.com/mail/?view=cm&fs=1&to=info@acharya.uz"),
                ("📱Telegram","https://t.me/acharya_support"),
                ("📍Location","https://maps.app.goo.gl/WoG5RTDuoyvD5ShTA"),
            ],
        }
        contact_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=habar,url=link) if link.startswith("http") else
            InlineKeyboardButton(text=habar, callback_data=link)]
            for habar , link in contacts[lang]
           ] +[[InlineKeyboardButton(text="⬅️", callback_data="back")]]
        )

        await call.message.edit_text("☎️Aloqa uchun Malumot⤵️\n☎️Contact Details⤵️\n☎️Контактная информация⤵️", reply_markup=contact_keyboard)
    elif data == "developer":
        lang = user_language.get(user_id,"uz")
        developer = {
            "uz":[
                ("Telegram","https://t.me/axrorback"),
                ("Whatsapp","https://wa.me/998931004005"),
                ("Instagram","https://instagram.com/axrorback"),
                ("LinkeDin","https://www.linkedin.com/in/axrorbek-ibrohimjonov-aaa525351?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"),
                ("Web Sayt","https://coderboys.uz/"),
                ("Twitter","https://x.com/axrorback"),
            ],
            "en":[
                ("Telegram","https://t.me/axrorback"),
                ("WhatsApp","https://wa.me/998931004005"),
                ("Instagram","https://instagram.com/axrorback"),
                ("LinkedIn","https://www.linkedin.com/in/axrorbek-ibrohimjonov-aaa525351?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"),
                ("Web Page","https://coderboys.uz/"),
                ("Twitter","https://x.com/axrorback"),
            ],
            "ru":[
                ("Телеграм","https://t.me/axrorback"),
                ("Ватсап","https://wa.me/998931004005"),
                ("Инстаграм", "https://instagram.com/axrorback"),
                ("LinkedIn","https://www.linkedin.com/in/axrorbek-ibrohimjonov-aaa525351?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"),
                ("Веб-сайт","https://coderboys.uz/"),
                ("Твиттер","https://x.com/axrorback"),
            ]
            }
        dev_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=text,url=url)] for text , url in developer[lang]
        ]   +[[InlineKeyboardButton(text="⬅️",callback_data="back")]])
        await call.message.edit_text("👨‍💻Dasturchi kontaktlari\n👨‍💻Developer Contacts\n👨‍💻Контакты разработчиков", reply_markup=dev_keyboard)

    elif data == "about":
        lang = user_language.get(user_id, "uz")
        about_text = {
            "uz":[("📌Acharya Universiteti Haqida","https://www.acharya.uz/overview")], # Uzbekcha Link Buttonga
            "ru":[("📌Подробная информация об Acharya","https://www.acharya.uz/ru/overview")], #Ruscha Linklar
            "en":[("📌About Acharya University","https://www.acharya.uz/en/overview")],# English Button linklari
        }

        about_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=text,url=url)] for text ,url in about_text[lang]
            ] + [[InlineKeyboardButton(text="⬅️",callback_data="back")]])  # Orqaga tugmasi

        await call.message.edit_text("🎓Universitet haqida⤵️\n🎓University information⤵️\n🎓Информация об университете⤵️", reply_markup=about_keyboard)


    elif data == "apply":
        lang = user_language.get(user_id, "uz")
        apply_text = {
            "uz":[
                ("🌐Sayt orqali Hujjat Topshirish","https://www.acharya.uz/uzb_reg/"),
                ("☎️Operatorga Murojaat qiling","https://t.me/acharya_support"),
            ],
            "ru":[
                ("🌐Подача документов через сайт","https://www.acharya.uz/uzb_reg/"),
                ("☎️Свяжитесь с оператором","https://t.me/acharya_support"),
            ],
            "en":[
                ("🌐 Sending the document through the site","https://www.acharya.uz/uzb_reg/"),
                ("☎️Contact the operator","https://t.me/acharya_support"),
            ]
        }
        apply_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=text,url=url)] for text , url in apply_text[lang]
        ]   +[[InlineKeyboardButton(text="⬅️",callback_data="back")]])
        await call.message.edit_text("📄Hujjat topshirish⤵️\n📄Apply document⤵️\n📄Отправить документ⤵️", reply_markup=apply_keyboard)
    elif data == "call_centr":
        lang = user_language.get(user_id,"uz")
        telefon_habari = {
            "uz":"📞Quyidagi raqam orqali biz bilan bog'laning⤵️\n +998 55 301 00 09",
            "ru":"📞Свяжитесь с нами по номеру ниже⤵️\n +998 55 301 00 09",
            "en":"📞Contact us on the number below⤵️\n +998 55 301 00 09",
        }
        call_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⬅️", callback_data="back")]
        ])
        await call.message.edit_text(telefon_habari[lang],reply_markup=call_keyboard)
        await call.answer()
    elif data == "robot":
        lang = user_language.get(user_id,"uz")
        robot_habar = {
            "uz":"🤖Bot Habaringizni Call-Centrga uzatadi",
            "ru":"🤖Бот пересылает ваше сообщение в колл-центр",
            "en":"🤖Bot forward your Message to Call-Centr"
        }
        robot_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🤖🤖",url="https://t.me/acharyarobot")]
        ]   +[[InlineKeyboardButton(text="⬅️",callback_data="back")]])
        await call.message.edit_text(robot_habar[lang],reply_markup=robot_keyboard)
    elif data == "back":
        language = user_language.get(user_id, "uz")
        await call.message.edit_text("😊Kerakli bo‘limni tanlang⤵️\n😊Select considered section⤵️\n😊Выберите нужный раздел⤵️", reply_markup=main_menu(language))

    await call.answer()


#def back_button(language):
 #   return InlineKeyboardMarkup(
        #inline_keyboard=[[InlineKeyboardButton(text="⬅️ Ortga", callback_data="back")]]
  #  )

async def main():
    logging.basicConfig(level=logging.INFO)
    await set_bot_menu()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

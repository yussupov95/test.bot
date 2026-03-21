from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
import json
import os
from datetime import datetime

TOKEN = "vk1.a.yk6CrpiXV0IirGWRG4bKbnDkQtSssCcHNo7UuD4S938IpdCvEhRc2PosDHQmEvsQX83RtuGB4na3ycHVwUWcOxw76fgIzOaRGjsYaD96EuGaoGpZkbG10qEMjFixdcRcc9r6nIvHRwml2FUXXNqrSQsqA5A5tN0gdCeka4FsvoZZQF0lFbvdFl6ho8YeVFr_2RXKNiNy2GNgv5b3XYkHxg"

bot = Bot(token=TOKEN)

APPLICATIONS_FILE = "applications.json"
ADMIN_IDS = [609908758, 1043667113, 697274681]

user_data = {}
user_questions = {}  # {user_id: {"step": 1, "nickname": "", "question": ""}}

def get_main_menu():
    keyboard = Keyboard(one_time=False, inline=False)
    keyboard.add(Text("📝 Заявка на К/А"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("📚 Что учить для А/П"), color=KeyboardButtonColor.SECONDARY)
    keyboard.row()
    keyboard.add(Text("📋 Руководство А/П"), color=KeyboardButtonColor.SECONDARY)
    keyboard.row()
    keyboard.add(Text("📖 Кинуть заявку на А/П"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("📩 Задать вопрос руководству"), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("❓ Популярные вопросы"), color=KeyboardButtonColor.NEGATIVE)
    return keyboard

def get_study_menu():
    keyboard = Keyboard(one_time=False, inline=False)
    keyboard.row()
    keyboard.add(Text("📋 Правила и обязанности А/П "), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("📋 Требования и форма подачи заявок"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("🌐 GPS Сервера"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("⚙️ Команды сервера"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("📖 РП Термины"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("🔒 Защита игрового аккаунта"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("← Назад"), color=KeyboardButtonColor.SECONDARY)
    return keyboard

def get_faq_menu():
    keyboard = Keyboard(one_time=False, inline=False)
    keyboard.add(Text("1️⃣ Когда откроют заявки на А/П"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("2️⃣ Когда проверят анкету на К/А"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("3️⃣ Требования для поступления на А/П"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("4️⃣ Кто такой А/П"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("5️⃣ Кто такой К/А"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("6️⃣ Когда проверят заявки на Доп-баллы"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("← Назад"), color=KeyboardButtonColor.SECONDARY)
    return keyboard

@bot.on.message(text="📖 Кинуть заявку на А/П")
async def send_ap_request(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "📬 **Подача заявки на А/П**\n\n"
        "🔗 **Ссылка для подачи заявки:**\n"
        "https://forum.blackrussia.online/forums/Агенты-поддержки.3283/\n\n"
        "📌 **Важно!**\n"
        "• Заявки могут быть закрыты в любой момент\n"
        "• Ждите, пока не откроют\n"
        "• Не флудите в личные сообщения руководству\n\n"
        "Удачи с заявкой!",
        keyboard=get_main_menu()
    )

@bot.on.message(text=["Начать", "start", "начать"])
async def start_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "👋 Добро пожаловать в бот подачи заявок!\n\n"
        "Выберите нужный раздел:",
        keyboard=get_main_menu()
    )

@bot.on.message(text="❓ Популярные вопросы")
async def faq_menu_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "❓ **Популярные вопросы**\n\n"
        "Выберите интересующий вас вопрос:",
        keyboard=get_faq_menu()
    )

@bot.on.message(text="🔒 Защита игрового аккаунта")
async def account_security_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "🔒 **Защита игрового аккаунта**\n\n"
        "🔗 Подробнее о защите аккаунта:\n"
        "https://vk.com/away.php?to=https%3A%2F%2Fforum.blackrussia.online%2Fthreads%2Fgrozny-%25D0%2597%25D0%25B0%25D1%2589%25D0%25B8%25D1%2582%25D0%25B0-%25D0%25B8%25D0%25B3%25D1%2580%25D0%25BE%25D0%25B2%25D0%25BE%25D0%25B3%25D0%25BE-%25D0%25B0%25D0%25BA%25D0%25BA%25D0%25B0%25D1%2583%25D0%25BD%25D1%2582%25D0%25B0.14640664%2F&utf=1/\n\n"
        "Обязательно ознакомьтесь!",
        keyboard=get_study_menu()
    )

@bot.on.message(text="1️⃣ Когда откроют заявки на А/П")
async def q1_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "📢 **Когда откроют заявки на А/П**\n\n"
        "О точной дате открытия заявок будет сообщено дополнительно.\n"
        "Следите за объявлениями в беседе и на форуме.",
        keyboard=get_faq_menu()
    )

@bot.on.message(text="2️⃣ Когда проверят анкету на К/А")
async def q2_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "📋 **Когда проверят анкету на К/А**\n\n"
        "Анкеты проверяются в течение 1-3 рабочих дней.\n"
        "О результате вам сообщат в личные сообщения.",
        keyboard=get_faq_menu()
    )

@bot.on.message(text="3️⃣ Требования для поступления на А/П")
async def q3_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "📌 **Требования для поступления на А/П**\n\n"
        "• Возраст от 15 лет\n"
        "• Знание правил сервера и команд\n"
        "• Отсутствие серьезных нарушений\n"
        "Подробнее в разделе «Что учить для А/П».",
        keyboard=get_faq_menu()
    )

@bot.on.message(text="4️⃣ Кто такой А/П")
async def q4_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "👥 **Кто такой А/П (Агент Поддержки)**\n\n"
        "Агент поддержки — это игрок, который помогает новичкам,\n"
        "отвечает на вопросы в чате и следит за порядком.\n\n"
        "Агенты являются первым звеном поддержки игроков.",
        keyboard=get_faq_menu()
    )

@bot.on.message(text="5️⃣ Кто такой К/А")
async def q5_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "👤 **Кто такой К/А (Кандидат в Администраторы)**\n\n"
        "Кандидат — это игрок, который подал заявку на должность Администратора\n"
        "и находится на стадии обзвона.",
        keyboard=get_faq_menu()
    )

@bot.on.message(text="6️⃣ Когда проверят заявки на Доп-баллы")
async def q6_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "⭐ **Когда проверят заявки на Доп-баллы**\n\n"
        "Заявки на дополнительные баллы проверяются 1-2 раза в неделю.\n"
        "О результатах сообщается в Инфо чате.",
        keyboard=get_faq_menu()
    )

@bot.on.message(text="📚 Что учить для А/П")
async def study_menu_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "📚 **Что нужно учить для А/П**\n\n"
        "Выберите раздел:",
        keyboard=get_study_menu()
    )

@bot.on.message(text="📋 Правила и обязанности А/П")
async def agent_rules_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "📋 **Правила и обязанности Агентов Поддержки**\n\n"
        "🔗 Полезные ссылки:\n"
        "• https://forum.blackrussia.online/threads/%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-%D0%B8-%D0%BE%D0%B1%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D0%BE%D0%B2-%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B8.6310504/ "
        "Ознакомьтесь с обязанностями!",
        keyboard=get_study_menu()
    )

@bot.on.message(text="📋 Требования и форма подачи заявок")
async def requirements_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "📋 **Требования и форма подачи заявок**\n\n"
        "🔗 Требования:\n"
        "• https://forum.blackrussia.online/threads/%D0%A2%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%B8-%D1%84%D0%BE%D1%80%D0%BC%D0%B0-%D0%BF%D0%BE%D0%B4%D0%B0%D1%87%D0%B8-%D0%B7%D0%B0%D1%8F%D0%B2%D0%BA%D0%B8-%D0%BD%D0%B0-%D0%B4%D0%BE%D0%BB%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D1%8C-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D0%B0-%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D0%B8.7835388/",        
        "Заполняйте строго по форме!",
        keyboard=get_study_menu()
    )

@bot.on.message(text="🌐 GPS Сервера")
async def gps_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "🌐 **GPS Сервера**\n\n"
        "🔗 Координаты и карта:\n"
        "• https://vk.com/away.php?to=https%3A%2F%2Fforum.blackrussia.online%2Fthreads%2Fgrozny-gps-%25D0%25A1%25D0%25B5%25D1%2580%25D0%25B2%25D0%25B5%25D1%2580%25D0%25B0.14641258%2F&utf=1",
        "Запомните ключевые точки!",
        keyboard=get_study_menu()
    )

@bot.on.message(text="⚙️ Команды сервера")
async def commands_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "⚙️ **Команды сервера**\n\n"
        "🔗 Список команд:\n"
        "• https://vk.com/away.php?to=https%3A%2F%2Fforum.blackrussia.online%2Fthreads%2Fgrozny-%25D0%259E%25D0%25B1%25D1%2589%25D0%25B8%25D0%25B9-%25D1%2581%25D0%25BF%25D0%25B8%25D1%2581%25D0%25BE%25D0%25BA-%25D0%25BA%25D0%25BE%25D0%25BC%25D0%25B0%25D0%25BD%25D0%25B4-%25D1%2581%25D0%25B5%25D1%2580%25D0%25B2%25D0%25B5%25D1%2580%25D0%25B0.14641215%2F&utf=1",
        "Основные команды нужно знать наизусть!",
        keyboard=get_study_menu()
    )    


@bot.on.message(text="📖 РП Термины")
async def rp_terms_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "📖 **РП Термины**\n\n"
        "🔗 Словарь терминов:\n"
        "• https://vk.com/away.php?to=https%3A%2F%2Fforum.blackrussia.online%2Fthreads%2Fgrozny-roleplay-%25D1%2582%25D0%25B5%25D1%2580%25D0%25BC%25D0%25B8%25D0%25BD%25D1%258B.14641299%2F&utf=1",
        keyboard=get_study_menu()
    )

@bot.on.message(text="📋 Общий список команд сервера")
async def all_commands_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "📋 **Общий список команд сервера**\n\n"
        "🔗 Полный список:\n"
        "• https://vk.com/away.php?to=https%3A%2F%2Fforum.blackrussia.online%2Fthreads%2Fgrozny-%25D0%259E%25D0%25B1%25D1%2589%25D0%25B8%25D0%25B9-%25D1%2581%25D0%25BF%25D0%25B8%25D1%2581%25D0%25BE%25D0%25BA-%25D0%25BA%25D0%25BE%25D0%25BC%25D0%25B0%25D0%25BD%25D0%25B4-%25D1%2581%25D0%25B5%25D1%2580%25D0%25B2%25D0%25B5%25D1%2580%25D0%25B0.14641215%2F&utf=1",
        "Держите под рукой!",
        keyboard=get_study_menu()
    )

@bot.on.message(text="📋 Руководство А/П")
async def admin_guide_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    
    await message.answer(
        "📋 **Руководство Администрации/Помощников**\n\n"
        "👤 **Куратор хелперов**\n"
        "• @povelitel_helperov\n\n"
        "👤 **Зам. Куратора хелперов**\n"
        "• @myrbkvv001\n\n"
        "👤 **Ст. След. за хелперами**\n"
        "• @papochka_sheyh\n\n"
        "👤 **След. за хелперами**\n"
        "• @phoenixki\n\n"
        "👤 **След. за хелперами**\n"
        "• @mkaratovich\n\n"
        "По всем вопросам обращайтесь к указанным лицам.",
        keyboard=get_main_menu()
    )

@bot.on.message(text="← Назад")
async def back_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    await message.answer(
        "Главное меню:",
        keyboard=get_main_menu()
    )

@bot.on.message(text="📝 Заявка на К/А")
async def zayavka_start(message: Message):
    if message.from_id != message.peer_id:
        return
    
    user_id = message.from_id
    user_data[user_id] = {"step": 1, "answers": []}
    
    cancel_keyboard = Keyboard(one_time=False, inline=False)
    cancel_keyboard.add(Text("❌ Отменить заявку"), color=KeyboardButtonColor.SECONDARY)
    
    await message.answer(
        "📝 **Заявка на К/А**\n\n"
        "Шаг 1 из 6\n\n"
        "Введите ваш **Nickname**:",
        keyboard=cancel_keyboard
    )

@bot.on.message()
async def zayavka_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    
    user_id = message.from_id
    
    # Если пользователь не в процессе заявки - выходим
    if user_id not in user_data:
        return
    
    text = message.text.strip()
    
    # Кнопка отмены
    if text == "❌ Отменить заявку":
        del user_data[user_id]
        await message.answer(
            "❌ Заявка отменена. Возвращаю в главное меню.",
            keyboard=get_main_menu()
        )
        return
    
    step = user_data[user_id]["step"]
    
    # Клавиатура с отменой для всех шагов
    cancel_keyboard = Keyboard(one_time=False, inline=False)
    cancel_keyboard.add(Text("❌ Отменить заявку"), color=KeyboardButtonColor.SECONDARY)
    
    if step == 1:
        user_data[user_id]["answers"].append(f"Nickname: {text}")
        user_data[user_id]["step"] = 2
        await message.answer(
            "Шаг 2 из 6\n\nОтправьте **скриншот /hstats**:",
            keyboard=cancel_keyboard
        )
    
    elif step == 2:
        if message.attachments and message.attachments[0].photo:
            photo = message.attachments[0].photo
            photo_url = photo.sizes[-1].url
            user_data[user_id]["answers"].append(f"Скриншот /hstats: {photo_url}")
            user_data[user_id]["step"] = 3
            await message.answer(
                "Шаг 3 из 6\n\nВведите ваш **Возраст**:",
                keyboard=cancel_keyboard
            )
        else:
            await message.answer(
                "❌ Пожалуйста, отправьте скриншот /hstats ",
                keyboard=cancel_keyboard
            )
    
    elif step == 3:
        user_data[user_id]["answers"].append(f"Возраст: {text}")
        user_data[user_id]["step"] = 4
        await message.answer(
            "Шаг 4 из 6\n\nСколько у вас **зеленых/синих клеток** в таблице?",
            keyboard=cancel_keyboard
        )
    
    elif step == 4:
        user_data[user_id]["answers"].append(f"Клетки: {text}")
        user_data[user_id]["step"] = 5
        await message.answer(
            "Шаг 5 из 6\n\nПолучали ли вы **наказание на посту**? (Да/Нет)",
            keyboard=cancel_keyboard
        )
    
    elif step == 5:
        user_data[user_id]["answers"].append(f"Наказание: {text}")
        user_data[user_id]["step"] = 6
        await message.answer(
            "Шаг 6 из 6\n\nПрисутствовали ли вы хотя бы на **одном собрании**? (Да/Нет)",
            keyboard=cancel_keyboard
        )
    
    elif step == 6:
        user_data[user_id]["answers"].append(f"Собрание: {text}")
        
        result = "✅ **Новая заявка на К/А**\n\n"
        for ans in user_data[user_id]["answers"]:
            result += f"• {ans}\n"
        
        # Отправка всем админам
        for admin_id in ADMIN_IDS:
            try:
                await bot.api.messages.send(
                    peer_id=admin_id,
                    message=result,
                    random_id=0
                )
            except:
                print(f"Не удалось отправить админу {admin_id}")
        
        await message.answer(
            "✅ **Заявка отправлена!**\n\n"
            "Скоро с вами свяжутся.",
            keyboard=get_main_menu()
        )
        
        del user_data[user_id]

@bot.on.message(text="📩 Задать вопрос руководству")
async def ask_question_start(message: Message):
    if message.from_id != message.peer_id:
        return
    
    user_id = message.from_id
    user_questions[user_id] = {"step": 1, "nickname": "", "question": ""}
    
    await message.answer(
        "📩 **Задать вопрос руководству**\n\n"
        "Шаг 1 из 2\n\n"
        "Введите ваш **NickName**:"
    )

@bot.on.message()
async def question_handler(message: Message):
    if message.from_id != message.peer_id:
        return
    
    user_id = message.from_id
    if user_id not in user_questions:
        return
    
    text = message.text.strip()
    step = user_questions[user_id]["step"]
    
    if step == 1:
        user_questions[user_id]["nickname"] = text
        user_questions[user_id]["step"] = 2
        await message.answer(
            "Шаг 2 из 2\n\n"
            "Напишите ваш **вопрос**:"
        )
    
    elif step == 2:
        user_questions[user_id]["question"] = text
        
        nickname = user_questions[user_id]["nickname"]
        question = user_questions[user_id]["question"]
        
        result = f"📩 **Новый вопрос от игрока**\n\n"
        result += f"👤 **NickName:** {nickname}\n"
        result += f"🆔 **ID:** {user_id}\n"
        result += f"❓ **Вопрос:** {question}\n\n"
        result += f"🔗 Профиль: https://vk.com/id{user_id}"
        
        # Отправляем всем админам
        for admin_id in ADMIN_IDS:
            try:
                await bot.api.messages.send(
                    peer_id=admin_id,
                    message=result,
                    random_id=0
                )
            except:
                print(f"Не удалось отправить админу {admin_id}")
        
        await message.answer(
            "✅ **Ваш вопрос отправлен!**\n\n"
            "Руководство ответит вам в ближайшее время.",
            keyboard=get_main_menu()
        )
        
        del user_questions[user_id]
        
        
if __name__ == "__main__":
    print("✅ Бот запущен")
    bot.run_forever()           

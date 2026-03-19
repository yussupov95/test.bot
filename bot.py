from vkbottle.bot import Bot, Message

TOKEN = "vk1.a.dj9taykSWx_H0bWtjU1U4V1XpqP1ALZEGggvt4nMltvLP6dj1XQ-NReHSSx-fbWd8SWA54CrKUGMmvPGAdbTe-wtMKGDJDATJnLnrte523MeA8iGKB4BV4Dkgvm5zZMJlx9tcYF-TqOw4_VeowZjGMJ9Kzc4emidfmD-FT97JYN-_Ezxbav_TiHOu8I_8aqLqeHdVWiPhFlezpxzzJmIvg"

bot = Bot(token=TOKEN)

@bot.on.message()
async def handler(message: Message):
    await message.answer("✅ Бот работает!")

if __name__ == "__main__":
    print("✅ Бот запущен")
    bot.run_forever()

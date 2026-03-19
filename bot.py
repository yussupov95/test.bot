from vkbottle.bot import Bot, Message

TOKEN = "vk1.a.DGzfRe7hrfmAZOc6ltV4CHYSU1fWY9jaPLkT66oRPTz_NZqzpu2aT6XKfKKubBDZX_1ujYWy1F1n7bguLHvRsaL-YRTkYYR1FbkwheRjprJbJeQG1oMg8V-3aVaZ81plv_WMhMzS7wOCOyIRRRgqxlFFdm0gRJmN0jazvJho0UEJJgcfCdG8ssDtfqe_JiVx8vUnWt9UDhf4lCH66ndSSg"

bot = Bot(token=TOKEN)

@bot.on.message()
async def handler(message: Message):
    await message.answer("✅ Бот работает!")

if __name__ == "__main__":
    print("✅ Бот запущен")
    bot.run_forever()

import asyncio
from handlers import client
from aiogram import Bot, Dispatcher
from config import tg_API
from aiogram.fsm.storage.memory import MemoryStorage

bot = ""


async def main():
    global bot
    bot = Bot(token=tg_API)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(client.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from handlers import client
from aiogram import Bot, Dispatcher
from config import tg_API


async def main():
    bot = Bot(token=tg_API)
    dp = Dispatcher()

    dp.include_router(client.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

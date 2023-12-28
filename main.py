import asyncio
from handlers import client
from aiogram import Bot, Dispatcher
from config import tg_API
from aiogram.fsm.storage.memory import MemoryStorage
from schedule_check import schedule_do


async def main():
    bot = Bot(token=tg_API)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(client.router)

    await bot.delete_webhook(drop_pending_updates=True)

    # Use asyncio.gather to run dp.start_polling(bot) and check_now concurrently
    await asyncio.gather(
        dp.start_polling(bot),
        schedule_do.check_now(bot)
    )

if __name__ == "__main__":
    asyncio.run(main())

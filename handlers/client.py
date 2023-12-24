from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from db_control import db
from msg_buttons import user_keyboard
import pack_mgr

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    # if db.check_is_user_exists(message.from_user.id):
    #     await message.answer("Вижу Вы уже имели едло с этим ботом, тогда продолжим")
    # else:
    #     await message.answer(
    #         "Привет!\n"
    #         "Этот бот поможет вам отслеживать посылки ПОЧТА РОССИИ\n"
    #         "Воспользуйтесь командой /add чтобы доабвить посылку в лист",
    #         reply_markup=user_keyboard.generate_usermenu_kb()
    #     )

    await message.answer(
            "Привет!\n"
            "Этот бот поможет вам отслеживать посылки ПОЧТА РОССИИ\n"
            "Воспользуйтесь командой /add чтобы доабвить посылку в лист",
            reply_markup=user_keyboard.generate_usermenu_kb()
        )


@router.message()
async def answer_yes(message: Message):
    pass


@router.callback_query()
async def more_info(callback: CallbackQuery):
    await callback.answer(text="Function in Develop", show_alert=True)

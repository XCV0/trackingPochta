from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from db_control import db
from msg_buttons import user_keyboard
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import pack_mgr

router = Router()


class AddPackage(StatesGroup):
    get_track_number = State()
    get_name = State()


@router.message(Command("start"))
async def cmd_start(message: Message):
    if db.check_is_user_exists(message.from_user.id):
        await message.answer("Вижу Вы уже имели едло с этим ботом, тогда продолжим")
    else:
        await message.answer(
            "Привет!\n"
            "Этот бот поможет вам отслеживать посылки ПОЧТА РОССИИ\n"
            "Воспользуйтесь командой /add чтобы доабвить посылку в лист",
            reply_markup=user_keyboard.generate_usermenu_kb()
        )

    # await message.answer(
    #         "Привет!\n"
    #         "Этот бот поможет вам отслеживать посылки ПОЧТА РОССИИ\n"
    #         "Воспользуйтесь командой /add чтобы доабвить посылку в лист",
    #         reply_markup=user_keyboard.generate_usermenu_kb()
    #     )\


@router.message(StateFilter(None), Command("add"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Хорошо, введите трек-номер посылки")

    await state.set_state(AddPackage.get_track_number)


@router.message(StateFilter(AddPackage.get_track_number))
async def get_track_numb(message: Message, state: FSMContext):
    await state.update_data(get_track_number=message.text)

    await message.answer("Хорошо, теперь введите название для посылки")
    await state.set_state(AddPackage.get_name)


@router.message(StateFilter(AddPackage.get_name))
async def get_track_numb(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f"{user_data['get_track_number']}, {message.text}")
    db.add_schedule_check(message.from_user.id, user_data['get_track_number'], message.text)
    await state.clear()


@router.callback_query()
async def more_info(callback: CallbackQuery):
    await callback.answer(text="Function in Develop", show_alert=True)

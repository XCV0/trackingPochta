import schedule
from pack_mgr import get_status
from db_control import db
from datetime import datetime
from ..main import bot


async def check_now():
    all_parcels = db.get_all_parcels()[0]
    for package_number in all_parcels:
        data = get_status.check_track_number(package_number)

        if datetime.fromisoformat(data['date']) > datetime.fromisoformat(db.get_last_package_date(package_number)):
            await bot.send_message(db.get_tg_id(package_number),
                                   f"ОБНОВЛЕНИЕ СТАТУСА ДЛЯ ПОСЫЛКИ {db.get_name_package(package_number)}\n"
                                   f"НОВЫЙ СТАТУС:")

schedule.every(10).seconds.do(check_now())

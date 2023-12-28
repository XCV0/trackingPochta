import asyncio
import time

from pack_mgr import get_status
from db_control import db
from datetime import datetime


async def check_now(bot):
    while True:
        print("check now function started working!")
        all_parcels = db.get_all_parcels()[0]
        for package_number in all_parcels:
            data = get_status.check_track_number(package_number)

            if datetime.fromisoformat(data['date']) > datetime.fromisoformat(db.get_last_package_date(package_number)[0]):
                await bot.send_message(db.get_tg_id(package_number),
                                       f"ОБНОВЛЕНИЕ СТАТУСА ДЛЯ ПОСЫЛКИ {db.get_name_package(package_number)}\n"
                                       f"НОВЫЙ СТАТУС: {data['cityName']}, {data['humanStatus']}\n"
                                       f"index: {data['index']}\n")
        time.sleep(10)



# def check_every_ten_seconds(bot):
#     print("timer was started")
#
#     schedule.every(10).seconds.do(lambda: asyncio.run(check_now(bot)))

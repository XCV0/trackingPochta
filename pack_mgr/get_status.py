import requests
import json
from config import user_agent

# track_numb = str(input()) # Я ЕБАЛ ЭТО СТРОКУ БЛЯТЬ ИЗ-ЗА НЕЁ Я ПРОЕБАЛ СТОЛЬКО НЕРВОВ


def check_track_number(track_number):
    resp_generate = "https://www.pochta.ru/api/tracking/api/v1/trackings/by-barcodes?language=ru&track-numbers=" + str(track_number)
    resp = requests.get(url=resp_generate,
                        data={
                            "language": "ru",
                            "track-numbers": track_number
                        },
                        headers={
                            'User-Agent': user_agent
                        }
                        )

    # print(resp.text)

    json_data = json.loads(resp.text)

    tracking_info = json_data["detailedTrackings"][0]

    history_item = tracking_info["trackingItem"]["trackingHistoryItemList"][0]

    # Printing the extracted information
    # print("Date:", history_item["date"])
    # print("Human Status:", history_item["humanStatus"])
    # print("Operation Type:", history_item["operationType"])
    # print("Operation Attribute:", history_item["operationAttr"])
    # print("Country ID:", history_item["countryId"])
    # print("Index:", history_item["index"])
    # print("City Name:", history_item["cityName"])
    # print("Country Name:", history_item["countryName"])
    # print("Country Name Genitive Case:", history_item["countryNameGenitiveCase"])
    # print("Country Custom Name:", history_item["countryCustomName"])
    # print("Description:", history_item["description"])
    # print("Weight:", history_item["weight"])
    # print("Is In International Tracking:", history_item["isInInternationalTracking"])

    return history_item

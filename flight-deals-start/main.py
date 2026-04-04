#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from pprint import pprint
from datetime import datetime as dt
import datetime




url = "https://api.sheety.co/76c41cb17dd9d9bb3b61c30e3e3646ab/flightDeals/prices"

# get data from sheety
response = requests.get(url=url)
# print(response.json())
sheet_data = response.json()["prices"]
print(sheet_data)
# check if there are missing IATA codes and update
for row in sheet_data:
    if row["iataCode"] == "":
        new_flight_code = FlightSearch().find_iata(row["city"])
        row["iataCode"] = new_flight_code
        row_id = row["id"]
        new_data = {"price": row}
        DataManager().update_iata(row_id, new_data)

# for row in sheet_data:
#     new_price = FlightData().get_price(row['iataCode'])
#     print(new_price)
#     row_id = row["id"]
#     DataManager().update_price(row_id=row_id, new_price=new_price)
#     if empty update price:
#     if "lowestPrice" :
#         DataManager.update_price(row_id, new_price)
#
#     else int(row["lowestPrice"]) > new_price:
#         DataManager.update_price(row_id, new_price)
#
#
#     print(f"{row['iataCode']}: {lowest_price}")
#
# for item in FlightData().get_price("SYD"):
#     pprint(item["price"])
#     pprint(item[])
# pprint(FlightData().get_price("SYD"))
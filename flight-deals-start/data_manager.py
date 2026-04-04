import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def update_iata(self, row_id, new_data):
        url = f"https://api.sheety.co/76c41cb17dd9d9bb3b61c30e3e3646ab/flightDeals/prices/{row_id}"
        body = new_data

        response = requests.put(url=url, json=body)
        # print(response.status_code)

    def update_price(self, row_id, new_price):
        url = f"https://api.sheety.co/76c41cb17dd9d9bb3b61c30e3e3646ab/flightDeals/prices/{row_id}"
        body = new_price

        response = requests.put(url=url, json=body)
        print(response.status_code)

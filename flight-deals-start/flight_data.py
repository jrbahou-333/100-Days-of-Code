import requests
from datetime import datetime as dt
import datetime

class FlightData:
    #This class is responsible for structuring the flight data.

    def get_price(self, destination):
        url = "https://api.tequila.kiwi.com/v2/search?"

        header = {
            "apikey": "-ItuvYsOBjljjYLhI_HRLnxZ9sbBnZ6l"
        }
        # get from and to dates into str format
        date_from = dt.now().strftime("%d/%m/%Y")
        date_to = (dt.now() + datetime.timedelta(days=30)).strftime("%d/%m/%Y")

        params = {
            "fly_from": "LON",
            "fly_to": destination,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to" : 14,
            "curr": "GBP"
        }

        response = requests.get(url=url, headers=header, params=params)
        return(response.json()["data"][0]["price"])
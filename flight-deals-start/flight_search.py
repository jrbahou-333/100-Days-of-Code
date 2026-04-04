import requests

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def find_iata(self, city):
        url = "https://tequila-api.kiwi.com/locations/query"

        header = {
            "apikey": "-ItuvYsOBjljjYLhI_HRLnxZ9sbBnZ6l"
        }

        params = {
            "term": city
        }

        response = requests.get(url=url, headers=header, params=params)

        return(response.json()["locations"][0]["code"])
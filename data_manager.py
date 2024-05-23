import requests
from pprint import pprint
    #This class is responsible for talking to the Google Sheet.
#https://api.sheety.co/529693899f2b9bd9b382fc5033e6471f/flightDeals/prices
SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/135c73bb2df90f8e5f6daa40caa5b6e6/flightDeals/prices'



class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode'],
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)



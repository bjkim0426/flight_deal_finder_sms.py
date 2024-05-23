import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'
TEQUILA_API_KEY = ''

class FlightSearch:

   def get_destination_code(self, city_name):
      header = {
         'apikey':TEQUILA_API_KEY
      }
      parameters = {
         'term': city_name,
         'location_types': 'city'
      }
      response = requests.get(
         url=f'{TEQUILA_ENDPOINT}/locations/query',
         params=parameters,
         headers=header
      )
      results = response.json()['locations']
      code = results[0]['code']
      return code

   def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
      header = {
         'apikey': TEQUILA_API_KEY
      }
      parameters = {
         'fly_from': origin_city_code,
         'fly_to': destination_city_code,
         'date_from': from_time.strftime('%d/%m/%Y'),
         'date_to': to_time.strftime('%d/%m/%Y'),
         "nights_in_dst_from": 7,
         "nights_in_dst_to": 28,
         "flight_type": "round",
         "one_for_city": 1,
         "max_stopovers": 0,
         "curr": "GBP"
      }

      response = requests.get(
         url=f'{TEQUILA_ENDPOINT}/search',
         params=parameters,
         headers=header
      )

      try:
         data = response.json(['data'][0])

      except IndexError:
         print(f'No flights found for {destination_city_code}')
         return None

      flight_data = FlightData(
         price=data['price'],
         origin_city=data['route'][0]['cityFrom'],
         origin_airport=data['route'][0]['flyFrom'],
         desination_city=data['route'][0]['cityTo'],
         destination_airport=data['route'][0]['flyTo'],
         out_date=data['route'][0]['local_departure'].split('T')[0],
         return_date=data['route'][1]['local_departure'].split('T')[0]
      )

      print(f'{flight_data.destination_city}: £{flight_data.price}')
      return flight_data





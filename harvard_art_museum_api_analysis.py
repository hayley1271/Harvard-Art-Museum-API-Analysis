"""Harvard Art Museum API Analysis

Requesting an API request key at this url:
https://github.com/harvardartmuseums/api-docs

Fetching the names and birth places of all British persons listed in the API.
"""

import requests

# we're looking for British artists
query = {'q':'culture:British', 'apikey':'293f59f0-85f9-11ea-a384-115b2a99fd07'}
url = 'https://api.harvardartmuseums.org/person'
response = requests.get(url, params=query) 
response.ok # should return True

data = response.json()
data # calling this will return the info in a dictionary

# extracting records from data dictionary into list raw_data 
raw_data = data['records']
fetch = {}
# prints dictionary where key is artist name and value is birth place
for i in raw_data:
  fetch[i['displayname']]=i['birthplace']
print(fetch)

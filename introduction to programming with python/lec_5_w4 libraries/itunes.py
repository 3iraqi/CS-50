import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("End:")

term=sys.argv[1]
limit=5
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={limit}&term={term}")

# print(json.dumps(response.json(), indent=2))

o =response.json()

for result in o["results"]:
    print(result["trackName"])
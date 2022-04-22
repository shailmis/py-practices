
import requests
import json

r = requests.get("https://formulae.brew.sh/api/formula.json")

out_json = r.json()
total_packages = len(out_json)
print(total_packages)

out_json_s = json.dumps(out_json[0], indent=2)
#print(out_json_s)

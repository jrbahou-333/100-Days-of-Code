import requests
import json

url = "https://www.planit.org.uk/api/applics/json"

params = {
    "start_date": "2023-10-20",
    "end_date": "2023-10-26",
    "pg_sz": 100,
    "app_size": "Large"
}

response = requests.get(url, params=params)
raw_data = response.json()["records"]

print(raw_data[0].get("address"))
app_list = []
field_list = ["area_name", "address", "app_state", "app_type", "description", "url", "app_size"]

for item in raw_data:
    new_dict = {}
    for field in field_list:
        new_dict[field] = item[field]
    app_list.append(new_dict)



with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(app_list, f, ensure_ascii=False, indent=4)

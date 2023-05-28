import json
json_data = '{"key1": "value1", "key2": "value2", "key3": "value3"}'
data = json.loads(json_data)
for key, value in data.items():
    print(key, value)
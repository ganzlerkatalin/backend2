
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print(type(x))
print(x.get("name"))

# convert into JSON:
#y = json.dumps(x)

"cars" = [
{
    "price": 1549,
    "passengerQty": 4,
    "currency": "EUR",
    "type": "Kia",
    "transmission": "manual",
    "passengers": [
            "Gabor",
            "Andras",
            "Timea",
            "Martin",
            "Miklos"
]
},
{"price": 1954,
"passengerQty": 5,
"currency": "EUR",
"type": "Suzuki",
"transmission": "manual",
"passengers": [
"Gabor",
"Andras",
"Timea",
"Martin",
"Miklos"
]
},
{"price": 2544,
"passengerQty": 5,
"currency": "USD",
"type": "Opel",
"transmission": "manual",

"passengers": [
"Gabor",
"Andras",
"Timea",
"Martin",
"Miklos"
]
},
{"price": 2544,
"passengerQty": 2,
"currency": "USD",
"type": "Opel",
"transmission": "manual",

"passengers": [
"Gabor",
"Timea",
"Miklos"
]
},
{"price": 9542,
"passengerQty": 4,
"currency": "USD",
"type": "Ford",
"transmission": "automatic",
"passengers": [
"Gabor",
"Timea",
"Miklos"
]
},
]

print(type(cars))
#for key, value in cars.iteritems()
#   print key, value
#print(cars.get("type"))
#print(cars("type"))

# the result is a JSON string:
print(cars)
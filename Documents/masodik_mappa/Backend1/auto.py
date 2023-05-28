#Python Házi feladat - Nested loops -
#2.Feladat Kigyűjteni azon autók típusát ahol az utasok száma túl nagy 
cars = [
    {"price": 1549,
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
    }
]

#print(cars)
print("Python Házi feladat -Nested loops -2.Feladat")
for index in range(0, len(cars)):
   # print(cars[index]['passengerQty'],cars[index]['passengers'])
    if (len(cars[index]['passengers']) > cars[index]['passengerQty']):
        print(cars[index]['type'],"típusú autóban túl sok az utas")
#  print(cars[index]['passengerQty'],cars[index]['passengers'])
#  print(cars[index]['price'],cars[index]['passengerQty'],cars[index]['currency'],cars[index]['type'], cars[index]['transmission'],cars[index]['passengers'])   
#print(cars[0]['price'],cars[0]['passengerQty'],cars[0]['currency'],cars[0]['type'], cars[0]['transmission'],cars[0]['passengers'])

print("\nPython Házi feladat -Nested loops -3.Feladat")
#3.Feladat - Átváltani az autók árát euróból usd-be - kiírni autó nevét, árát
for index in range(0, len(cars)):
       print(cars[index]['price'],cars[index]['currency'],cars[index]['type'])
       if (cars[index]['currency'] == 'EUR'):
         cars[index]['price']=(cars[index]['price'])*1.08
         cars[index]['currency'] = 'USD'
  
print("\nEUR USD-re váltás után")          
for index in range(0, len(cars)):
       print(cars[index]['price'],cars[index]['currency'],cars[index]['type'])

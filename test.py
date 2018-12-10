import requests
while True:
    license_plate = input("Enter license plate: ")

    r = requests.get(url='http://apis.is/car?number=' + license_plate)
    car = r.json()
    car = car["results"][0]
    print(car["type"])
    print(car["subType"])
    print(car)

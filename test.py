import urllib.request
import json


while True:
    try:
        license_plate = input("Enter license plate (q to quit): ").lower()
        if license_plate == "q":
            continue
        else:
            with urllib.request.urlopen("http://apis.is/car?number=" + license_plate) as url:
                car = json.loads(url.read())
            car = car["results"][0]
            print(car)
            print(car["type"].split()[0].capitalize())
            print(car["subType"].capitalize())
            print(car["number"])
    except Exception as e:
        print(e)

car_1 = {
    "Make" : "Subaru",
    "Model": "22B STI",
    "Year" : 1998,
    "Price" : None,
    "Owned" : False,
    "Colors" : ["Blue", "White", "Red"]
}


car_2 = {
    "Make" : "Lucid",
    "Model" : "Air",
    "Year" : 2024,
    "Price" : float(68000),
    "Owned" : True,
    "Colors" : ["Black", "White", "Silver"]
}

favorite_cars = [car_1, car_2]


if favorite_cars == []:
    print("This list is empty")
    print("Lets add some items to thje list")


elif favorite_cars[0]["Make"] == "Subaru":
    print("This is a Subaru")


else:
    print("This list is not empty")
    print(favorite_cars[0]["Make"]+" " + favorite_cars[0]["Model"] + " is my favorite car")

code = 200
match code:
    case 404:
        print("Page not found")
    case 401:
        print("Unauthorized access") 
    case 403:
        print("Forbidden access")
    case 301:
        print("Page moved permanently")
    case 200:
        print("Page found")
# from classes.my_classes import Car



# my_car2 = Car(make="Ford", model="Bronco", year="2021", mileage="30000", color="Grey", condition="New")
# print(my_car2.__dict__)

from classes.my_classes import Car
my_car = Car(make="Jeep", model="Wagoneer", year=2024, mileage=3000, color="Grey", condition="New")
my_car.start()
my_car.accelerate(20)
my_car.accelerate(30)
my_car.stop()

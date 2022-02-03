car = {"Brand": "Martin", "Model": "Anton", "Year": 2018}
print(car)
for auto in car:
    print(f"The key is {auto} and the value is {car.get(auto)}")


for vehicle in car.items():
    print(vehicle)


for mobil in car.values():
    print(mobil)
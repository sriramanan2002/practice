cars = {"car1": "Mercedes", "car2": "BMW", "car3": "Audi", "car4": "Honda", "car5": "Ferrari"}

#Popping last element

print(cars)
cars.popitem()
print(cars)

#Updating new elemnts

cars.update({"car6":"Tesla"})
print(cars)

#printing the dictionary as list

cars_list1 = [*cars.keys()]
cars_list2 = [*cars.values()]
print(cars_list1 + cars_list2)
class Vehicle():
    has_wheel = True
    runs_on_fuel  =True

    def honk(self): #note the self argument is mandatory for method to attach itself to class. Similar to a constructor
        print("Honk! Honk!")

class Car(Vehicle):
    number_of_wheels = 4

class Train(Vehicle):
    number_of_wheels = 108

vehicle = Vehicle()
print("Object: vehicle\n", "-"*15)
print("A vehicle has wheel:", vehicle.has_wheel)
vehicle.honk()

car = Car()
print("Object: car\n", "-"*15)
print("A car has wheel:", car.runs_on_fuel)
print("Number of wheels:", car.number_of_wheels)
car.honk()

train = Train()
print("Object: train\n", "-"*15)
print("A train has wheel:", train.runs_on_fuel)
print("Number of wheels:", train.number_of_wheels)
train.honk()

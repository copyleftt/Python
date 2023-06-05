class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self, name):
        print(f"{name} издает звук: {self.sound}")

# Дочерний класс, наследующий от Animal
class Cat(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def purr(self):
        print(f"{self.name} мурлычет")

# Дочерний класс, наследующий от Animal
class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

    def bark(self):
        print(f"{self.name} лает")

# Создание объектов
cat = Cat("Кошка", "Мяу", "Рыжий")
dog = Dog("Собака", "Гав", "Лабрадор")

cat.purr()

cat.make_sound("Lambda")

cat.name

dog.breed

dog.bark()



class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
class HybridCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 1.5
        self.gas_tank_size = 10
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def describe_gas_tank(self):
        print(f"This car has a {self.gas_tank_size}-gallon gas tank.")
    def get_range(self):
        if self.battery_size == 1.5:
            range = 20
        elif self.battery_size == 2.0:
            range = 25
        print(f"This car can go about {range} miles on a full charge and a full tank of gas.")
 # Создание объектов
my_tesla = ElectricCar('tesla', 'model s', 2021)
my_hybrid = HybridCar('toyota', 'prius', 2022)
 # Вызов методов объектов
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.get_range()
print(my_hybrid.get_descriptive_name())
my_hybrid.describe_battery()
my_hybrid.describe_gas_tank()
my_hybrid.get_range()
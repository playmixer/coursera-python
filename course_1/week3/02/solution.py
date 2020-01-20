import os
import csv

        
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        if self.get_photo_file_ext() not in ['.jpeg', '.jpg', '.png', '.gif']:
            raise
        if brand:
            self.brand = brand
        else:
            raise
        if float(carrying) == False:
            raise
        if float(carrying) < 0:
            raise
        self.carrying = float(carrying)        
                
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        if int(passenger_seats_count) <= 0:
            raise
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        try:
            l, w, h = list(map(lambda x: float(x), body_whl.split("x")))
        except:
            l, w, h = 0.0, 0.0, 0.0
        if l < 0 or w < 0 or h < 0:
            l, w, h = 0.0, 0.0, 0.0
        self.body_length = l
        self.body_width = w
        self.body_height = h
        
    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__( brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        if extra == '':
            raise
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            try:
                if row[0] not in ['car', 'truck', 'spec_machine']:
                    raise
                
                car_type = row[0]
                brand = row[1]
                passenger_seats_count = row[2]
                photo_file_name = row[3]
                body_whl = row[4]
                carrying = row[5]
                extra = row[6]
                
                if car_type == "car":
                    car = Car(brand, photo_file_name, carrying, passenger_seats_count)
                elif car_type == "truck":
                    car = Truck(brand, photo_file_name, carrying, body_whl)
                elif car_type == "spec_machine":
                    car = SpecMachine(brand, photo_file_name, carrying, extra)                    
                
                car_list.append(car)
            except:
                pass
                
    return car_list


def test():
    cars = get_car_list('f:/cars.csv')
    return cars
        

def test1():
    cars = get_car_list('f:/cars1.csv')
    return cars
        
# Total tests: 84. Tests failed: 2, Errors: 0. Total time: 0.246.
# Failed test - test_21.
#  E   ValueError: could not convert string to float:

# During handling of the above exception, another exception occurred:
# E   AssertionError: Тест 21.1. Вызов функции get_car_list на файле, содержащем только не валидные данные, вызывает исключение ValueError.
#     assert False


# Total tests: 84. Tests failed: 2, Errors: 0. Total time: 0.250.
# Failed test - test_21.
#  E   ValueError: invalid literal for int() with base 10: ''

# During handling of the above exception, another exception occurred:
# E   AssertionError: Тест 21.1. Вызов функции get_car_list на файле, содержащем только не валидные данные, вызывает исключение ValueError.
#     assert False
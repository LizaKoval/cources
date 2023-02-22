class Car:
    color: str  # цвет
    count_passenger_seats: int  # количество пассажирских мест
    is_baby_seat: bool  # наличие десткого кресла
    is_busy: bool  # что-то
    def __init__(self, clr, count_ps, babysit, is_busy=False):
        self.color = clr
        self.count_passenger_seats = count_ps
        self.is_baby_seat = babysit
        self.is_busy = is_busy
    def __str__(self):
        return f'\nЦвет: {self.color}\n' \
               f'количество пассажирских мест:  {self.count_passenger_seats}\n' \
               f'наличие десткого кресла: {self.is_baby_seat}\n' \
               f'свободно: {self.is_busy}'

class Taxi():
    cars: list[Car]

    def __init__(self, cars):
        self.cars = cars

    def find_car(self, count_p, is_baby):
        for i in self.cars:
            if i.count_passenger_seats == count_p and i.is_baby_seat == is_baby and i.is_busy==False:
                return i




w_ford = Car('white',5, False)
b_ford = Car('black',4, True)
y_toyota = Car('yellow', 3, False)
print(w_ford)

cars = [w_ford, b_ford, y_toyota]
taxi = Taxi(cars)
print(taxi.find_car(3, False))




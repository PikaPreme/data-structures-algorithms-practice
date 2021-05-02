class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color


if __name__ == '__main__':
    my_car = Car('Toyota', '2020', 'Silver')
    moms_car = Car('Toyota', '2000', 'White')

    moms_car = Car('Toyota', '2021', 'Black')

    print(moms_car.get_model())
    print(moms_car.get_year())
    print(moms_car.get_color())

    print('I drive a {} {} {}'.format(my_car.get_color(), my_car.get_year(), my_car.get_model()))
    my_car.set_color('Red')
    print('I drive a {} {} {}'.format(my_car.get_color(), my_car.get_year(), my_car.get_model()))


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.food = cuisine_type

    def describe_restaurant(self):
        print('The name of the restaurant is ' + self.name.title() + '.'
              + '\nThe type of restaurant is ' + self.food.title() + '.')

    def open_restaurant(self):
        print(self.name.title() + ' IS OPEN.')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        self.flavours = ['vanilla', 'butterscotch', 'chocolate', 'strawberry']
        super().__init__(restaurant_name, cuisine_type)

    def display(self):
        print("The ice cream flavours available are :-\n" + str(self.flavours))


restaurant = IceCreamStand('cabana', 'italian')
restaurant.display()

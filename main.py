class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.food = cuisine_type

    def describe_restaurant(self):
        print('The name of the restaurant is ' + self.name.title() + '.'
              + '\nThe type of restaurant is ' + self.food.title() + '.')

    def open_restaurant(self):
        print(self.name.title() + ' IS OPEN.')

restaurant = Restaurant('Cabana', 'Mexican')
restaurant.describe_restaurant()
restaurant.open_restaurant()

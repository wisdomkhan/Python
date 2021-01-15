class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.food = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('The name of the restaurant is ' + self.name.title() + '.'
              + '\nThe type of restaurant is ' + self.food.title() + '.')

    def open_restaurant(self):
        print(self.name.title() + ' IS OPEN.')


p = 'yes'
while p != 'no':
    restaurant = Restaurant(input('Enter name of restaurant\t'), input('Enter type of food served\t'))
    restaurant.number_served = input('Enter no of customers served\t')
    restaurant.describe_restaurant()
    print("The no of customers served is " + restaurant.number_served + '.')
    p = input('\nWould you like to use me?\t')

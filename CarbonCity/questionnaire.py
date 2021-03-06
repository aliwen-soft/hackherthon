
print("""Hello ''! Welcome to Carbon City, 
where citizens strive each day to make more sustainable choices
 and reduce their carbon footprint""")
print("To help us calculate your carbon footprint, please answer the following questions:")

class Person:
    def __init__(self, name, username, password, location, diet, energy_consumption, shopper_type):
        self.name = name
        self.username = username
        self.password = password
        self.location = location
        self.diet = diet
        self.energy_consumption = energy_consumption
        self.shopper_type = shopper_type

# user creates account before questionnaire is presented
# mock login system with username and password assumed correct
    def login(self, username, password):
        correct = True
        while correct:
            username - input()

    def welcome(self):
        print("Hello " + self.name + ". Welcome to Carbon City.")

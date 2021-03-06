
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
    def login(self, username, password):
    """mock login system with username and password assumed correct"""
        correct = True
        while correct:
            self.username = input("Username:")
            if password == self.password:
                result = Hello " + self.name + ". Welcome to Carbon City!"
            else:
                result = "Password is incorrect."
    return result

    def welcome(self):
        print("Hello " + self.name + ". Welcome to Carbon City.")

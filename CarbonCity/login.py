
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
            if self.username == input("Username:"):
                 result1 = True
            else:
                result1 = False

            if self.password == input("Password:"):
                result2 = True
            else:
                    result2 = False
            if result1 != result 2:
                result = "Username or password is incorrect."
            else:
                result = Hello " + self.name + ". Welcome to Carbon City!"            
        return result

    def welcome(self):
        print("Hello " + self.name + ". Welcome to Carbon City.")

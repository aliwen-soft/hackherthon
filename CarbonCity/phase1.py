
class Person:
    def __init__(self, name, username, password, status, location, diet, energy_consumption, shopper_type):
        self.name = name
        self.username = username
        self.password = password
        self.status = status
        self.location = location
        self.diet = diet
        self.energy_consumption = energy_consumption
        self.shopper_type = shopper_type

# user creates account before questionnaire is presented
    def login(self, username, password):
        """mock login system with username and password assumed correct"""
        if self.username != input("Username:"):
                result1 = False
            
        if self.password != input("Password:"):
            result2 = False
              
        if result1 or result 2 == False:
            result = "Username or password is incorrect."
        else:
            result = Hello " + self.name + ". Welcome to Carbon City!"            
        return result

    def firstintro(self):
        if self.status == new:
            print("Hello " + self.name + """! Welcome to Carbon City, 
            where citizens strive each day to make more sustainable choices 
            and reduce their carbon footprint""")
            print("To help us calculate your carbon footprint, please answer the following questions:")

    def questionnaire(self):
        # Q1
        answer1 = input("""How would you best describe your diet? 
        \na. Meat in every meal \nb. Meat in most meals \nc. Vegeterian \nd. Vegan 
        \nAnswer: """)
        if answer1 == "a":
            cf1 = 10            # cf stans for carbon footprint factor 1
        elif answer1 == "b":
            cf1 = 7
        elif answer1 == "c":
            cf1 = 4
        else:
            cf1 = 3
        answer1 = self.diet
        # Q2
        answer2 = input("""In a week, how much food do you spend from retaurants and takeaways? 
        \na. £0 \nb. £1 - £10 \nc. £10 - £50 \nd. More than £50 
        \nAnswer: """)
        if answer2 == "a":
            cf2 = 0
        elif answer2 == "b":
            cf2 = 5
        elif answer2 == "c":
            cf2 = 7
        else:
            cf2 = 10
        answer2 = self.shopper_type
        return ((cf1 + cf2)/20)*100 %





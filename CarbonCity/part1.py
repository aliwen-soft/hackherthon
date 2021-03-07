# created class of type person so then can define people using 
class Person:
    def __init__(self, name, username, password, location):
        self.name = name
        self.username = username
        self.password = password
        self.location = location
        
# register function, array of people

# user creates account before questionnaire is presented
def login(self, person):
    #lower case p as getting attribute from the argument
    """mock login system with username and password assumed correct"""
    if person.username != input("Username: "):
            result1 = False
        
    if person.password != input("Password: "):
        result2 = False
            
    if result1 or result2 == False:
        result = "Username or password is incorrect."
    else:
        result = "Hello " + person.name + ". Welcome to Carbon City!"         
    return result

def firstintro(self, person):
    print("Hello " + person.name + """! Welcome to Carbon City, 
        where citizens strive each day to make more sustainable choices 
        and reduce their carbon footprint""")
    print("To help us calculate your carbon footprint, please answer the following questions:")

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

def main():
# dictates how things are run
    person1 = Person("Dan", "Dan97", "Pass", "Happy", "Here", "Seafood". "High", "Holic")
    login(person1)
    print("Hello World!") 
    firstintro()


# says run main function if file name is main
# not indented as you want it to always run
if __name__ == "__main__": 
    main()
    


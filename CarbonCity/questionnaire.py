# made an attempt at using classes

# created class of type person so then can define people using 

#class Person:
    #'''a class that stores data for each user'''
    #def __init__(self, name, username, password, location):
        #'''set instance variables'''
        #self.name = name
        #self.username = username
        #self.password = password
        #self.location = location
        
# register function, array of people

# user creates account before questionnaire is presented
def login(name, username, password):
    #lower case p as getting attribute from the argument
    """mock login system with username and password assumed correct"""
    if username != input("Username: "):
        result1 = "incorrect"
        
    if password != input("Password: "):
        result2 = "incorrect"
            
    if result1 or result2 == "incorrect":
        result = "Username or password is incorrect."
    else:
        result = "Hello " + name + ". Welcome to Carbon City!"         
    return result

def firstintro(name):
    '''introduces new user to the app and takes them through the questionnaire'''
    print("Hello " + name + """! Welcome to Carbon City, 
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
    carbonfp = ((cf1 + cf2)/20)*100
    goal_cf = carbonfp * 0.25
    return '''Thank you for completing the questionnaire. Your current carbon footprint is 
    ''' + str(carbonfp) + "% and your target carbon footprint is " + str(goal_cf) +"%."

#def main():
# dictates how things are run
    #person1 = Person("Dan", "Dan97", "Pass", "London")
    #login(person1)
    ##firstintro()


# says run main function if file name is main
# not indented as you want it to always run
#if __name__ == "__main__": 
    #main()
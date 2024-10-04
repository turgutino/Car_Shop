import json


def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            return data['users'], data['cars']
    except FileNotFoundError:
        return {1:{"username":"1","password":"","balance":20000,"mycars":[]},2:{"username":"Elsad","password":"elsad123","balance":8000,"mycars":[]}}, \
               {1:{"name":"Prius","year":2006,"price":8000,"count":6},2:{"name":"Cruze","year":2013,"price":15000,"count":4},3:{"name":"Corolla","year":2009,"price":11000,"count":2}}


def save_data(users, cars):
    data = {'users': users, 'cars': cars}
    with open('data.json', 'w') as file:
        json.dump(data, file)

users, cars = load_data()

def AdminPanel():
    
    def AddCar():
        ID = input("Enter ID: ")
        if ID in cars:
            print("This ID already exists in the database. Please enter another ID.")
            AddCar()
        else:
            Name = input("Enter car name: ")
            Year = int(input("Enter car year: "))
            Price = float(input("Enter car price: "))
            Count = int(input("Enter car count: "))
            cars[ID] = {"name": Name, "year": Year, "price": Price, "count": Count}
            save_data(users, cars)
            print("Car successfully added to the database!")
            
    def DeleteCar():
        ID = input("Enter the ID: ")
        if ID in cars:
            del(cars[ID])
            save_data(users, cars)
        else:
            print("This ID does not exist in the database.")
    
    def UpdateCar():
        ID = input("Enter the ID: ")
        if ID in cars:
            choice = input("""
1 -> Name
2 -> Price
3 -> Count 
Select what you want to update: """)
            if choice == "1":
                new_name = input("Enter the new name: ")
                cars[ID]["name"] = new_name
            
            if choice == "2":
                new_price = float(input("Enter the new price: "))
                cars[ID]["price"] = new_price
             
            if choice == "3":
                new_count = int(input("Enter the new count: "))
                cars[ID]["count"] = new_count
            save_data(users, cars)
        else:
            print("This ID does not exist in the database. Please enter a new one.")
            UpdateCar()
    
    def SearchCar(ID):
        if ID in cars:
            print(f"<><><>{ID}<><><>")
            print("Name:", cars[ID]["name"])
            print("Year:", cars[ID]["year"])
            print("Price:", cars[ID]["price"])
            print("Count:", cars[ID]["count"])
        else:
            print("No car with this ID exists in the database.")
    
    def ShowCars():
        for i in cars:
            SearchCar(i)

    select = input("""
1 -> Show Cars
2 -> Search Car
3 -> Add Car
4 -> Update Car
5 -> Delete Car
6 -> Exit

Select: """)
    
    if select == "1":
        ShowCars()
    elif select == "2":
        ID = input("Enter the ID: ")
        SearchCar(ID)
    elif select == "3":
        AddCar()
    elif select == "4":
        UpdateCar()
    elif select == "5":
        DeleteCar()
    elif select == "6":
        return 0
    else:
        print("Invalid selection.")
        
    AdminPanel()

def UserPanel(username, password):
    
    def ViewCars():
        for i in cars:
            print(f"<><><>{i}<><><>")
            print("Name:", cars[i]["name"])
            print("Year:", cars[i]["year"])
            print("Price:", cars[i]["price"])
            print("Count:", cars[i]["count"])
        
        UserPanel(username, password)
    
    def SearchCar():
        choice = input("""
1 -> Name
2 -> Year
3 -> Price                     

What would you like to search by: """)
        
        if choice == "1":
            name = input("Enter the car name: ").lower()
            found = False 
            for i in cars:
                if cars[i]["name"].lower() == name:
                    found = True
                    print(f"<><><>{i}<><><>")
                    print("Name:", cars[i]["name"])
                    print("Year:", cars[i]["year"])
                    print("Price:", cars[i]["price"])
                    print("Count:", cars[i]["count"])
            
            if not found:
                print("No car with this name exists in the database.")
                                
        if choice == "2":
            year = int(input("Enter the car year: "))
            found = False     
            for i in cars:
                if cars[i]["year"] == year:
                    found = True
                    print(f"<><><>{i}<><><>")
                    print("Name:", cars[i]["name"])
                    print("Year:", cars[i]["year"])
                    print("Price:", cars[i]["price"])
                    print("Count:", cars[i]["count"])
            if not found:
                print("No car with this year exists in the database.")

        if choice == "3":
            price = int(input("Enter the car price: "))
            found = False     
            for i in cars:
                if cars[i]["price"] == price:
                    found = True
                    print(f"<><><>{i}<><><>")
                    print("Name:", cars[i]["name"])
                    print("Year:", cars[i]["year"])
                    print("Price:", cars[i]["price"])
                    print("Count:", cars[i]["count"])
            if not found:
                print("No car with this price exists in the database.")

        UserPanel(username, password)
    
    def BuyCar():
        for i in cars:
            print(f"<><><>{i}<><><>")
            print("Name:", cars[i]["name"])
            print("Year:", cars[i]["year"])
            print("Price:", cars[i]["price"])
            print("Count:", cars[i]["count"])
                    
        car_choice = input("Enter the ID of the car you want to buy: ")
        if car_choice in cars:
            quantity = int(input("Enter the quantity of cars you want to buy: "))
            if quantity > cars[car_choice]["count"]:
                print("There are not enough cars in the database.")
                UserPanel(username, password)
            else:
                for i in users:
                    if username == users[i]["username"]:
                       if cars[car_choice]["price"] * quantity > users[i]["balance"]:
                           print("You do not have enough balance.")
                           UserPanel(username, password)
                       else:
                           print("Car successfully purchased!")
                           users[i]["balance"] -= cars[car_choice]["price"] * quantity
                           cars[car_choice]["count"] -= quantity
                           users[i]["mycars"].append(cars[car_choice]["name"])
                           
                           save_data(users, cars)
                           UserPanel(username, password)
        else:
            print("No car with this ID exists in the database.")
            UserPanel(username, password)

    def AddBalance():
        balance = int(input("Enter the amount you want to add: "))
        for i in users:
             if username == users[i]["username"]:
                 users[i]["balance"] += balance
                 save_data(users, cars)
                 print("Balance added.")
                 UserPanel(username, password)

    def ViewPersonalInfo():
        print(f"Username: {username}")
        print(f"Password: {password}")
        for i in users:
            if username == users[i]["username"]:
                print("Balance:", users[i]["balance"])
        for i in users:
            if username == users[i]["username"]:
                print("My cars:", users[i]["mycars"])
        UserPanel(username, password)

    select = input("""
1 -> View all cars
2 -> Search car
3 -> Buy car
4 -> Add balance
5 -> View personal information                  

Make your selection: """)
    
    if select == "1":
        ViewCars()
    elif select == "2":
        SearchCar()
    elif select == "3":
        BuyCar()
    elif select == "4":
        AddBalance()
    elif select == "5":
        ViewPersonalInfo()
    else:
        print("Invalid selection.")

def Login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "" and password == "":
        AdminPanel()
    else:
        found = False
        for i in users:
            if username == users[i]["username"]:
                found = True
                if password == users[i]["password"]:
                    UserPanel(username, password)
                else:
                    print("Incorrect password.")
        if not found:
            print("Incorrect username.")
            
Login()

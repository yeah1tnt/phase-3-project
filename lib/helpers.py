from db.models import User, Dictionary, GameData

##### Add user if user aren't in system
def addUser_0(session, user_input):
    name = user_input.lower()
    print("\nDo you want to register this username?")
    print("\nEnter 'yes' to register")
    print("Enter 'no' to exit")
    user_input = input("Enter your choice: ")
    while user_input:
        if user_input.lower() == "yes":
            print("How old are you?")
            age = input("\nEnter your age: ")
            user = User(name=name, age=age, level=1)
            session.add(user)
            session.commit()
            print(f"\nSucessfully registered {name}!")
            break
        elif user_input.lower() == "no":
            print("\nExitting program")
            exit()
        else:
            print("\nInvalid input. Please try again")


#####

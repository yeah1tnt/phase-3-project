from db.models import User, Dictionary, GameData

##### Add user if user aren't in system
def addUser_0(session, user_input):
    name = user_input.lower()
    print("\nDo you want to register this username?")
    print("\nEnter 'yes' to register")
    print("Enter 'no' to exit")
    
    while user_input:
        user_choice = input("Enter your choice: ")
        if user_choice.lower() == "yes":
            print("How old are you?")
            age = input("\nEnter your age: ")
            user = User(name=name, age=age, level=1)
            session.add(user)
            session.commit()
            game = GameData(user_id=user.id, game_session=0, high_score=0, total_score=0)
            session.add(game)
            session.commit()
            print(f"\nSucessfully registered {name}!")
            break
        elif user_choice.lower() == "no":
            print("\nExitting program")
            exit()
        else:
            print("\nInvalid input. Please try again")


##### User settings functions
def userAccess_01a(session):
    # user_list = [user.name for user in session.query(User).all()]
    # score_list = [game.total_score for game in session.query(GameData).all()]
    # print("\nUser list: ", user_list)
    # print("Score list: ", score_list)
    users = session.query(User).all()
    games = session.query(GameData).all()
    print("Here are the users and their scores:")
    for user in users:
        for game in games:
            if user.id == game.user_id:
                print(f"Name: {user.name}, Total Score: {game.total_score}")

def userAccess_01b(session, user_input):
    user = session.query(User).filter(User.name == user_input).first()

    print("\nAre you sure you want to reset your score?")
    print("\nEnter 'yes' to reset")
    print("Enter 'no' to exit")
    
    while(user_input):
        user_choice = input("\nEnter your choice: ")
        if user_choice.lower() == "yes":
            session.query(GameData).filter(GameData.user_id == user.id).update({GameData.total_score: 0})
            session.query(GameData).filter(GameData.user_id == user.id).update({GameData.high_score: 0})
            session.commit()
            exit()
        elif user_choice.lower() == "no":
            print("\nReturning to user settings")
            break
        else:
            print("\nInvalid input. Please try again")

##### Dictionary settings functions

def wordAccess_02a(self):
    pass
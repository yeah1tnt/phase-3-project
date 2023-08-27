from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Dictionary, GameData
from helpers import addUser_0, userAccess_01a
import ipdb
class myCLI:
    def __init__(self):
        self.user_name = [user.name for user in session.query(User).all()]
        self.user_level = [user.level for user in session.query(User).all()]
        self.word = [dict.word for dict in session.query(Dictionary).all()]
        self.main()

    def main(self):
        user_input = input("Enter your username: ")
        if user_input.lower() in self.user_name:
            print(f"\nWelcome, {user_input}!")
        else:
            addUser_0(session, user_input)

        while user_input:
            print("\n       MAIN MENU")
            print("\nEnter a to access user settings")
            print("Enter b to access the dictionary")
            print("Enter c to start dictionary game")
            print("Enter e to exit")
            user_choice = input("\nEnter your choice: ")
            if user_choice.lower() == "a":
                myCLI.userAccess_01(self)
            elif user_choice.lower() == "b":
                myCLI.wordAccess_02(self)
            elif user_choice.lower() == "c":
                myCLI.gameAccess_03(self)
            elif user_choice.lower() == "e":
                exit()
            else:
                print("\nInvalid input. Please try again")

    def userAccess_01(self):
        while(1):
            print("\n       USER SETTINGS")
            print("\nEnter a to show all users and their scores")
            print("Enter b to reset your scores")
            print("Enter e to exit")
            user_choice = input("\nEnter your choice: ")
            if user_choice.lower() == "a":
                userAccess_01a(session)
            elif user_choice.lower() == "b":
                exit()
            elif user_choice.lower() == "e":
                exit()
            else:
                print("\nInvalid input. Please try again")
                
    def wordAccess_02(self):
        print("\n       DICTIONARY SETTINGS")
        exit()
    def gameAccess_03(self):
        print("\n       GAME MENU")
        exit()

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/db/dictionary.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    myCLI()
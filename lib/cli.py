from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Dictionary, GameData
from helpers import addUser_0, userAccess_01a, userAccess_01b, wordAccess_02a, wordAccess_02b, wordAccess_02c, wordAccess_02d
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
                myCLI.userAccess_01(self, user_input)
            elif user_choice.lower() == "b":
                myCLI.wordAccess_02(self, user_input)
            elif user_choice.lower() == "c":
                myCLI.gameAccess_03(self, user_input)
            elif user_choice.lower() == "e":
                exit()
            else:
                print("\nInvalid input. Please try again")

    def userAccess_01(self, user_input):
        while(user_input):
            print("\n       USER SETTINGS")
            print("\nEnter a to show all users and their scores")
            print("Enter b to reset your scores")
            print("Enter c to go back to main menu")
            print("Enter e to exit")
            user_choice = input("\nEnter your choice: ")
            if user_choice.lower() == "a":
                userAccess_01a(session)
            elif user_choice.lower() == "b":
                userAccess_01b(session, user_input)
            elif user_choice.lower() == "c":
                myCLI()
            elif user_choice.lower() == "e":
                print("\nExiting program")
                exit()
            else:
                print("\nInvalid input. Please try again")
                
    def wordAccess_02(self, user_input):
        while(user_input):
            print("\n       DICTIONARY SETTINGS")
            print("\nEnter a to show all words and their definitions")
            print("Enter b to add a new word and definition")
            print("Enter c to generate a random word with its definition")
            print("Enter d to delete a word")
            print("Enter e to go back to main menu")
            print("Enter f to exit")
            user_choice = input("\nEnter your choice: ")
            if user_choice.lower() == "a":
                wordAccess_02a(session)
            elif user_choice.lower() == "b":
                wordAccess_02b(session, user_input)
            elif user_choice.lower() == "c":
                wordAccess_02c(session, user_input)
            elif user_choice.lower() == "d":
                wordAccess_02d(session, user_input)
            elif user_choice.lower() == "e":
                myCLI()
            elif user_choice.lower() == "f":
                print("\nExiting program")
                exit()
            else:
                print("\nInvalid input. Please try again")
    def gameAccess_03(self):
        print("\n       GAME MENU")
        exit()

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/db/dictionary.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    myCLI()
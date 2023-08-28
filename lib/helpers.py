from db.models import User, Dictionary, GameData
import json
from urllib.request import urlopen
from faker import Faker
from random import choice
import random
import ipdb
fake = Faker()

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
            session.query(GameData).filter(GameData.user_id == user.id).update({GameData.high_score: 10})
            session.commit()
            exit()
        elif user_choice.lower() == "no":
            print("\nReturning to user settings")
            break
        else:
            print("\nInvalid input. Please try again")

##### Dictionary settings functions

def wordAccess_02a(session):
    dict = session.query(Dictionary).all()
    for word in dict:
        print(f"Word: {word.word}, Type: {word.type}, Definition: {word.definition}")

def wordAccess_02b(session, user_input):
    while(user_input):
        print("\nWhat word would you like to add?")
        word = input("\nEnter your word: ")
        check1 = session.query(Dictionary).filter(Dictionary.word == word).first()
        if (check1 != None):
            print("\nWord already exists")
            break
        print("\nWhat part of speech do you want for this word? (noun, verb, etc)")
        type = input("\nEnter this word's part of speech: ")

        api = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = urlopen(api.format(word=word))
        data = json.loads(response.read())

        for speech in data:
            if speech['meanings'][0]['partOfSpeech'] == type:
                definition = speech['meanings'][0]['definitions'][0]['definition']
                dictionary = Dictionary(word=word, type=type, definition=definition)
                session.add(dictionary)
                session.commit()
                print(f"\nDefinition: {speech['meanings'][0]['definitions'][0]['definition']}")
                break
        check2 = session.query(Dictionary).filter(Dictionary.word == word).first()
        if(check2 != None):
            print("\nWord succesfully added")
            break
        else:
            print(f"\nWord: {word}, Type: {type}")
            print("Word not successfully added, word does not exist or has invalid speech")

def wordAccess_02c(session, user_input):
    word = fake.word()
    check1 = session.query(Dictionary).filter(Dictionary.word == word).first()
    if (check1 != None):
        print("\nWord already exists")
        return
    api = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = urlopen(api.format(word=word))
    data = json.loads(response.read())
    typechoice = ["noun", "verb", "adjective", "adverb"]
    type = choice(typechoice)
    while(user_input):
        for speech in data:
                if speech['meanings'][0]['partOfSpeech'] == type:
                    definition = speech['meanings'][0]['definitions'][0]['definition']
                    dictionary = Dictionary(word=word, type=type, definition=definition)
                    session.add(dictionary)
                    session.commit()
                    print(f"\nWord: {word}, Type: {type}")
                    print(f"Definition: {speech['meanings'][0]['definitions'][0]['definition']}")
                    break
        check2 = session.query(Dictionary).filter(Dictionary.word == word).first()
        if(check2 != None):
            print("\nWord succesfully added")
            return
        else:
            type = choice(typechoice)

def wordAccess_02d(session, user_input):
    print("\nWord to delete: ")
    word = input("\nEnter your word: ")
    if session.query(Dictionary).filter(Dictionary.word == word).first() == None:
        print("\nWord does not exist")
        return
    session.query(Dictionary).filter(Dictionary.word == word).delete()
    session.commit()
    print("\nWord succesfully deleted")


##### Game settings functions

def gameAccess_03a(session):
    highest_score = session.query(GameData).order_by(GameData.high_score.desc()).first()
    user = session.query(User).filter(User.id == highest_score.user_id).first()
    print(f"\nThe user {user.name} with a score of: {highest_score.high_score} got the highest score")

def gameAccess_03b(session, user_input):
    user = session.query(User).filter(User.name == user_input).first()
    current = session.query(GameData).filter(GameData.user_id == user.id).first()
    print(f"\nYour current score is: {current.total_score}")
    print(f"Your high score is: {current.high_score}")

def gameAccess_03c(session, user_input):
    count = 3
    print("     Game Start")
    while(user_input):
        
        answer, answer_def, answer_choice = random_word(session)
        user = session.query(User).filter(User.name == user_input).first()
        game = session.query(GameData).filter(GameData.user_id == user.id).first()
        if(count == 0):
            print("\nGame Over")
            if(game.high_score < game.game_session):
                game.high_score = game.game_session
            session.commit()
            game.total_score = game.game_session + game.total_score
            game.game_session = 0
            session.commit()
            return
        while(count != 0):
            print(f"\nYou have {count} attempts left")
            print(f"Your current score is: {game.game_session}")
            print(f"\nThe word is {answer}")
            print("What is the definition of this word?\n")
            for i in range(4):
                print(f"{i+1}: {answer_choice[i]}")
            user_choice = input("\nEnter your choice from 1 to 4: ")
            if user_choice.isdigit() and int(user_choice) in range(1, 5):
                user_choice = int(user_choice) - 1
                if answer_choice[user_choice] == answer_def:
                    print("\nCorrect!")
                    game.game_session += 1
                    break
                else:
                    print("\nIncorrect")
                    count -= 1
                    break
            else:
                print("\nInvalid input, must be number in range. Please try again")


        
def gameAccess_03d(session, user_input):
    count = 3
    print("     Game Start")
    while(user_input):
        answer, answer_def, answer_choice = random_def(session)
        user = session.query(User).filter(User.name == user_input).first()
        game = session.query(GameData).filter(GameData.user_id == user.id).first()
        if(count == 0):
            print("\nGame Over")
            if(game.high_score < game.game_session):
                game.high_score = game.game_session
            session.commit()
            game.total_score = game.game_session + game.total_score
            game.game_session = 0
            session.commit()
            return
        while(count != 0):
            print(f"\nYou have {count} attempts left")
            print(f"Your current score is: {game.game_session}")
            print(f"\nThe definition is {answer}")
            print("What is the word for this definition?\n")
            for i in range(4):
                print(f"{i+1}: {answer_choice[i]}")
            user_choice = input("\nEnter your choice from 1 to 4: ")
            if user_choice.isdigit() and int(user_choice) in range(1, 5):
                user_choice = int(user_choice) - 1
                if answer_choice[user_choice] == answer_def:
                    print("\nCorrect!")
                    game.game_session += 1
                    break
                else:
                    print("\nIncorrect")
                    count -= 1
                    break
            else:
                print("\nInvalid input, must be number in range. Please try again")

def random_word(session):
    dict = [dict.word for dict in session.query(Dictionary).all()]
    answer = choice(dict)
    answer_def = session.query(Dictionary).filter(Dictionary.word == answer).first().definition
    answer_choice = [answer_def]
    while len(answer_choice) < 4:
        extra = choice(dict)
        extra_def = session.query(Dictionary).filter(Dictionary.word == extra).first().definition
        if extra_def not in answer_choice:
            answer_choice.append(extra_def)
    random.shuffle(answer_choice)

    return answer, answer_def, answer_choice

def random_def(session):
    dict = [dict.definition for dict in session.query(Dictionary).all()]
    answer = choice(dict)
    answer_def = session.query(Dictionary).filter(Dictionary.definition == answer).first().word
    answer_choice = [answer_def]
    while len(answer_choice) < 4:
        extra = choice(dict)
        extra_def = session.query(Dictionary).filter(Dictionary.definition == extra).first().word
        if extra_def not in answer_choice:
            answer_choice.append(extra_def)
    random.shuffle(answer_choice)

    return answer, answer_def, answer_choice
from models import (User, Dictionary, GameData)
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from random import randint
import json
from urllib.request import urlopen
fake = Faker()

engine = create_engine('sqlite:///lib/db/dictionary.db')
session = Session(engine, future = True)

def create_user():
    user = User(name=fake.name(), age=randint(1, 100), level=randint(1, 100))
    session.add(user)
    session.commit()

def create_dictionary():
    word = fake.word()
    api = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = urlopen(api.format(word=word))
    data = json.loads(response.read())
    type = data[0]['meanings'][0]['partOfSpeech']
    definition = data[0]['meanings'][0]['definitions'][0]['definition']
    dictionary = Dictionary(word=word, type=type, definition=definition)
    session.add(dictionary)
    session.commit()

def create_game_data():
    game_data = GameData(user_id=fake.name(), game_session=fake.word(), high_score=randint(1, 100), total_score=randint(1, 100))
    session.add(game_data)
    session.commit()

def delete_all():
    session.query(User).delete()
    session.query(Dictionary).delete()
    session.query(GameData).delete()
    session.commit()

if __name__ == '__main__':
    delete_all()
    create_user()
    create_dictionary()
    create_game_data()
    
    session.close()
    session.commit()
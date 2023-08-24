from models import (Dictionary, GameData)
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import randint

fake = Faker()

engine = create_engine('sqlite:///dictionary.db')
Session = sessionmaker(bind=engine)
session = Session()
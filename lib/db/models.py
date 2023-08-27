from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    level = Column(Integer)

    gameData = relationship("GameData", back_populates="user")

    def __rep__(self):
        return f'Id: {self.id}' \
            + f'Name: {self.name}' \
            + f'Age: {self.age}' \
            + f'Level: {self.level}'
    

class Dictionary(Base):
    __tablename__ = "dictionary"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String)
    type = Column(String)
    definition = Column(String)

    def __rep__(self):
        return f'Id: {self.id}' \
            + f'Word: {self.word}' \
            + f'Type: {self.type}' \
            + f'Definition: {self.definition}'
    
class GameData(Base):
    __tablename__ = "game_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    game_session = Column(Integer)
    high_score = Column(Integer)
    total_score = Column(Integer)

    user = relationship("User", back_populates="gameData")

    def __rep__(self):
        return f'Id: {self.id}' \
            + f'User Id: {self.user_id}' \
            + f'Game Session: {self.game_session}' \
            + f'High Score: {self.high_score}' \
            + f'Total Score: {self.total_score}'
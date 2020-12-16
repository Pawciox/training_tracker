from sqlalchemy import create_engine, Column, Integer, DECIMAL, String
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class Round(Base):
    __tablename__ = 'rounds'

    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)
    weight = Column(DECIMAL)
    number_of_reps = Column(Integer)
    tempo = Column(String)
    # pause = Column(Integer)


    def __repr__(self):
        s = f"""
            exercise_name = {self.exercise_name}
            weight = {self.weight} kg
            number_of_reps = {self.number_of_reps}
            tempo = {self.tempo}
        """
        return s


class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)


    def __repr__(self):
        return self.exercise_name



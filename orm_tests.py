from models import Set, Exercise, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()


first = Set(exercise_name='Bench press', weight=75, number_of_reps=10, tempo='3010')
second = Set(exercise_name='Bench press', weight=80, number_of_reps=8, tempo='3010')
third = Set(exercise_name='Bench press', weight=100, number_of_reps=6, tempo='3010')

session.add_all([first, second, third])
session.commit()

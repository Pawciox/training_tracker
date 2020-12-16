from models import Round, Exercise
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)


first = Round(exercise_name='Bench press', weight= 75, number_of_reps=10, tempo='3010')
second = Round(exercise_name='Bench press', weight= 80, number_of_reps=8, tempo='3010')
third = Round(exercise_name='Bench press', weight= 100, number_of_reps=6, tempo='3010')

print(first)
print(second)
print(third)
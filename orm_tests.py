from models import Set, Exercise, Base
from sqlalchemy import create_engine, text, and_, func
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()


first = Set(exercise_name='Bench press', weight=75, number_of_reps=10, tempo='3010')
second = Set(exercise_name='Bench press', weight=80, number_of_reps=8, tempo='3010')
third = Set(exercise_name='Squat', weight=60, number_of_reps=6, tempo='3010')
fourth = Set(exercise_name='Squat', weight=120, number_of_reps=3, tempo='3010')

session.add_all([first, second, third, fourth])
session.commit()

q = session.query(Set).filter(text('weight > 78 AND number_of_reps = 8'))
q2 = session.query(Set).filter(and_(text('weight > 78')), (text('number_of_reps = 8')))
q3 = session.query(Set).filter(and_((Set.weight > 78), (Set.number_of_reps == 8)))
q4 = session.query(Set).filter(Set.weight > 78).filter(Set.number_of_reps == 8)

q5 = session.query(Set).filter(text('weight >:weight AND number_of_reps =:reps')).params(weight=78, reps=8)
q6 = session.query(Set).from_statement(text('select * from sets where weight >= :weight ')).params(weight=80)

stmt = text('select id, exercise_name, weight, number_of_reps, tempo from sets where weight >= :weight')
stmt = stmt.columns(Set.id, Set.exercise_name, Set.number_of_reps, Set.tempo)
q7 = session.query(Set).from_statement(stmt).params(weight=80)

stmt = text('select weight, exercise_name from sets where weight >= :weight')
stmt = stmt.columns(Set.weight, Set.exercise_name)
for n, w in session.query(Set.exercise_name, Set.weight).from_statement(stmt).params(weight=80):
    print(n, w)

q8 = session.query(Set).filter(Set.weight > 78).count()
q9 = session.query(func.count('*')).filter(Set.weight > 78)
print(q9.scalar())


# print(q.all() == q2.all() == q3.all() == q4.all() == q5.all())

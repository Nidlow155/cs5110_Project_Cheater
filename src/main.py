from Student import Student, Class
from random import randint

NUM_STUDENTS = 5
NUM_DAYS = 10
# students = [ Student(i, randint(0, 10), NUM_DAYS) for i in range(NUM_STUDENTS)] # one way to make it more realistic is to give a distribution of procrastination values that is heavily skewed rather than randomly distributed since most people procrastinate

# show the start day
# print(f'The students must complete the assignment by day number {NUM_DAYS}')
# for student in students:
#     print(f'Student {student.id} has a procrastination characteristic of {student.procrastinate}, so they will start on day {student.startDay}')

myClass = Class(NUM_STUDENTS, NUM_DAYS)

# print()
# run the simulation
for i in range(NUM_DAYS):
    # print(f'At the end of day {i}...')
    myClass.useDay(report=True)



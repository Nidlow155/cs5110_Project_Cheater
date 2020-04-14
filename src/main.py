from Student import Student
from Class import Class

NUM_STUDENTS = 5
NUM_DAYS = 10

myClass = Class(NUM_STUDENTS, NUM_DAYS)

# run the simulation
for i in range(NUM_DAYS):
    myClass.useDay(report=True)



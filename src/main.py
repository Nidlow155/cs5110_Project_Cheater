from Student import Student, Class
from visual import Visual
from random import randint

NUM_STUDENTS = 5
NUM_DAYS = 10
myClass = Class(NUM_STUDENTS, NUM_DAYS)

# run the simulation
for i in range(NUM_DAYS):
    myClass.useDay(report=False)

v = Visual(myClass.students)
v.showClass()

# input("next class")
# NUM_STUDENTS = 20
# NUM_DAYS = 10
# myClass = Class(NUM_STUDENTS, NUM_DAYS)
# v.setClass(myClass.students)
# v.showClass()

v.dontClose()

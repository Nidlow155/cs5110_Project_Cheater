from Student import Student
from Class import Class
from configuration import *
from visual import Visual


myClass = Class(NUM_STUDENTS, NUM_DAYS)

# run the simulation
v = Visual(myClass.students)
v.showClass()
for i in range(NUM_DAYS):
    myClass.useDay(report=True)
    v.updateClass(myClass.students)
v.dontClose()

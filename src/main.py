from Student import Student
from Class import Class
from configuration import *
from visual import Visual


myClass = Class(NUM_STUDENTS, NUM_DAYS)

# run the simulation
for i in range(NUM_DAYS):
    myClass.useDay(report=False)

v = Visual(myClass.students)
v.showClass()
# how to update class
# v.setClass(myClass.students)
# v.showClass()
v.dontClose()

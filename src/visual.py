import turtle
import math

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x: {self.x}  y: {self.y}"

class Visual:
    def __init__(self, students=None):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t2 = turtle.Turtle()
        self.t2.speed(0)
        self.t2.hideturtle()
        self.students = students
        self.sCoords = []
        self.updatedCheaters = []
        self.updatedFinished = []
        if students:
            self.setClass(students)

    ##################
    # public functions #
    def showClass(self):
        # self.t.clear()
        self._drawAllStudents()
        self._drawAllFriendships()
        self._drawDayCount()
        # turtle.done()

    def updateClass(self, students, day):
        self.setClass(students)
        self._drawAllStudents(updatesOnly=True)
        self._drawDayCount(day)

    def setClass(self, students):
        self.students = students
        self._calculateStudentCoords()

    def clearScreen(self):
        self.t.clear()

    def dontClose(self):
        turtle.done()

    #####################
    # private functions #
    def _calculateStudentCoords(self):
        self.sCoords = []
        n = len(self.students)
        r = n * 10
        self.radius = r
        for j in range(n):
            theta = j*(2*math.pi / n)
            c = Coords(r*math.cos(theta), r*math.sin(theta))
            self.sCoords.append(c)

    def _drawAllFriendships(self):
        for s1 in self.students:
            for s2 in s1.friends:
                self._linkStudents(s1.id, s2.id)

    def _linkStudents(self, i, j):
        self._drawLine(self.sCoords[i], self.sCoords[j])

    def _drawLine(self, c1, c2):
        self.t.up()
        self.t.goto(c1.x, c1.y)
        self.t.down()
        self.t.goto(c2.x, c2.y)

    def _drawStudent(self, i):
        diameter = 20
        self.t.up()
        c = self.sCoords[i]
        self.t.goto(c.x, c.y)
        self.t.down()
        color = "Green" if self.students[i].finished else "Black"
        self.t.dot(diameter, color)
        if self.students[i].cheater:
            self.t.dot(diameter/2, "Red")

    def _drawAllStudents(self, updatesOnly=False):
        for i in range(len(self.students)):
            if updatesOnly:
                if self.students[i].cheater and i not in self.updatedCheaters:
                    self.updatedCheaters.append(i)
                    self._drawStudent(i)
                if self.students[i].finished and i not in self.updatedFinished:
                    self.updatedFinished.append(i)
                    self._drawStudent(i)
            else:
                self._drawStudent(i)

    def _drawDayCount(self, day=""):
        self.t2.up()
        self.t2.goto(0,self.radius+40)
        style = ('Courier', 30)
        self.t2.clear()
        self.t2.write('Day: ', True, font=style, align='center')
        self.t2.write(day, font=style, align='center')

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
        self.students = students
        self.sCoords = []
        if students:
            self.setClass(students)

    ##################
    # public functions #
    def showClass(self):
        self.t.clear()
        self._drawAllStudents()
        self._drawAllLinks()
        # turtle.done()

    def setClass(self, students):
        self.students = students
        self._calculateStudentPositions()

    def clearScreen(self):
        self.t.clear()

    def dontClose(self):
        self.t.done()

    #####################
    # private functions #
    def _calculateStudentPositions(self):
        self.sCoords = []
        n = len(self.students)
        r = n * 10
        for j in range(n):
            theta = j*(2*math.pi / n)
            c = Coords(r*math.cos(theta), r*math.sin(theta))
            self.sCoords.append(c)

    def _drawAllLinks(self):
        for s in self.students:
            for j in s.friends:
                self._linkStudents(s.id, j)

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
        color = "Red" if self.students[i].cheater else "Black"
        self.t.dot(diameter, color)

    def _drawAllStudents(self):
        for i in range(len(self.students)):
            self._drawStudent(i)


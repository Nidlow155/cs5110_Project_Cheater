from random import randint

PROCRASTINATION_RANGE = (0, 10)
CHEAT_RANGE = (0, 10)

class Student:
    def __init__(self, id, cheat_level, procrastinate_level, dueDate):
        assert PROCRASTINATION_RANGE[0] <= procrastinate_level <= PROCRASTINATION_RANGE[10]
        assert CHEAT_RANGE[0] <= cheat_level <= CHEAT_RANGE[10]

        self.id = id
        self.cheat_level = cheat_level
        self.procrastinate_level = procrastinate_level
        self.dueDate = dueDate # considered to be due at 12:01 AM on the dueDate. For example, if it is due on day 10, they have days 0-9 to work on the assignment
        self.dayNumber = 0
        self.progress = 0 # a number between 0 and 1 that shows the fraction of the total work already completed
        self.startDay = int((procrastinate_level / 10) * (self.dueDate - 1)) # the day when they will start. Lies in the range [0, self.dueDate - 1], since the latest you can start is day 9 if it is due on day 10
        self.workPerDay = 1 / (self.dueDate - self.startDay)

        self.friends = [] # TODO LATER

    def useDay(self):
        if self.dayNumber >= self.dueDate:
            raise Exception("The student can't do anything on (or past) the due date, since it is considered to be due at 12:01 AM on the due date.")
        if (self.dayNumber >= self.startDay):
            self.progress += self.workPerDay
        self.dayNumber += 1
        self.potentiallyCheat()

    def potentiallyCheat(self):
        pass


class Class:
    def __init__(self, student_count, dueDate):
        self.dueDate = dueDate # considered to be due at 12:01 AM on the dueDate. For example, if it is due on day 10, they have days 0-9 to work on the assignment
        self.students = []

        for i in range(student_count):
            cheat = randint(*CHEAT_RANGE)
            procrastinate = randint(*PROCRASTINATION_RANGE)
            self.students.append(Student(i, cheat, procrastinate, dueDate))

    def useDay(self):


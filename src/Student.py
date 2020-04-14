from random import randint

PROCRASTINATION_RANGE = (0, 10)
CHEAT_RANGE = (0, 10)

class Student:
    def __init__(self, id, cheat_level, procrastinate_level, dueDate):
        assert PROCRASTINATION_RANGE[0] <= procrastinate_level <= PROCRASTINATION_RANGE[1]
        assert CHEAT_RANGE[0] <= cheat_level <= CHEAT_RANGE[1]

        self.id = id
        self.cheat_level = cheat_level
        self.procrastinate_level = procrastinate_level
        self.dueDate = dueDate  # considered to be due at 12:01 AM on the dueDate. For example, if it is due on day 10, they have days 0-9 to work on the assignment
        self.progress = 0  # a number between 0 and 1 that shows the fraction of the total work already completed
        self.finished = False

        lastDay = dueDate - 1
        error = self.dueDate // 10  # error level of 10% of the total work time
        self.startDay = ((procrastinate_level // 10) * lastDay) + randint(-error, error)   # start day = proportional to their procrastination +/- 10% error level
        if self.startDay >= self.dueDate:  # if start day is after its due
            self.startDay = lastDay
        if self.startDay < 0:  # if start day is before first day
            self.startDay = 0
        self.finishDay = randint(self.startDay, lastDay)  # finish randomly between the day they start and the day before due
        self.workPerDay = 1 / (self.finishDay - self.startDay + 1)  # get the work done evenly during each day bewteen due date and finish date

        self.friends = [] # TODO LATER

    def useDay(self, today, report=False):
        if today >= self.dueDate:
            raise Exception("The student can't do anything on (or past) the due date, since it is considered to be due at 12:01 AM on the due date.")
        # work
        if (today >= self.startDay and not self.finished):
            self.progress += self.workPerDay
        
        # check if student is done
        if (abs(self.progress - 1) < .00001):
            self.progress = 1
            self.finished = True
        
        # cheat if need be
        self.potentiallyCheat(today, report)

    def potentiallyCheat(self, today, report=False):
        if self.progress < 1 and self.cheat_level <= 3 and today >= self.startDay:
            self.potentiallyRequest(report)
        if self.cheat_level <= 3 and today >= self.startDay:
            self.potentiallySend(report)
            
    def potentiallySend(self, report=False):
        if report:
            print('Student ' + str(self.id) + ' sent their homework.')
    
    def potentiallyRequest(self, report=False):
        if report:
            print('Student ' + str(self.id) + ' requested homework.')

class Class:
    def __init__(self, student_count, dueDate):
        self.dueDate = dueDate # considered to be due at 12:01 AM on the dueDate. For example, if it is due on day 10, they have days 0-9 to work on the assignment
        self.today = 0
        self.students = []

        for i in range(student_count):
            cheat = randint(*CHEAT_RANGE)
            procrastinate = randint(*PROCRASTINATION_RANGE)
            self.students.append(Student(i, cheat, procrastinate, dueDate))

    def useDay(self, report=False):
        if report:
            print('During day: ' + str(self.today))
        for student in self.students:
            student.useDay(self.today, report)
        if report:
            self.report()
        self.today += 1

    
    def report(self):
        print("\nAt the end of day: " + str(self.today))
        for student in self.students:
            if student.finished:
                print(f'Student {student.id} has finished')
            else:
                print(f'Student {student.id} has progress {student.progress}')
        print()
                




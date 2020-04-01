class Student:
    def __init__(self, id, procrastinate, dueDate):
        self.id = id
        if not (0 <= procrastinate <= 10):
            raise Exception("The procrastination characteristic must be in the range [0, 10]")
        self.procrastinate = procrastinate
        self.dayNumber = 0
        self.dueDate = dueDate # considered to be due at 12:01 AM on the dueDate. For example, if it is due on day 10, they have days 0-9 to work on the assignment
        self.progress = 0 # a number between 0 and 1 that shows the fraction of the total work already completed
        self.startDay = int((procrastinate / 10) * (self.dueDate - 1)) # the day when they will start. Lies in the range [0, self.dueDate - 1], since the latest you can start is day 9 if it is due on day 10
        self.workPerDay = 1 / (self.dueDate - self.startDay)

    def useDay(self):
        if self.dayNumber >= self.dueDate:
            raise Exception("The student can't do anything on (or past) the due date, since it is considered to be due at 12:01 AM on the due date.")
        if (self.dayNumber >= self.startDay):
            self.progress += self.workPerDay
        self.dayNumber += 1
from Student import Student
from configuration import *
from random import randint, shuffle
from seaborn import barplot


class Class:
    def __init__(self, student_count, dueDate):
        # verbosity for each type of initialization, set to false for deployment (didn't parameterize so it wouldn't be ugly)
        verbose_setFriends = False
        verbose_buildDistributions = True

        # attributes on a class
        self.dueDate = dueDate  # considered to be due at 12:01 AM on the dueDate. For example, if it is due on day 10, they have days 0-9 to work on the assignment
        self.today = 0
        self.students = []

        # build the distributions of procrastination and cheat levels
        procrastinationLevels = self.buildDistribution(PROCRASTINATE_DISTR, verbose_buildDistributions, 'procrastination')
        cheatLevels = self.buildDistribution(CHEAT_DISTR, verbose_buildDistributions, "cheat")

        # add the students
        for i in range(student_count):
            cheat = 2
            procrastinate = 4
            self.students.append(Student(i, cheat, procrastinate, dueDate))

        # set the friends
        needsFriends = [True] * NUM_STUDENTS
        counter = 0
        while (True in needsFriends):
            if verbose_setFriends:
                print(f'\n========\nROUND {counter}\n========\n')
            for i in range(len(self.students)):
                if self.students[i].needsFriends():
                    self.students[i].makeFriends(self.students, verbose_setFriends)
                needsFriends[i] = self.students[i].needsFriends()
            counter += 1
            if counter == MAX_ITERATIONS:
                break
        if counter == MAX_ITERATIONS:
            print("Maxed Out")
        else:
            if verbose_setFriends:
                for student in self.students:
                    student.printFriendList()

    def buildDistribution(self, distribution, verbose, name):
        values = []
        for level in range(len(distribution)):
            quantityAtGivenLevel = int(distribution[level] * NUM_STUDENTS)
            for i in range(quantityAtGivenLevel):
                values.append(level)
        if len(values) != NUM_STUDENTS:
            for i in range(NUM_STUDENTS - len(values)):
                values.append(randint(0, len(distribution) - 1))
        if verbose:
            print(f"For {name}, values are (before shuffling):")
            for i in values:
                print(str(i) + ", ", end='')
            print()
        shuffle(values)
        return values

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

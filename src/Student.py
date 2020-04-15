from random import randint, shuffle
from common import *

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

        # friends parameters
        self.personality = randint(0, NUM_PERSONALITIES)
        self.numFriends = randint(.1 * NUM_STUDENTS, .7 * NUM_STUDENTS)
        self.friends = [] # TODO LATER

    def getId(self):
        return self.id
    
    def getCheatLevel(self):
        return self.cheat_level
    
    def getProcLevel(self):
        return self.procrastinate_level
    
    def getProgress(self):
        return self.progress
    
    def getStartDay(self):
        return self.startDay
    
    def getFinishDay(self):
        return self.finishDay
    
    def getWorkPerDay(self):
        return self.workPerDay
    
    def getFriends(self):
        return self.friends

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
        # self.potentiallyCheat(today, report)

    def potentiallyCheat(self, today, report=False):
        if self.progress < 1 and self.cheat_level <= 3 and today >= self.startDay:
            self.potentiallyRequest(report)
        if self.cheat_level <= 3 and today >= self.startDay:
            self.potentiallySend(report)
            
    def potentiallySend(self, report=False):
        for friend in self.friends:
            # friend.potentiallyReceive(report) # TODO add this method in once friends are implemented
            if report:
                print('Student ' + str(self.id) + ' sent their homework to ' + str(friend.getId()))
    
    def potentiallyRequest(self, report=False):
        if self.cheat_level <= 3: # TODO introduce the idea that students may not finish in time and that's why they would "request help" (cheat)
            for friend in self.friends:
                # friend.potentiallySend() # TODO determine if they only ask from certain friends
                if report:
                    print('Student ' + str(self.id) + ' requested homework from ' + str(friend.getId()))
            
    def potentiallyReceive(self, friendId, report=False):
        if self.cheat_level <= 3 and self.progress < 1: # TODO determine metrics for why a student would accept homework
            # TODO algorithm for if they receive how much does their progress increase
            # TODO do they receive based on any of their friend's metrics?
            if report:
                print('Student ' + str(self.id) + ' received homework from ' + str(friendId))

    def makeFriends(self, students):
        # validation
        if len(self.friends) >= self.numFriends:
            raise Exception("Shouldn't be calling Student::makeFriends() when the student already has all their friends")

        # functionality
        if len(self.friends) == 0:
            candidates = students.copy()
        else:
            candidates = self.getFriendsOfFriends()
            print(f'len(candidates) = {len(candidates)}')
        shuffle(candidates)
        self.friends.append(candidates[0])
        if len(self.friends) == self.numFriends:
            return 1
        else:
            return 0

    def needsFriends(self):
        if len(self.friends) < self.numFriends:
            return True
        else:
            return False


    def getFriendsOfFriends(self):
        secondDegreeFriends = []
        for myFriend in self.friends:
            for theirFriend in myFriend.friends:
                if theirFriend not in secondDegreeFriends:
                    secondDegreeFriends.append(theirFriend)
        return secondDegreeFriends


    def printFriendList(self):
        print(f'Student {self.id} has {len(self.friends)} friends, with max friends of {self.numFriends}. Friends\'s ids are: ', end="")
        for friend in self.friends:
            print(str(friend.getId()) + ', ', end='')
        print()


from random import randint, shuffle
from numpy import argsort
from configuration import *

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
        self.cheater = False

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
        self.preferredNumFriends = randint(MIN_FRIENDS, MAX_FRIENDS)
        self.friends = []
        
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
    
    def setCheater(self, isCheater):
        self.cheater = isCheater
        
    def updateProgress(self, addedProgress):
        if self.progress < 1:
            self.progress += addedProgress
        if self.progress > 1:
            self.progress = 1
            self.finished = True

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
        
    # Willing to cheat if closer to the deadline and add peer pressure meaning the more friends you have
    # that are willing to cheat; meaning the more friends you have that have cheated will change you
    # more willing to send than request
    def potentiallyCheat(self, today, report=False):
        if self.progress < 1 and self.cheat_level <= MORAL_CHEAT_MIN and today >= self.startDay and not self.cheater:
            self.request(today, report)
        
    def potentiallySend(self, today, requester, report=False):
        if self.cheat_level <= MORAL_CHEAT_MIN and self.startDay >= today and self.progress > requester.getProgress():
            if report:
                print('Student ' + str(self.id) + ' sent their homework to ' + str(requester.getId()))
            return True
        else:
            return False
    
    def request(self, today, report=False):
        for friend in self.friends:
            if report:
                print('Student ' + str(self.id) + ' requested homework from ' + str(friend.getId()))
            if friend.potentiallySend(today, self, report):
                self.cheater = True
                friend.setCheater(True) # TODO is the friend also a cheater?
                # self.updateProgress(friend.getWorkPerDay())
                # friend.updateProgress(self.workPerDay)

    def makeFriends(self, students):
        print(f'ID is {self.id}, preferredNumFriends is {self.preferredNumFriends}')
        # validation
        if len(self.friends) >= self.preferredNumFriends:
            raise Exception("Shouldn't be calling Student::makeFriends() when the student already has all their friends")

        # get all the candidates
        allCandidates = []
        for student in students:
            if self.isCandidate(student):
                allCandidates.append(student)
        shuffle(allCandidates)

        # get preferred candidates
        likelyCandidates = self.getFriendsOfFriends()
        if len(likelyCandidates) < MIN_CANDIDATES:
            print(f'(supplementing existing {len(likelyCandidates)} candidates with new candidates with ids ', end='')
            for candidate in allCandidates:
                if candidate not in likelyCandidates:
                    likelyCandidates.append(candidate)
            print(')')

        # select a candidate
        print(f'Candidate ids are: ', end='')
        for candidate in likelyCandidates:
            print(candidate.id, ', ', end='')
        print()
        print(f'Friends before are: ', end='')
        for friend in self.friends:
            print(friend.getId(), ", ", end='')
        newFriend = self.selectCandidate(likelyCandidates)
        self.friends.append(newFriend)
        newFriend.addFriend(students[self.id])
        print(f'\nAdded friend {likelyCandidates[0].id}')
        print('*****')


    def selectCandidate(self, candidates):
        scores = [0] * len(candidates)
        for i in range(len(candidates)):
            if candidates[i].personality == self.personality:
                scores[i] += 1
            if abs(candidates[i].cheat_level - self.cheat_level) <= CHEAT_TOLERANCE:
                scores[i] += 1
            if abs(candidates[i].procrastinate_level - self.procrastinate_level) <= PROCRASTINATE_TOLERANCE:
                scores[i] += 1
        indexOfSelection = argsort(scores)[-1]
        return candidates[indexOfSelection]


    def addFriend(self, student):
        self.friends.append(student)

    def needsFriends(self):
        if len(self.friends) < self.preferredNumFriends:
            return True
        else:
            return False


    def getFriendsOfFriends(self):
        secondDegreeFriends = []
        for myFriend in self.friends:
            for theirFriend in myFriend.friends:
                if (theirFriend not in secondDegreeFriends) and self.isCandidate(theirFriend):
                    secondDegreeFriends.append(theirFriend)
        return secondDegreeFriends


    def isCandidate(self, student):
        return (student.getId() != self.id) and (student not in self.friends)


    def printFriendList(self):
        print(f'Student {self.id} has {len(self.friends)} friends, with max preferred friends of {self.preferredNumFriends}. Friends\'s ids are: ', end="")
        ids = []
        for friend in self.friends:
            ids.append(friend.getId())
        ids.sort()
        for id in ids:
            print(str(id) + ', ', end='')
        print()


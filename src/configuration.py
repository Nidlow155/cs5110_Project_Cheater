from sys import exit

def getSumOfList(p_list):
    # the sum(list) native function didn't do what I wanted it to, so I made this function, then it failed me too
    sum = 0
    for i in p_list:
        sum += i
    if abs(1 - sum) < .00001:
        sum = 1
    return sum

# demographic configuration
CHEAT_DISTR = [0, .7, .1, 0, .1, .1]
PROCRASTINATE_DISTR = [0, 0, .4, .2, .1, .2, .1]

# classroom configuration
NUM_DAYS = 10
NUM_STUDENTS = 25
DAY_DELAY = .75  # seconds

# student configuration
NUM_PERSONALITIES = 5
MORAL_CHEAT_MIN_REQUEST = 3
MORAL_CHEAT_MIN_SEND = 2

# friend generation configuration
CHEAT_TOLERANCE = 2
PROCRASTINATE_TOLERANCE = 1
MIN_CANDIDATES = 4
MIN_FRIENDS = 1
MAX_FRIENDS = 3
MAX_ITERATIONS = 1000

# validate configurations
MAX_PROCRASTIATION = len(PROCRASTINATE_DISTR) - 1
MAX_CHEAT = len(CHEAT_DISTR) - 1

if (MAX_FRIENDS > NUM_STUDENTS - 1):
    exit("Can't have more friends than students")
if (MIN_FRIENDS < 0):
    exit("Can't have less than 0 friends")
if (CHEAT_TOLERANCE > MAX_CHEAT):
    exit(f"CHEAT_TOLERANCE is greater than the max permissible level of {MAX_CHEAT}")
if (CHEAT_TOLERANCE < 0):
    exit("CHEAT_TOLERANCE is less than 0")
if (MIN_CANDIDATES > (NUM_STUDENTS - 1)):
    exit("MIN_CANDIDATES is greater than the number of students")
if (MIN_CANDIDATES < 0):
    exit("MIN_CANDIDATES is less than zero")
if (PROCRASTINATE_TOLERANCE > MAX_PROCRASTIATION):
    exit(f"PROCRASTINATE_TOLERANCE is greater than the max permissible level of {MAX_PROCRASTIATION}.")
if (PROCRASTINATE_TOLERANCE < 0):
    exit("PROCRASINATE_TOLERANCE is less than 0")
if getSumOfList(CHEAT_DISTR) != 1:
    exit(f"The sum of CHEAT_DISTR must equal 1, equals {getSumOfList(CHEAT_DISTR)}")
if getSumOfList(PROCRASTINATE_DISTR) != 1:
    exit(f"The sum of PROCRASTINATE_DISTR must equal 1, equals {getSumOfList(PROCRASTINATE_DISTR)}")


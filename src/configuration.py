from sys import exit

# classroom configuration
NUM_DAYS = 20
NUM_STUDENTS = 30

# student configuration
PROCRASTINATION_RANGE = (0, 10)
CHEAT_RANGE = (0, 10)
NUM_PERSONALITIES = 16
MORAL_CHEAT_MIN = 3

# friend generation configuration
CHEAT_TOLERANCE = 3
PROCRASTINATE_TOLERANCE = 7
MIN_CANDIDATES = 4
MIN_FRIENDS = 5
MAX_FRIENDS = 8
MAX_ITERATIONS = 10000000000

# validate configurations
if (MAX_FRIENDS > NUM_STUDENTS - 1):
    exit("Can't have more friends than students")
if (MIN_FRIENDS < 0):
    exit("Can't have less than 0 friends")
if (CHEAT_TOLERANCE > CHEAT_RANGE[1]):
    exit("CHEAT_TOLERANCE is above the maximum value")
if (CHEAT_TOLERANCE < 0):
    exit("CHEAT_TOLERANCE is less than 0")
if (MIN_CANDIDATES > (NUM_STUDENTS - 1)):
    exit("MIN_CANDIDATES is greater than the number of students")
if (MIN_CANDIDATES < 0):
    exit("MIN_CANDIDATES is less than zero")
if (PROCRASTINATE_TOLERANCE > PROCRASTINATION_RANGE[1]):
    exit("PROCRASTINATE_TOLERANCE is greater than max procrastination")
if (PROCRASTINATE_TOLERANCE < 0):
    exit("PROCRASINATE_TOLERANCE is less than 0")




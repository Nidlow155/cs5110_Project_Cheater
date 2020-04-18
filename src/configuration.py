from sys import exit

# demographic configuration
CHEAT_DISTR = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
PROCRASTINATE_DISTR = [.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]

# classroom configuration
NUM_DAYS = 10
NUM_STUDENTS = 20
DAY_DELAY = .75  # seconds

# student configuration
NUM_PERSONALITIES = 5
MORAL_CHEAT_MIN_REQUEST = 3
MORAL_CHEAT_MIN_SEND = 2

# friend generation configuration
CHEAT_TOLERANCE = 3
PROCRASTINATE_TOLERANCE = 7
MIN_CANDIDATES = 4
MIN_FRIENDS = 1
MAX_FRIENDS = 3
MAX_ITERATIONS = 1000

# validate configurations
if (MAX_FRIENDS > NUM_STUDENTS - 1):
    exit("Can't have more friends than students")
if (MIN_FRIENDS < 0):
    exit("Can't have less than 0 friends")
if (CHEAT_TOLERANCE > (len(CHEAT_DISTR) - 1)):
    exit(f"CHEAT_TOLERANCE is greater than the max permissible level of {len(CHEAT_DISTR) - 1}.")
if (CHEAT_TOLERANCE < 0):
    exit("CHEAT_TOLERANCE is less than 0")
if (MIN_CANDIDATES > (NUM_STUDENTS - 1)):
    exit("MIN_CANDIDATES is greater than the number of students")
if (MIN_CANDIDATES < 0):
    exit("MIN_CANDIDATES is less than zero")
if (PROCRASTINATE_TOLERANCE > (len(PROCRASTINATE_DISTR) - 1)):
    exit(f"PROCRASTINATE_TOLERANCE is greater than the max permissible level of {len(PROCRASTINATE_DISTR - 1)}.")
if (PROCRASTINATE_TOLERANCE < 0):
    exit("PROCRASINATE_TOLERANCE is less than 0")
if round(sum(CHEAT_DISTR)) != 1:
    exit(f"The sum of CHEAT_DISTR must equal 1, equals {sum(CHEAT_DISTR)}")
if round(sum(PROCRASTINATE_DISTR)) != 1:
    exit(f"The sum of PROCRASTINATE_DISTR must equal 1, equals {sum(PROCRASTINATE_DISTR)}")

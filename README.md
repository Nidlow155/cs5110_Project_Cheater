# Find the Cheater - CS 5110 Final Project

## Group Members : Alex Beeston, Joseph Carlisle, Matthew Lindow

---

## Code Objective

The objective of our code is to create a network of students that will decide to cheat or not within an assignment's work period. Various metrics such as moral, desperation, procrastination, and peer pressure will determine whether or not a student decides to cheat.

The original intent of the code was also to create an algorithm for determining which students were the original cheaters within this network/classroom. We were unable to implement this functionality but have successfully built a network of student who act as agents making decisions of whether or not to cheat.

---

## How to Run the Code

We have created a virtual environment to run the code so the following commands may be run in the command line.

If a virtual envionrment has not been set up run this command:

    pip install pipenv

Install any necessary dependencies from the pip file.

    pipenv install <package name>

Afterwards the code can be run in a few ways from the root directory:

    pipenv shell
    python src/main.py 

Or:

    pipenv run python src/main.py

The code may also be run from the IDE if the virtual environment has been created by selecting the run code icon from main.py.

---

### Git Commands

#### Push to a new branch

- git push remoteName localBranchName:remoteNewBranchName

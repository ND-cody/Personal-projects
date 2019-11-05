import os
import sys

home = os.path.expanduser("~")

def flashcards(q, a):
    cards = {}
    questions = q
    answers = a

    i = 0
    for k in questions:
        cards[k] = answers[i]
        i += 1

    for k, v in cards.items():
        if k[-1] == "?":
            print(k)
        elif k[-1] != "?":
            print(k+"?")
        ans = input()
        if ans.lower() == v.lower():
            print("Correct!")
        else:
            print("Incorrect\nAnswer is: {}".format(v))

def create():
    questions = []
    answers = []
    n = int(input("How many flaschards would you like?\n"))
    i = 0
    while i < n:
        questions.append(input("Please enter your question:\n").capitalize())
        answers.append(input("Please enter your answer:\n").capitalize())
        i += 1
    return questions, answers

def new_cards():
    title = input("What subject are these flashcards on?\n")
    cwd = os.getcwd()
    exists = os.path.isfile(str(home) + "/.cmd-cards-files/" + str(title) + ".txt")
    if exists:
        print("You have already created flashcards on this subject.")
        print("Would you like to rename these flashcards?\n(Otherwise the current file will be overwritten)")
        choice = input("Y/N:    ")
        if choice.lower() == "yes" or choice.lower() == "y":
            title = input("What subject are these flashcards on?\n")

    questions, answers = create()

    with open(str(home) + "/.cmd-cards-files/" + str(title) + ".txt", "w+") as data:
        data.write(" ".join(questions) + "\n")
        data.write(" ".join(answers))

    print("Would you like to go through your flash card now?")
    yn = "x"
    while yn.lower() not in ("y", "n"):
        yn = input("Y/N:    ")
        if yn.lower() in "yes":
            flashcards(questions, answers)
            print("Thank you for using cmd cards!")
        elif yn.lower() in "no":
            print("Thank you for using cmd cards!")
        else:
            print("Not a valid input")

def old_cards():
    questions = []
    answers = []
    cards = os.listdir(str(home) + "/.cmd-cards-files/")
    for name in cards:
        print(" -" + name[:-4])
    print("What cards would you like to access?")
    title = input("Type the subject title here:     ")
    exists = os.path.isfile(str(home) + "/.cmd-cards-files/" + str(title) + ".txt")
    if exists:
        print("Would you like to add new questions to this topic or practice with currently existing cards?")
        appen = "x"
        while appen.lower not in ("add", "prac"):
            appen = input("Add/Prac:      ")
            if appen.lower() == "exit":
                break
            if appen.lower() in "prc":
                with open(str(home) + "/.cmd-cards-files/" + str(title) + ".txt", "r+") as src:
                    keys = src.readlines()
                    questions = keys[0].strip().split()
                    answers = keys[1].split()
                    flashcards(questions, answers)
                break
            elif appen.lower() in "add":
                with open(str(home) + "/.cmd-cards-files/" + str(title) + ".txt", "r+") as src:
                    keys = src.readlines()
                    questions = keys[0].strip().split()
                    answers = keys[1].split()
                    q, a = create()
                    questions.extend(q)
                    answers.extend(a)
                    src.seek(0)
                    src.truncate()
                    src.write(" ".join(questions) + "\n")
                    src.write(" ".join(answers))
                print("Questions added")
                break
            else:
                print("Not a valid input")

def main():
    try:
       os.mkdir(str(home) + "/" + ".cmd-cards-files")
       print("Welcome to cmd cards!")
       print("This program will create files to store your flashcards for specific subjects")
       print("This program will also create and edit files and a directory on your machine.")
       print("However you will not need to access or edit these files")
    except FileExistsError:
        print("Welcome to cmd cards!")
        print("Would you like to create new flash cards or access currently existing ones?")
        old_or_new = "x"
        while old_or_new not in ("old", "new"): 
            old_or_new = input("O/N:  ")
            if old_or_new.lower() in "new":
                new_cards()
            elif old_or_new.lower() in "old":
                old_cards()
            else:
                print("Not a valid input")
 
if __name__ == '__main__':
    main()

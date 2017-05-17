# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

rt = 1;
secretnum = 0;
numofguess = 0;


# helper function to start and restart the game
def new_game(r):
    # initialize global variables used in your code here
    global rt;
    global secretnum;
    global numofguess;

    if (r == 100):
        print "****New Game starts with Range [0,100)****\n";
        numofguess = 7;
        rt = 1;
        secretnum = random.randrange(0, 100);
        print "Number of Remaining Guesses is", numofguess;
    elif (r == 1000):
        print "****New Game starts with Range [0,1000)****\n";
        numofguess = 10;
        rt = 0;
        secretnum = random.randrange(0, 1000);
        print "Number of Remaining Guesses is", numofguess;
    # print secret_number;
    print "\n";


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    print "The Game Range has been changed to Range[0,100)";
    new_game(100);


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    print "The Game Range has been changed to Range[0,1000)";
    new_game(1000);


def input_guess(guess):
    # main game logic goes here
    guess = int(guess);
    global numofguess;
    print "Guess was", guess
    if (guess < secretnum):
        numofguess = numofguess - 1;
        print "Number of Available Guesses is", numofguess;
        print "Higher\n";
        if (numofguess == 0):
            print "Game Lost,Zero guesses available";
            if (rt == 0):
                new_game(1000);
            else:
                new_game(100);
    elif (guess > secretnum):
        numofguess = numofguess - 1;
        print "Number of Available Guesses is", numofguess;
        print "Lower\n";
        if (numofguess == 0):
            print "Game Lost,Zero guesses available";
            if (rt == 0):
                new_game(1000);
            else:
                new_game(100);
    else:
        numofguess = numofguess - 1;
        print "Number of Available Guesses is", numofguess;
        print "Correct\n";
        if (rt == 0):
            new_game(1000);
        else:
            new_game(100);


# create frame
frame = simplegui.create_frame("Guess the number Game", 300, 300);
frame.add_input("Enter the number", input_guess, 1500);
frame.add_button("RANGE [0,100)", range100);
frame.add_button("RANGE [0,1000)", range1000);

# register event handlers for control elements and start frame
frame.start();

# call new_game
new_game(100);


# always remember to check your completed program against the grading rubric


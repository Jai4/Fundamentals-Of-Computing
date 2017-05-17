# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    # fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        result = 0
    elif name == "Spock":
        result = 1
    elif name == "paper":
        result = 2
    elif name == "lizard":
        result = 3
    elif name == "scissors":
        result = 4
    return result

def number_to_name(number):
    # fill in your code below
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        result = "rock"
    elif number == 1:
        result = "Spock"
    elif number == 2:
        result = "paper"
    elif number == 3:
        result = "lizard"
    elif number == 4:
        result = "scissors"
    return result

def rpsls(playerchoice):
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name

    # print results
    print 'Player chooses', playerchoice;
    playernumber = name_to_number(playerchoice)
    computernumber = random.randrange(0, 5)
    print 'Computer chooses', number_to_name(computernumber)

    index=playernumber-computernumber;

    if index==0:
        print 'Player and Computer Tie!';
    elif index>0:
        if index==1 or index==2:
            print 'Player Wins!';
        else:
            print 'Computer Wins!';
    else:
        index=(playernumber-computernumber)%5;
        if index==1 or index==2:
            print 'Player Wins!';
        else:
            print 'Computer Wins!';
    print ;



# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
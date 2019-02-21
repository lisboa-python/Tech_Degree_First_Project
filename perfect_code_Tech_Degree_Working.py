import random

##################################################
# the out of range function
# gets called if the user puts a number thats out of the 1 to 10 range
def out_of_range():
    print("looks like that numebrs out of range")
    print("Try something between 1 and 10")
##################################################



def start_game():
##################################################
#generating the random number
    rand_int = random.randint(1, 10)
##################################################
#welcome statement
    print("Welcome to the game player one")
#input statement, that the while loop depends on
    game_play = input('Welcome to the game, would you like to play? Yes or No >>> ')
##################################################
# first if
# if they say 'no' then I get them out of the game right away
    if game_play.lower() == 'no':
        print("ok bye bye")
        exit()
##################################################
# if they said yes... then, we have a world of trouble for you haha
    elif game_play.lower() == 'yes':
##################################################
# set the number to 0, so that we can use it as a counter for the number of times the player tries
        number_of_guesses = 0
# while loop begins, if player said 'yes', then, some intersting things happen
        while game_play.lower() == "yes":
# first we ask for a number.
            raw_guess = input("Please pick a number >>> ")
# we put this try in here so if it's not a number, we can handle it eliquontly
            try:
# the input must be an integer. we make sure of that here
                guess = int(raw_guess)
# if its above 10
                if guess > 10:
# we call the out of range function up on line 6
                    out_of_range()
# hit continue if the numbe was bigger than 10, which takes us back to the top of the while loop to guess another digit
                    continue
# same as above, except with a 1, so I'm not going to go over it
                elif guess < 1:
                    out_of_range()
                    continue
# the humble except statement that prints out some nice things when we input some mean things
# still don't quit understand why we do the 'as err' part
# going to ask that in questions
            except ValueError as err:
                print("well that was painful, numbers between 1 and 10 only please")
# this else activates if we were good, and stayed within the 1 to 10
            else:
# if the guess, which is an int is bigger than the random int, then...
                if int(guess) > rand_int:
# print some stuff
                    print("It's lower")
# add one to the counter
                    number_of_guesses += 1
# print the number of total guesses
                    print("You've tried {} times".format(number_of_guesses))
# start back at the top
                    continue

# same as the above, so I won't cover it
                elif int(guess) < rand_int:
                    print("It's higher")
                    number_of_guesses += 1
                    print("You've tried {} times".format(number_of_guesses))
                    continue

# otherwise, you've won the game, so gtf out of here
                else:
                    print("got it")
                    print("good job, closing game")
                    number_of_guesses += 1
                    print("You've tried {} times".format(number_of_guesses))
# big diffrence here is the break statement, takes you right out of the game.
                    break

# this is here if, instead of a simple yes or not, we type something rediculous like 'bramble wood'
    else:
        print("Yes's and No's only please.")
        start_game()

start_game()


# print(
# '''
# The real question is how do we get this thing to do what we really want it to do
# The keepping of the score, becuase what fun is a fucking game if we can't keep score
# of who's a winner and who's a looser
#
# But to do this, we need to move the while loop up
#
# It needs to be one of the first things, and i'ts  a bit of a conundrum
#
# To do this, the entir ething needs to be re thought, from the ground up
# '''
# )

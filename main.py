#!/usr/bin/python
# assign point values to cards
    # let's use a python dictionary
import BJdictionary as bjdic
import random

# define main function
def main():
    print(bjdic.BJdict['AS'])
    print(bjdic.BJdict)
    print(bjdic.BJdict.keys)

# let's make the deck a list
    deck=list((bjdic.BJdict.keys()))

# shuffle the deck
    deck=random.shuffle(deck)
    
# deal to player 1
    # maybe deal can be a function
# deal to dealer
# count cards for player 1
# count cards for dealer


 ### I thought it was interactive for the player ? ###
# if card sum for player 1 <10 "hit"
# if card sum for player 1 >19 "stand"



# if card sum for dealer =< 17 "hit"
# if card sum for dealer => 18 "stand"
    # compare dealer the player to see who wins

if __name__ == '__main__':
    main()

import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_score = 0
dealer_hand = []
player_score = 0
player_hand = []
want_to_play = 'y'
print("welcome to python game blackjack!")
############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
while want_to_play == 'y':
    want_to_play = input('do you want to play Blackjack? type "y" or "n"')
    #If user types 'n' loop ends!
    if want_to_play.lower() == 'n':
        break
    
    #Dealer draws one concealed and one unconcealed card
    #Dealer also hands player his cards
    
    
    #does dealer have blackjack? NO? ok game continues!
     #case Dealer has, does the player also have a blackjack?
      #if he does it is a draw, if he doesn't, player loses!
      
   
   #player draw one more card?
   
   #if yes: is player_score > 21? player loser: draw one more card?
   #if no: if dealer_score =>17 : DEALER STANDS*
   #ELSE:DEALER DRAWS UNTIL SCORE >= 17*
   
   #IS player_score == dealer_score ? DRAW! :
   #player_score > 21 ? Player loses!:
   #Dealer_score >21? Player Wins!:
   # player_score>Dealer_score ? Player wins!
   # player_score<Dealer_score ? player loses!
      
    





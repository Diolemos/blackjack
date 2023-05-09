import art
import random
import dealer_actions 

player = {
        'score': 0,
        'hand': []  
           }
dealer = {
        'score': 0,
        'hand': []  
           }

    

    
'''
Hand out 2 cards for each participant
'''
for i in range(2):
    player['hand'].append(dealer_actions.deal_card())
    dealer['hand'].append(dealer_actions.deal_card())
player['score'] = dealer_actions.calculate_score(player['hand'])
dealer['score'] = dealer_actions.calculate_score(dealer['hand'])        


print(f" your cards are:{player['hand']}, current score: {player['score']}")
print(f"The dealer's first card is: {dealer['hand'][0]}")    
    
    

if player['score'] == 0 or dealer['score'] == 0 or player['score'] > 21:
    is_game_over = True
else:
    user_should_deal = input("Type 'y' to get a new card, type 'n' to pass")
    if user_should_deal == 'y':
        player['hand'].append(dealer_actions.deal_card())    
    else:
        is_game_over = True    

    
# is_game_over = False 

   
# print("welcome to python game blackjack!")




# # want_to_play == 'y':    
# #     want_to_play = input('do you want to play Blackjack? type "y" or "n"')
# #     #If user types 'n' loop ends!
# #     if want_to_play.lower() == 'n':
#         break
#     reset_game(player=player, dealer=dealer)
#     dealer_actions.hand_out_cards(deck=cards,player=player,dealer=dealer)
#     # print(f"testing , player just got:  {player['hand']} ")
#     # print(f"testing, dealer just got :  {dealer['hand']}")
#     #Dealer draws one concealed and one unconcealed card
#     #Dealer also hands player his cards
    
#     print(f"Dealer first card is [{dealer['hand'][0]}]")
#     print(f"Your hand  is {player['hand']}")
    
#     get_score(participant=player)
#     get_score(participant=dealer)
       
#     print(f"And your score is {player['score']}")
#     is_game_over = dealer_actions.check_for_win(player=player,dealer=dealer)
#     #does dealer have blackjack? NO? ok game continues!
#      #case Dealer has, does the player also have a blackjack?
#       #if he does it is a draw, if he doesn't, player loses!
      
#    #outer variables? if they're true, continue.
#     if is_game_over :
#         continue
#    #player draw one more card?
#    # player draw one more card?
# while not is_game_over:
#     draw_another_card = input("Want to draw another card?? type 'y' or 'n'")
#     if draw_another_card == 'y':
#         new_card = random.choice(cards)
#         #If player draws ace and his score's grater than 7, ace == 1
#         if new_card == 11 and player['score'] > 7:
#             new_card = 1  
#         player['hand'].append(new_card)
#         get_score(participant=player)
#         print(f"Dealer first card is [{dealer['hand'][0]}]")
#         print(f"Your hand  is {player['hand']}")
        
#         # draw another card
#         # if yes: is player_score > 21? player loser: draw one more card?
#         is_game_over = dealer_actions.check_for_win(player=player,dealer=dealer)
#         # if is_game_over :
#         #     continue
        
#     # Dealer's turn
#     elif draw_another_card == 'n':
#         print("Dealer's turn!")
#         if dealer['score']>=17:
#             is_game_over = dealer_actions.check_for_win(player=player,dealer=dealer)
#             # if is_game_over :
#             #     continue
#         else:
#             while dealer['score'] <= 17:
#                 new_card = random.choice(cards)
#                 if new_card > 10 and dealer['score'] > 7:
#                     new_card = 1 
#                 dealer['hand'].append(new_card)
#                 get_score(participant=dealer) 
                         
#             is_game_over = dealer_actions.check_for_win(player=player,dealer=dealer)
#             # if is_game_over :
#             #     continue
#     #if no: if dealer_score =>17 : DEALER STANDS*
#             #ELSE:DEALER DRAWS UNTIL SCORE >= 17* 
#             #dealers_turn()   
#             #if no: if dealer_score =>17 : DEALER STANDS*
#             #ELSE:DEALER DRAWS UNTIL SCORE >= 17* 
#             #dealers_turn()
   
#    #IS player_score == dealer_score ? DRAW! :
#    #player_score > 21 ? Player loses!:
#    #Dealer_score >21? Player Wins!:
#    # player_score>Dealer_score ? Player wins!
#    # player_score<Dealer_score ? player loses!
      
    





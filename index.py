import art
import os
import random
import dealer_actions 

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def play_game():
    
    print(art.logo_list[random.randint(0,1)])
    
    player = {
            'score': 0,
            'hand': []  
            }
    dealer = {
            'score': 0,
            'hand': []  
            }
    is_game_over = False
        

        
    '''
    Hand out 2 cards for each participant
    '''
    deck = dealer_actions.create_deck()
    for i in range(2):
        player['hand'].append(dealer_actions.deal_card(deck))
        dealer['hand'].append(dealer_actions.deal_card(deck))
        
    while not is_game_over:    
        
            
        player['score'] = dealer_actions.calculate_score(player['hand'])
        dealer['score'] = dealer_actions.calculate_score(dealer['hand'])        

        
        print(f" your cards are:{player['hand']}, current score: {player['score']}")
        print(f"The dealer's first card is: {dealer['hand'][0]}")    
            
            

        if player['score'] == 0 or dealer['score'] == 0 :
            is_game_over = True
           
        else:
            user_should_deal = input("Type 'y' to get a new card, type 'n' to pass")
            if user_should_deal == 'y':
                player['hand'].append(dealer_actions.deal_card(deck))   
                player['score']= dealer_actions.calculate_score(player['hand']) 
                if player['score'] >= 21:
                  is_game_over = True
            else: #"n"
                is_game_over = True    

        while dealer['score'] != 0 and dealer['score'] < 17 and player['score'] <= 21 :
            dealer['hand'].append(dealer_actions.deal_card(deck))
            dealer['score'] = dealer_actions.calculate_score(dealer['hand'])
    print(f"Dealer's final hand is {dealer['hand']} and his score is {dealer['score']}")
    print(f"Your final hand is {player['hand']} with a total score of {player['score']}")        
    print(dealer_actions.compare(player['score'],dealer['score']))        


while input("Do you want to play a game of Blackjack? type 'y' or 'n':") == 'y':
    cls()
    play_game()
        




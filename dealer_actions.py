import random

def deal_card():    
    #Deals one card
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return(card)       
    
def calculate_score(cards):
    """
    Receives the list of cards and returns the scores
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)       
    
def compare( player_score, dealer_score):
    if player_score == dealer_score:
        return "It's a Draw 😶 "
    elif dealer_score == 0:
        return 'You lose 🫨 Dealer has a Blackjack 😒 '
    elif player_score == 0:
        return "You win! 🏆 You got a Blackjack! 🏆 "
    elif player_score > 21:
        return "you lose, 😵 You went over 21 😵"
    elif dealer_score > 21:
        return "Dealer went over 21, 🤭 you Win!👍"
    elif player_score > dealer_score:
        return "You win 😎" 
    else:
        return "you lose 😑"
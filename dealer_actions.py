import random
# Create a full deck with all 52 cards
def create_deck():
    """Creates a standard deck of 52 cards"""
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  
    random.shuffle(deck)  # Shuffle deck at the start
    return deck

deck = create_deck()

def deal_card(deck):
    """Draws a card from the deck and removes it"""
    return deck.pop()


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "It's a Draw 😶"
    elif dealer_score == 0:
        return 'You lose 🫨 Dealer has a Blackjack 😒'
    elif player_score == 0:
        return "You win! 🏆 You got a Blackjack! 🏆"
    elif player_score > 21:
        return "You lose, 😵 You went over 21 😵"
    elif dealer_score > 21:
        return "Dealer went over 21, 🤭 you Win!👍"
    elif player_score > dealer_score:
        return "You win 😎"
    else:
        return "You lose 😑"
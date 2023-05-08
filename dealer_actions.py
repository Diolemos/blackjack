import random
def hand_out_cards(deck, dealer, player):
    """
    Distributes two cards each to the dealer and the player from a deck of cards.

    Args:
    - deck: A list of 13 integers representing a deck of cards. 
    - dealer_hand: A list representing the dealer's hand, initially containing two cards.
    - player_hand: A list representing the player's hand, initially containing two cards.

    Returns: None

    Modifies:
    - The dealer_hand and player_hand lists by replacing their initial values with two new random card values.

    Example Usage:
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_hand = [0, 0]
    player_hand = [0, 0]
    hand_out_cards(deck, dealer_hand, player_hand)

    In this example, the function distributes two random cards each to the dealer and the player from a deck of 13 cards,
    that can be pulled infinite times,
    and replaces the initial values of dealer_hand and player_hand with the new card values.
    """
    
    dealer['hand'].append(random.choice(deck))
    dealer['hand'].append(random.choice(deck))
    player['hand'].append(random.choice(deck))
    player['hand'].append(random.choice(deck))
    
    
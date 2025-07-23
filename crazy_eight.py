import random

def create_crazy_eight_deck():
    """
    Creates a standard 52-card deck for Crazy Eights.

    Args:
        shuffle (bool): Whether to shuffle the deck before returning.

    Returns:
        list[str]: A list of cards in the format 'Rank of Suit'.
    """
    # Define the four suits and thirteen ranks
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Create the deck by combining each rank with each suit
    deck = []
    for suit in suits:
        for rank in ranks:
            card = f"{rank} of {suit}"
            deck.append(card)

    random.shuffle(deck)

    return deck

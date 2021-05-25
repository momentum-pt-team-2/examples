import random
#Make a card game in Python like the card game War

# cards
# deck

# 2 players
player1 = []
player2 = []

# - make a deck
deck = []
table = []
# - in that deck, put 52 cards, 2 - A of each suit ♥️ ♣️ ♦️ ♠️
# 'J', 'Q', 'K', 'A'
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10]
suits = ['♥️', '♣️', '♦️', '♠️']

def make_deck(ranks_list, suits_list, deck):
    for suit in suits_list:
        for rank in ranks_list:
            deck.append((rank, suit))
            random.shuffle(deck)
    # TODO shuffle the deck

    for card in deck:
        print(card)

    return deck

# - deal cards out to each player, one at a time until all are gone
def deal_cards(deck, players):
    while len(deck) > 0:
        for player in players:
            card = deck.pop()
            player.append(card)

    print("Player 1 has " + str(len(player1)) + " cards")
    print("Player 2 has " + str(len(player2)) + " cards")

# - players throw down top card face up 
def turn(player1, player2):
    # TODO abstract the player putting down a card into its own function
    card1 = player1.pop()
    table.append(card1)
    print("player 1s card is " + str(card1))
    card2 = player2.pop()
    table.append(card2)
    print("player 2s card is " + str(card2))
    compare(card1, card2)
# - if cards are the same value, 
# deal out three more cards then one more face up, compare again

def compare(card1, card2):
    if card1[0] > card2[0]:
        print("Player 1 wins this round")
        while len(table) > 0:
            card = table.pop()
            player1.append(card)
    elif card2[0] > card1[0]:
        print("Player 2 wins this round")
        while len(table) > 0:
            card = table.pop()
            player1.append(card)
    else: 
        print("War!")
        while len(player1) > 0 and len(player2) > 0:
            for i in range(3):
                if len(player1) > 0 and len(player2) > 0:
                    card1 = player1.pop()
                    table.append(card1)
                    card2 = player2.pop()
                    table.append(card2)
            if len(player1) > 0 and len(player2) > 0:
                card1 = player1.pop()
                table.append(card1)
                print("player 1s card is " + str(card1))
                card2 = player2.pop()
                table.append(card2)
                print("player 2s card is " + str(card2))
                compare(card1, card2)




# - if not the same, player with higher card value gets the pile
# - play stops when one player runs out of cards, other player wins
def play_game(ranks, suits, deck, player1, player2):
    make_deck(ranks, suits, deck)
    deal_cards(deck, [player1, player2])
    while len(player1) and len(player2) > 0:
        turn(player1, player2)
    if len(player1) > 0:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

play_game(ranks, suits, deck, player1, player2)
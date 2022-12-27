import random

from art import logo 
# deal_card() function that uses the list to return a random card.
def deal_cards():
    """This function draws one card from the deck of cards. Here 11 is ace."""
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card = random.choice(cards)
    return card

# calculate_score() that takes a list of cards as input and return score
# Look up the sum() function
def calculate_scores(cards):
#  check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score.
#  0 will represent a blackjack in our game.
    if sum(cards)==21 and len(cards)==2:
        return 0
    # check for an 11 (ace). If the score is already over 21, 
    # remove the 11 and replace it with a 1. 
    # You might need to look up append() and remove().
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# compare function
def compare(user_score,dealer_score):
    if user_score == dealer_score:
        return "It's a Draw."
    elif dealer_score == 0:
        return "You lose, Opponent has a BlackJack"
    elif user_score == 0:
        return "You Win."
    elif user_score > 21:
        return "You lose you went over 21."
    elif dealer_score > 21:
        return "You Win, Opponent went over."
    elif user_score>dealer_score:
        return "You Win"
    else:
        return "You Lose."

def play_game():
    print(logo)
    user_cards = []
    dealer_cards = []
    is_gameover = False

    for _ in range(2):
        user_cards.append(deal_cards())
        dealer_cards.append(deal_cards())

    while not is_gameover:
        user_score = calculate_scores(user_cards)
        dealer_score = calculate_scores(dealer_cards)
        print(f"Your Cards: {user_cards}, Your Current Score is: {user_score}")
        print(f"Dealers Cards: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_gameover = True
        else:
            deal = input("Type 'y' to get another card, type 'n' to pass: \n")
            if deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_gameover= True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_cards())
        dealer_score = calculate_scores(dealer_cards)

    print(f"You Final hand is {user_cards}, Final Score: {user_score}")
    print(f"Dealer's hand is {dealer_cards}, Final Score: {dealer_score}")
    print(compare(user_score, dealer_score))

while input("Do you want to play a game of 21? Type 'y' or 'n': ")=="y":
    
    play_game()






    




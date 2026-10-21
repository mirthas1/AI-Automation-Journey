"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card in ('J','Q','K'):
        return 10
    point = 1 if card == 'A' else int(card)
    return point
    


def higher_card(card_one, card_two):
    #create two variables by calling the previous function then compare those and out
    if card_one in ("J","K","Q","10"):
        if card_two in ("J","K","Q","10"):
            return card_one,card_two
        return card_one
    if card_two in ("J","K","Q"):
        return card_two
    if card_one == "A" or card_two == "A":
        if card_one == card_two:
            return card_one,card_two
        elif card_two =="A":
            return card_one
        return card_two
    if int(card_one)>int(card_two):
        return card_one
    elif card_one == card_two:
        return card_one,card_two
    else:
        return card_two
    


def value_of_ace(card_one, card_two):
    if card_one is "A" or card_two is "A" or card_one in ("J","K","Q") or card_two in ("J","K","Q"):
        return 1 
    gun = 1 if (int(card_one)+int(card_two)) > 10 else 11
    return gun


def is_blackjack(card_one, card_two):
    if card_one in ("A","Q","J","K","10") and card_two is "A":
        if card_one == card_two:
            return False
        return True
    if card_two in ("Q","J","K","10") and card_one is "A":
        return True
    return False
    


def can_split_pairs(card_one, card_two):
    if card_one == card_two or (card_one in ("Q","J","K","10") and card_two in ("Q","J","K","10")):
        return True
    return False


def can_double_down(card_one, card_two):
    if card_one in ("Q","J","K","10","9","8") and card_two is "A" or card_two in ("Q","J","K","10","9","8") and card_one is "A":
        return True
    if card_one == 'A' or card_two is 'A':
            return False
    if (int(card_one)+int(card_two)) in (9,10,11):
        return True
    return False

    

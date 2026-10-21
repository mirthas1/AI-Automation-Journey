"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Return the value of a single card, with an Ace worth 1."""
    if card in {"J", "Q", "K"}:
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Return the higher card, or both if their values are equal."""
    value_one = 11 if card_one == "A" else value_of_card(card_one)
    value_two = 11 if card_two == "A" else value_of_card(card_two)
    if value_one == value_two:
        return card_one, card_two
    return card_one if value_one > value_two else card_two


def value_of_ace(card_one, card_two):
    """Return 11 if an Ace won't bust the hand, otherwise 1."""
    if card_one == "A" or card_two == "A":
        return 1
    if value_of_card(card_one) + value_of_card(card_two) <= 10:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Return True if the hand is a blackjack (Ace + 10-value card)."""
    if card_one == "A":
        return value_of_card(card_two) == 10
    if card_two == "A":
        return value_of_card(card_one) == 10
    return False


def can_split_pairs(card_one, card_two):
    """Return True if the two cards have the same value."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Return True if the hand totals 9, 10, or 11."""
    return value_of_card(card_one) + value_of_card(card_two) in {9, 10, 11}
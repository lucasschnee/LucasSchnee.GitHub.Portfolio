# Name: Lucas Schnee
# VUnetID: schneelj
# Email: lucas.j.schnee@vanderbilt.edu
# Class: CS 1104 - Vanderbilt University
# Section: 2
# Date: 4/2/22
# Honor statement: I attest that I understand the honor code for this class and have neither given
#                  nor received any unauthorized aid on this assignment.

# Program description:
# this program outputs 3 card poker hands based on a seed
import random

SUITS = ['C', 'D', 'H', 'S']

NAMES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

DECK_SIZE = 52

SUIT_SIZE = len(VALUES)

HAND_SIZE = 3


def get_card_value(deck):
    """
      gets 52 unique random values from 0 to 51 and puts them in the deck. removes the last card
      since 51 is a multiple of 3

        Parameters:
          deck: the "blank" deck of 52 1s

        Returns:
          the list "deck" with 51 unique values in a particular order

        """
    # Start of statements for the get_card_value function
    used_num = []

    for card in range(DECK_SIZE):
        card_same = True

        while card_same:
            value = random.randint(0, 51)

            if value not in used_num:
                card_same = False
                used_num.append(value)
                deck[card] = value
    deck.pop()
    return deck


def check_straight_flush(list_of_3_cards):
    """
      checks the 3 cards for straight flush. If true, makes value_check 1 so that straight and
      flush functions do not print anything. Else, keeps value_check at 0

        Parameters:
          list_of_3_cards: a given set of 3 cards

        Returns:
          value_check

        """
    # Start of statements for the get_card_value function
    list_of_3_cards.sort()

    if list_of_3_cards[0] // 13 == list_of_3_cards[1] // 13 == list_of_3_cards[2] // 13 and \
            list_of_3_cards[0] + 2 == list_of_3_cards[1] + 1 == list_of_3_cards[2]:
        print("--> Straight flush", end=" ")
        value_check = 1

    else:
        value_check = 0

    return value_check


def check_three_of_a_kind(list_of_3_cards):
    """
      checks the 3 cards for three of a kind. If true, makes value_check 1 so that pair
       function does not print anything. Else, keeps value_check at 0

        Parameters:
          list_of_3_cards: a given set of 3 cards

        Returns:
          value_check

        """
    # Start of statements for the get_card_value function
    if list_of_3_cards[0] % 13 == list_of_3_cards[1] % 13 == list_of_3_cards[2] % 13:
        print("--> Three of a kind", end=" ")
        value_check = 1

    else:
        value_check = 0

    return value_check


def check_straight(list_of_3_cards, value_for_straight_flush):
    """
      checks the 3 cards for a straight

        Parameters:
          list_of_3_cards: a given set of 3 cards
          value_for_straight_flush: either 0 or 1 to dictate the output of this function

        """
    # Start of statements for the check_straight function
    if value_for_straight_flush == 0:
        straight_list_check = []

        for card in range(len(list_of_3_cards)):
            straight_list_check.append(list_of_3_cards[card] % 13)
            straight_list_check.sort()

        if (straight_list_check[0] % 13) + 2 == (straight_list_check[1] % 13) + 1 == (
                straight_list_check[2] % 13):
            print("--> Straight", end=" ")


def check_flush(list_of_3_cards, value_for_straight_flush):
    """
      checks the 3 cards for a flush

        Parameters:
          list_of_3_cards: a given set of 3 cards
          value_for_straight_flush: either 0 or 1 to dictate the output of this function

        """
    # Start of statements for the check_flush function
    if value_for_straight_flush == 0:

        if list_of_3_cards[0] // 13 == list_of_3_cards[1] // 13 == list_of_3_cards[2] // 13:
            print("--> Flush", end=" ")


def check_pair(list_of_3_cards, value_for_three_of_a_kind):
    """
      checks the 3 cards for a pair

        Parameters:
          list_of_3_cards: a given set of 3 cards
          value_for_three_of_a_kind: either 0 or 1 to dictate the output of this function

        """
    # Start of statements for the check_pair function
    if value_for_three_of_a_kind == 0:

        if not list_of_3_cards[0] % 13 != list_of_3_cards[1] % 13 != list_of_3_cards[2] % 13 \
               != list_of_3_cards[0] % 13:
            print("--> Pair", end=" ")


def check_five_special_hands(list_of_3_cards):
    """
      runs all the checks for special hands

        Parameters:
          list_of_3_cards: a given set of 3 cards

        """
    # Start of statements for the check_five_special_hands function
    value_for_straight_flush = check_straight_flush(list_of_3_cards)
    value_for_three_of_a_kind = check_three_of_a_kind(list_of_3_cards)
    check_straight(list_of_3_cards, value_for_straight_flush)
    check_flush(list_of_3_cards, value_for_straight_flush)
    check_pair(list_of_3_cards, value_for_three_of_a_kind)


def results(deck_values):
    """
      prints the deck in groups of 3 cards and runs a function to check for special hands

        Parameters:
          deck_values: the deck of 51 unique numbers representing cards in a deck

        """
    # Start of statements for the results function
    counter = 0
    list_of_3_cards = []

    for card in range(len(deck_values)):

        if len(NAMES[deck_values[card] % 13] + SUITS[deck_values[card] // 13]) == 3:
            print(NAMES[deck_values[card] % 13] + SUITS[deck_values[card] // 13], end=" ")

        else:
            print(" " + NAMES[deck_values[card] % 13] + SUITS[deck_values[card] // 13], end=" ")

        counter += 1
        list_of_3_cards.append(deck_values[card])

        if counter == 3:
            check_five_special_hands(list_of_3_cards)
            counter = 0
            print()
            list_of_3_cards = []


def main():
    seed = int(input('Enter a seed: '))
    random.seed(seed)
    deck = [1 for _ in range(DECK_SIZE)]
    print("=== Results")
    deck_values = get_card_value(deck)
    results(deck_values)
    print("===========")


if __name__ == '__main__':
    main()

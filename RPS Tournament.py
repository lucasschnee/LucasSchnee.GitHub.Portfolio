# Name: Lucas Schnee
# VUnetID: schneelj
# Email: lucas.j.schnee@vanderbilt.edu
# Class: CS 1104 - Vanderbilt University
# Section: 2
# Date: 4/9/22
# Honor statement: I attest that I understand the honor code for this class and have neither given
#                  nor received any unauthorized aid on this assignment.

# Program description:
# this program runs an advanced rock paper scissors tournament with two different
# phases depending on whether two people are left
import random

space = " "

CHOICE = ['Rock', 'Paper', 'Scissors']


def num_players_calc():
    """
      gets the number of players(amount has to be three or more)

        Returns:
          num_players

        """
    # Start of statements for the num_players_calc function
    num_player_check = True
    num_players = input("Enter number of players: ")

    while num_player_check:

        if num_players.isnumeric():

            if int(num_players) <= 2:
                num_players = input("Must be at least 3, try again: ")

            else:
                num_player_check = False

        else:
            num_players = input("Must be a number, try again: ")

    num_players = int(num_players)
    return num_players


def names_of_players_calc(num_players):
    """
      gets the names of the players(amount has to equal num_players)

        Parameters:
          num_players: the number of players

        Returns:
          names_of_players_list

        """
    # Start of statements for the names_of_players_calc function
    names_of_players = input("Enter names of players: ")
    names_of_players_list = names_of_players.split()
    same_num_test_for_names = True

    while same_num_test_for_names:

        if len(names_of_players_list) == num_players:
            same_num_test_for_names = False

        else:
            names_of_players = input("Must enter " + str(num_players) + " names, try again: ")
            names_of_players_list = names_of_players.split()

    return names_of_players_list


def game_header(names_list):
    """
      prints the header of the output with the inputted names

        Parameters:
          names_list: the list of names

        """
    # Start of statements for the game_header function
    print("==========" * len(names_list))

    for name in names_list:

        amount_space = 10 - len(name)

        if amount_space % 2 == 1:
            print(space * int((amount_space - 1) / 2) + name + space * int((amount_space + 1) / 2), end="")

        else:
            print(space * int(amount_space / 2) + name + space * int(amount_space / 2), end="")
    print()
    print("==========" * len(names_list))


def phase_1_of_game(names_list):
    """
      plays the first game until there are only two people left where the majority rps "wins"

        Parameters:
          names_list: the list of names

        Returns:
          names_list (with "Out" for all but two people)

        """
    # Start of statements for the phase_1_of_game function
    while names_list.count("Out") < len(names_list) - 2:

        outcome_for_name = []
        for name in names_list:

            if name == "Out":
                print("    X     ", end="")
                choice = "X"

            else:
                choice = random.randint(0, 1)

                if choice == 1:
                    print("  Paper   ", end="")

                else:
                    print("   Rock   ", end="")

            outcome_for_name.append(choice)

        print()

        if outcome_for_name.count(0) > outcome_for_name.count(1):

            for name in range(len(names_list)):

                if outcome_for_name[name] == 1:
                    names_list[name] = "Out"

        if outcome_for_name.count(1) > outcome_for_name.count(0):

            for name in range(len(names_list)):

                if outcome_for_name[name] == 0:
                    names_list[name] = "Out"

    return names_list


def phase_2_of_game(names_list):
    """
      continues the game when there are only two people left with normal rps
      returns the winner, prints X for people that are out for each go

        Parameters:
          names_list: the list of names

        Returns:
          winner

        """
    # Start of statements for the phase_2_of_game function
    winner = ""
    while names_list.count("Out") < len(names_list) - 1:

        outcome_for_name = []

        for name in names_list:

            if name == "Out":
                print("    X     ", end="")
                choice = "X"

            else:

                choice = random.randint(0, 2)

                if choice == 1:
                    print("  Paper   ", end="")

                elif choice == 0:
                    print("   Rock   ", end="")

                else:
                    print(" Scissors ", end="")

            outcome_for_name.append(choice)

        print()


        winner = return_winner(outcome_for_name, names_list)


def return_winner(outcome_for_name, names_list):
    """
      returns the winner if phase2 has completed

        Parameters:
          outcome_for_name: the outcome for each round of the game(rps or X)
          names_list: the list of names

        """
    # Start of statements for the return_winner function
    if 0 in outcome_for_name and 1 in outcome_for_name:
        outcome_for_name[outcome_for_name.index(0)] = "Out"
        return names_list[outcome_for_name.index(1)]

    elif 1 in outcome_for_name and 2 in outcome_for_name:
        outcome_for_name[outcome_for_name.index(1)] = "Out"
        return names_list[outcome_for_name.index(2)]

    elif 0 in outcome_for_name and 2 in outcome_for_name:
        outcome_for_name[outcome_for_name.index(2)] = "Out"
        return names_list[outcome_for_name.index(0)]

    else:
        return ""




def outcome(names_list, winner):
    """
      prints the winner

        Parameters:
          names_list: the list of names(for formatting)
          winner: the winner of the game

        """
    # Start of statements for the outcome function
    print("==========" * len(names_list))
    print("{} won.".format(winner))


def main():
    seed = int(input('Enter a seed: '))
    random.seed(seed)
    num_players = num_players_calc()
    names_list = names_of_players_calc(num_players)
    game_header(names_list)
    names_list = phase_1_of_game(names_list)
    winner = phase_2_of_game(names_list)
    outcome(names_list, winner)


if __name__ == '__main__':
    main()

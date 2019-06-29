#!/usr/bin/env python3

import random
import time

# testfile cards
deck = [
    {"name": "prickler", "age": 10, "attack": 40, "speed": 38, "clever": 18},
    {"name": "ghost", "age": 10, "attack": 50, "speed": 10, "clever": 33},
    {"name": "eartch", "age": 35, "attack": 78, "speed": 4, "clever": 7},
    {"name": "axar", "age": 4, "attack": 50, "speed": 3, "clever": 28},
    {"name": "hacker", "age": 24, "attack": 5, "speed": 23, "clever": 20},
    {"name": "igna", "age": 29, "attack": 33, "speed": 7, "clever": 2},
    {"name": "kracken", "age": 40, "attack": 28, "speed": 9, "clever": 8},
    {"name": "loxer", "age": 12, "attack": 44, "speed": 30, "clever": 18},
    {"name": "joker", "age": 12, "attack": 40, "speed": 38, "clever": 18},
    {"name": "mother", "age": 17, "attack": 50, "speed": 10, "clever": 33},
    {"name": "gistari", "age": 35, "attack": 78, "speed": 4, "clever": 7},
    {"name": "ballray", "age": 4, "attack": 50, "speed": 3, "clever": 28},
    {"name": "patient3", "age": 4, "attack": 5, "speed": 23, "clever": 20},
    {"name": "ignahell", "age": 29, "attack": 33, "speed": 7, "clever": 2},
    {"name": "rapidsham", "age": 40, "attack": 28, "speed": 9, "clever": 8},
    {"name": "sxiom", "age": 40, "attack": 44, "speed": 30, "clever": 18},
]


def show_deck(cards):
    for card in cards:
        print(card)


def shuffle(deck):
    random.shuffle(deck)
    return deck


def deal_card(deck):
    card = deck.pop()
    return card


def show_card(hand):
    i = 0
    for k, v in hand.items():
        if i == 0:
            print("Monster:", v)
        else:
            print(f"{i}. {k}  \t{v}")
        i += 1


def deal_deck(players_hand, cards):
    i = 0
    for card in cards:
        time.sleep(0.1)
        print(f"Card dealt to player {i + 1}")
        players_hand[i].append(card)
        i += 1
        if i == len(players_hand):
            i = 0
    return players_hand


def create_player(player_count):
    players_hand = []
    for i in range(player_count):
        print(f"Player {i + 1} has joined")
        players_hand.append([])
    return players_hand


def check_user_input(user_select, menu_items):
    try:
        user_select = int(user_select)
        if user_select in list(range(1, menu_items + 1)):
            return user_select
        else:
            print("Not a valid choice")
    except ValueError:
        print("That ain't a number fool")


def game_main(players_amount, players_hand):

    stat_choice = {1: "age", 2: "attack", 3: "speed", 4: "clever"}
    current_player = 0
    current_round = []
    compare_stats = []
    players_amount = int(players_amount)

    for i in range(players_amount):
        drawn = deal_card(players_hand[i])
        current_round.append(drawn)

    while True:
        show_card(current_round[current_player])
        user_select = input("Pick an attribute. ")
        user_select = check_user_input(user_select, 4)
        if user_select not in range(1, 5):
            print("Please try again\n")
        else:
            stat_type = stat_choice[user_select]
            print(f"You picked {stat_type}\n")
            break

    # for i in range(players_amount):
    p_no = 1
    for hand in current_round:
        stat_amount = hand[stat_choice[user_select]]
        print(f"Player {p_no} had {stat_amount} for {stat_type}")
        compare_stats.append(stat_amount)
        p_no += 1

    max_value = max(compare_stats)
    print("Max Value is", max_value)
    res_list = [i for i, value in enumerate(compare_stats) if value == max_value]
    print("Indices:", res_list)


# Game Menu
def play_game():
    print("Hello weakling")
    while True:
        how_many_players = input("Please select how many players (1 to 6)?\n> ")
        players_amount = check_user_input(how_many_players, 6)
        if players_amount != None:
            print("Great")
            break
        else:
            print()
    print(f"Thanks. You selected {players_amount} players")
    print("Please take your seats... while I shuffle the cards")
    random.shuffle(deck)
    players = create_player(players_amount)
    print("Dealing cards...")
    players_hand = deal_deck(players, deck)
    game_main(how_many_players, players_hand)


# Start Menu
def start():
    print("\nHello and welcome to Hayden's Trump Cards Game!\n")
    while True:
        print("+++ Main Menu +++")
        print("1. Play Game")
        print("2. Exit Game")
        user_select = input("> ")

        user_select = check_user_input(user_select, 2)
        if user_select == 1:
            play_game()
        elif user_select == 2:
            break
        else:
            print("Pick again")
    print("Goodbye...")


start()

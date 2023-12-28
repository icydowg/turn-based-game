from time import sleep
import os

delay = 0.05

def name_and_stats(players: list, names: list):
    '''Displays names of players with stats neatly'''
    sleep(delay)
    os.system("cls")
    just_length = len(max(names)) + 6
    for player in players:
        status, turns = player.silenced
        print(player.name.center(just_length, "-"))
        print(f"HP: {player.health}")
        print(f"SP: {player.stamina}")

        if status:
            print(f"Status: silenced [{turns}]")
        else:
            print("Status: normal")
        
        print("\n")
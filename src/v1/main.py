# import time
# from v1 import ( Dice, Game, GameBoard, Node )
from v1.dice import Dice
from v1.game import Game
from v1.game_board import GameBoard
from v1.node import Node


def __delay():
    # time.sleep(1)
    pass


def run_game_multi_player() -> None:
    game = Game(GameBoard(10))

    dice = Dice()

    players_all = [
        "Tom",
        "Jerry",
        "Donald",
        "Micky",
        "Goofy",
    ]

    # mapped = map(game.register_player, (p for p in players_all))

    # map(game.register_player, players_all)
    game.who_registered_so_far()

    game.register_players(players_all)

    game.start_game()
    game.who_registered_so_far()

    while game.is_game_still_on():
        game.start_iteration()
        for player in game.players_playing:
            game.player_rolls(player, dice.roll())

        # game.who_finished_so_far()
        # game.who_are_still_playing()

        game.end_iteration()
        print("\n--------------")
        __delay()

    # print("==============")
    game.who_finished_so_far()
    game.who_are_still_playing()


def walk_linked_list(node: Node) -> None:
    print("Start: walk_linked_list")

    current_node = node
    while(current_node is not None):
        print(current_node)
        current_node = current_node.next
        # time.sleep(1)

    print("End: walk_linked_list")


if __name__ == "__main__":
    print("######################")
    print("######################")
    run_game_multi_player()

from v1.node import Node


class Player:
    def __init__(self, name: str, start_postion: Node = None):
        self.name = name
        self.current_position = start_postion

    def __str__(self):
        return "Player[name = {}, current_position = {}]".format(self.name, self.current_position)

    def where_are_you(self) -> None:
        return "{} is now at {}.".format(self.name, self.current_position.value)
        # return "Player[{}]: location = [{}]".format(self.name, self.current_position)

    def move(self, steps: int) -> None:
        # TODO revisit: plamement of this method
        # print("Player: starting node = [{}]".format(self.current_position))

        # if self.have_you_finished_the_game():
        #     print("Player: You already finished the game.")
        #     return

        positions_moved = 0
        moving_to = self.current_position

        while(positions_moved < steps):
            if self.__can_move_to(moving_to.next):
                positions_moved += 1
                moving_to = moving_to.next
            else:
                break

        self.current_position = moving_to

        # print("steps requested = {}, moved = {}".format(steps, positions_moved))
        # print("Player: ending node = [{}]".format(self.current_position))

    def __can_move_to(self, node: Node) -> bool:
        # TODO revisit: plamement of this method
        # print("\tPlayer: testing a move to node = [{}]".format(node))
        return node is not None

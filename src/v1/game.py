from v1.game_board import GameBoard
from v1.player import Player
from utils import logging_config
import utils.game_helpers as game_helpers


logger = logging_config.configure('logging.json', __name__)


class Game:
    ##############################################
    def __init__(self, game_board: GameBoard):
        logger.debug("Game: Initilization starting...")

        self.game_board = game_board
        self.__initialize()

        logger.debug("Game: Initilization complete")

    def __initialize(self) -> None:
        self.__players_all = []
        self.__players_playing = []
        self.__players_finished = []
        self.__has_game_started = False
        self.__has_game_ended = False
        self.__iterations = 0
        self.__iteration_on_going = False

    def reset(self) -> None:
        logger.info("Resetting the game....")
        self.__initialize()

    ##############################################
    @property
    def iterations(self) -> int:
        return self.__iterations

    @property
    def players_all(self) -> list:
        return self.__players_all.copy()

    @property
    def players_playing(self) -> list:
        return self.__players_playing.copy()

    @property
    def players_finished(self) -> list:
        return self.__players_finished.copy()
    ##############################################

    def info(self) -> None:
        '''
        Prints current state of the game

        :rtype: None
        '''
        logger.info("TBD")

    def who_registered_so_far(self) -> None:
        print("\nWho registered so far:")

        for player in self.__players_all:
            print("\t{}".format(player.where_are_you()))

    def who_finished_so_far(self) -> None:
        print("\nWho finished so far:")

        for player in self.__players_finished:
            print("\t{}".format(player.where_are_you()))

    def who_are_still_playing(self) -> None:
        print("\nWho are still playing:")

        for player in self.__players_playing:
            print("\t{}".format(player.where_are_you()))

    def register_player(self, name: str) -> bool:
        '''
        registers a player. Checks for duplicate names.

        :return: True for success, False for failure
        :rtype: bool
        '''
        if self.__has_game_started:
            logger.warning("The game has started. Cannot add anymore player.")
            return False

        found_player = game_helpers.find_player_by_name(self.__players_all, name)
        if found_player:
            logger.warning("Player {} is already registered in the game.".format(name))
            return False

        self.__players_all.append(Player(name, self.game_board.start_node))
        logger.info("Player {} is now registered in the game.".format(name))
        return True

    def register_players(self, names: list) -> bool:
        if self.__has_game_started:
            logger.warning("The game has started. Cannot add anymore player.")
            return False

        # TODO try map() one more time
        for name in names:
            self.register_player(name)

        # TODO return collective status, or list of individual statuses
        return True

    def start_game(self) -> bool:
        if len(self.__players_all) == 0:
            logger.warning('Cannot start game with no registered players')
            return False

        if self.__has_game_started:
            logger.warning('Game has already started. Cannot start it again.')
            return False

        self.__has_game_started = True
        self.__players_playing = self.__players_all.copy()
        return True

    def player_rolls(self, player: Player, roll: int) -> None:
        # TODO validate player is in the game, differently
        # TODO ensure player order
        if player not in self.__players_all:
            print("Game: Player {} is not registered in the game.".format(player.name))
            return

        player.move(roll)
        if self.__have_player_finished_the_game(player):
            self.__player_finished_game(player)
            other_message = "Congratulations, {}! You finished the game.".format(player.name)
        else:
            other_message = ""

        print("{} rolls {}. {} {}".format(player.name, roll, player.where_are_you(), other_message))

    def __player_finished_game(self, player: Player) -> None:
        self.__players_finished.append(player)

    def __have_player_finished_the_game(self, player: Player) -> bool:
        return self.game_board.is_last_node(player.current_position)

    def start_iteration(self) -> bool:
        '''
        starts an iteration.

        :return: True on success, False on failure
        :rtype: bool
        '''
        if not self.is_game_still_on():
            logger.warning('Cannot start iteration - Game has not started yet. Start the game first')
            return False

        if self.__iteration_on_going:
            logger.warning('Cannot start iteration - iteration {} is ongoing. '
                           'Finish it before starting a new one'.format(self.__iterations))
            return False

        self.__iteration_on_going = True
        self.__iterations += 1
        return True

    def end_iteration(self) -> bool:
        if not self.__iteration_on_going:
            logger.warning('Cannot end iteration - no active iteration.')
            return False

        for player in self.__players_finished:
            if player in self.__players_playing:
                self.__players_playing.remove(player)
                logger.debug('Removing player {} from the next iteration'.format(player.name))

        if len(self.__players_playing) == 0:
            self.__has_game_ended = True
            logger.info('No player remains in the game. This is the last iteration')

        self.__iteration_on_going = False
        return True

    def is_game_still_on(self) -> bool:
        return self.__has_game_started and not self.__has_game_ended

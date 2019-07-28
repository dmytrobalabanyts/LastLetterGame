import random
import json
import Utils
from BaseClass import BaseClass, common_queue

class Game(BaseClass):
    """The main class that provides functionality of the game. 
    The only public method is 'go()' which ruhs a game"""
    def __init__(self, player1, player2, state_machine, restore = False):
        """Supply the game object with player objects and state machine object"""
        super().__init__()
        self.__players[0] = player1
        self.__players[1] = player2
        self.__player_names[player1] = 'Human'
        self.__player_names[player2] = 'Bot'
        self.__state_machine = state_machine

    def run(self):
        self.go()

    def go(self):
        """The method runs the new game"""
        self.__last_word = ''
        result = 'first_turn'
        random.seed()
        self.__current_player = random.randint(0, 1)

        while True: 
            if result == 'first_turn':
                answer = self.__notify_user(self.__players[self.__current_player], 'first_turn', self.__last_word)
            elif result == 'rejected':
                self.__current_player = 1 - self.__current_player
                self.__last_word = self.__previous_word
                answer = self.__notify_user(self.__players[self.__current_player], 'repeat_turn', self.__last_word)
            elif result == 'wrong_letter':
                answer = self.__notify_user(self.__players[self.__current_player], 'wrong_letter', self.__last_word)
            elif result == 'already_used':
                answer = self.__notify_user(self.__players[self.__current_player], 'already_used', self.__last_word)
            elif result == 'not_exist':
                answer = self.__notify_user(self.__players[self.__current_player], 'not_exist', self.__last_word)
            elif result == 'validated':
                self.__previous_word = self.__last_word
                self.__last_word = answer
                self._save_state()
                self.__current_player = 1 - self.__current_player
                answer = self.__notify_user(self.__players[self.__current_player], 'your_turn', self.__last_word)
            elif result == 'stop_game':
                return

            result = self.__validate_word(answer)

    def __validate_word(self, word):
        if word[0] == '-':
            return 'rejected'
        elif word[0] == '!':
            return 'stop_game'
        elif self.__last_word != '' and word[0] != self.__last_word[-1]:
            return 'wrong_letter'
        answer = self.__notify(self.__state_machine, 'validate', word)
        result = json.loads(answer)
        return result['answer']  

    def __notify_user(self, address, notification, data):
        self.send(self.__player_names[address], Utils.format_notification(notification, data))
        addr_from, response, tag = self.receive()

        answer = json.loads(response)
        if answer['command'] == 'next_word':
            return answer['data']

    def __notify(self, address, notification, data):
        self._save_state()
        return address.notify(Utils.format_notification(notification, data))

    __players = [None, None]
    __player_names = {}
    __current_player = 0
    __state_machine = None
    __last_word = ''
    __previous_word = ''
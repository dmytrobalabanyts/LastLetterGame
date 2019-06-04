import random
import json
import Utils

class Game(object):
    """description of class"""
    def __init__(self, player1, player2, state_machine):
        self.__players[0] = player1
        self.__players[1] = player2
        self.__state_machine = state_machine

    def go(self):
        self.__game_is_going = True
        random.seed()
        current_player = random.randint(0, 1)

        while(not self.__word_accepted):
            self.__last_word = self.__get_first_word()
            answer = self.__notify(self.__players[current_player], "first_turn", self.__last_word)
            self.__translate_answer(answer)

        while(self.__game_is_going):
            if self.__word_accepted:
                while not self.__validate_word(self.__last_word):
                    answer = self.__notify(self.__players[current_player], "repeat_turn", self.__last_word)
                    self.__translate_answer(answer)

                self.__add_to_used_words(self.__last_word)
                self.__save_state()

                current_player = 1 - current_player

                answer = self.__notify(self.__players[current_player], "your_turn", self.__last_word)
            else:
                answer = self.__notify(self.__players[1 - current_player], "repeat_turn", self.__last_word)
            self.__translate_answer(answer)

    def __get_first_word(self):
        start_letter = 'abcdefghijklmnopqrstuvwxyz'[random.randint(0, 25)]
        return start_letter

    def __translate_answer(self, answer):
        if answer[0] == '-':
            self.__word_accepted = False
            return
        self.__word_accepted = True
        self.__last_word = answer

    def __add_to_used_words(self, word):
        self.__notify(self.__state_machine, 'used', word)

    def __validate_word(self, word):
        answer = self.__notify(self.__state_machine, 'validate', word)
        result = json.loads(answer)
        return result['answer'] == "validated"  

    def __notify(self, address, notification, data):
        return address.notify(Utils.format_command(notification, data))

    def __save_state(self):
        pass

    __players = [None, None]
    __state_machine = None
    __word_accepted = False
    __game_is_going = False
    __last_word = ''
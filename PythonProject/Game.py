import random

class Game(object):
    """description of class"""
    def __init__(self, player1, player2, state_machine):
        self._player1 = player1
        self._player2 = player2
        self._state_machine = state_machine

    def start(self):
        self._game_is_going = True
        random.seed()
        if random.randint(0, 1):
            self._current_player = self._player1
        else:
            self._current_player = self._player2
        while(not self._word_accepted):
            self._last_word = self._get_first_word()
            answer = self._notify("your_turn", self._last_word)
            self._translate_answer(answer)

        while(self._game_is_going):
            while not self._validate_word(self._last_word):
                answer = self._notify("repeat_turn", self._last_word)
                translate_answer(answer)

            self._state._add_to_used_words(self._last_word)
            _save_state()

            if self._current_player is _player1:
                self._current_player = _player2
            else:
                self._current_player = _player1

            self._notify("your_turn", self._last_word)

    def _get_first_word(self):
        start_letter = 'abcdefghijklmnopqrstuvwxyz'[random.randint(0, 25)]
        return 'You go first. Start with a word on ' + start_letter

    def _notify(self, notification, data):
        self._last_answer = self._current_player.notify('notification=' + notification + '; data=' + data)

    def _translate_answer(self, answer):
        self._word_accepted = True

    def _add_to_used_words(self, word):
        self._state._add_to_used_words(word)

    _player1 = None
    _player2 = None
    _state_machine = None
    _word_accepted = False
    _game_is_going = False
    _last_word = ''
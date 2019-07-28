import json
import Utils
from BaseClass import BaseClass

class State(BaseClass):
    """This class implements the state machine for the "Last Letter" game
    Possible commands:
        command - 'validate'
        data - word to be checked"""
    def __init__(self, dictionary):
        super().__init__()
        self.__dictionary = dictionary

    def notify(self, string):
        """the only published method. All the class interface is provided
        by its commands and their data supplied in the string"""
        notification = json.loads(string)
        if notification['command'] == 'validate':
            valid = self.__word_validator(notification['data'])
            if valid == 'valid':
                self.__add_to_used_words(notification['data'])
                result = '{"answer": "validated"}'
            elif valid == 'already_used':
                self.__add_to_used_words(notification['data'])
                result = '{"answer": "already_used"}'
            elif valid == 'not_exist':
                result = '{"answer": "not_exist"}'
            self._save_state()
            return result

    def __word_validator(self, word):
        word_is_correct = True
        if  self.__word_was_used(word):
            return 'already_used'
        if not self.__word_exists(word):
            return 'not_exist'
        else:
            return 'valid'

    def __add_to_used_words(self, last_word):
        self.__used_words.add(last_word)

    def __word_exists(self, word):
        answer = self.__notify(self.__dictionary, Utils.format_notification('check', word))
        result = json.loads(answer)
        if result['command'] == 'answer' and result['data'] == 'exists':
            return True
        else:
            return False

    def __notify(self, address, notification):
        return address.notify(notification)

    def __word_was_used(self, word):
        return word in self.__used_words

    __dictionary = None
    __used_words = set()

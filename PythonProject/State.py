import json
import Utils

class State(object):
    """description of class"""
    def __init__(self, dictionary):
        self.__dictionary = dictionary

    def __add_to_used_words(self, last_word):
        self.__used_words.add(last_word)

    def notify(self, string):
        notification = json.loads(string)
        if notification['command'] == 'validate':
            result = self.__word_validator(notification['data'])
            if result == 'valid':
                return '{"answer": "validated"}'
            elif result == 'already_used':
                return '{"answer": "already_used"}'
            elif result == 'not_exist':
                return '{"answer": "not_exist"}'
        elif notification['command'] == 'used':
            self.__add_to_used_words(notification['data'])

    def __word_validator(self, word):
        word_is_correct = True
        if  self.__word_was_used(word):
            return 'already_used'
        if not self.__word_exists(word):
            return 'not_exist'
        else:
            return 'valid'

    def __word_exists(self, word):
        return True

    def __word_was_used(self, word):
        return word in self.__used_words

    __dictionary = None
    __used_words = set()

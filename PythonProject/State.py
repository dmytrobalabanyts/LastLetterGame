import json
import Utils

class State(object):
    """description of class"""
    def __init__(self, dictionary):
        self.__dictionary = dictionary

    def __add_to_used_words(self, last_word):
        self.__used_words.add(__last_word)

    def notify(self, string):
        notification = json.loads(string)
        if notification['command'] == 'validate':
            return '{"answer": "validated"}'
        elif notification['command'] == 'used':
            if self.__word_validator(notification['data']):
                return '{"answer": "validated"}'
            else:
                return '{"answer": "invalidated"}'

    def __word_validator(self, word):
        word_is_correct = True
        if word in self.__used_words:
            word_is_correct = False
        return word_is_correct

    __dictionary = None
    __used_words = set()

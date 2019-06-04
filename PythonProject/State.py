import json
import Utils

class State(object):
    """description of class"""
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __add_to_used_words(self, __last_word):
        pass

    def notify(self, string):
        notification = json.loads(string)
        if notification['command'] == 'validate':
            return '{"answer": "validated"}'
        elif notification['command'] == 'used':
            return '{"answer": "null"}'

    dictionary = None



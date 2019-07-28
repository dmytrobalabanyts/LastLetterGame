import json
import Utils
from BaseClass import BaseClass

class Dictionary(BaseClass):
    """This class provides a possibility to check whether the word exists or not.
    Possible commands:
        command - 'check'
        data - word to be checked"""
    def __init__(self, arguments, restore = False):
        super().__init__()
        with open('..\\Auxilary\\MainWordDatabase\\nouns.txt') as f:
            Dictionary.__words = f.readlines()

    def notify(self, string):
        """the only published method. All the class interface is provided
        by its commands and their data supplied in the string"""
        notification = json.loads(string)
        if notification['command'] == 'check':
            word = notification['data'] + '\n'
            result = word in Dictionary.__words
            self._save_state()
            if result:
                return Utils.format_notification('answer', 'exists')
            else:
                return Utils.format_notification('answer', 'not_exists')
    
    __words = list()



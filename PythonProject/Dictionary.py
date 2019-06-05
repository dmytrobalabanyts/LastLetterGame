import json
import Utils

class Dictionary(object):
    """description of class"""
    def __init__(self, arguments):
        with open('..\\Auxilary\\MainWordDatabase\\nouns.txt') as f:
            Dictionary.__words = f.readlines()

    def notify(self, string):
        notification = json.loads(string)
        if notification['command'] == 'check':
            word = notification['data'] + '\n'
            result = word in Dictionary.__words
            if result:
                return Utils.format_notification('answer', 'exists')
            else:
                return Utils.format_notification('answer', 'not_exists')

    __words = list()



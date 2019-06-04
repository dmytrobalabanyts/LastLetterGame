import json

class User(object):
    """description of class"""
    def __init__(self, name):
        self.__name = name

    def notify(self, string):
        notification = json.loads(string)
        if notification['command'] == 'first_turn':
            self.__get_word('Your go first. Start from: ' + notification['data'])
            return self.__answer
        elif notification['command'] == 'your_turn':
            self.__get_word('Your turn. Answer to: ' + notification['data'])
            return self.__answer
        elif notification['command'] == 'repeat_turn':
            self.__get_word(self.__answer 
                              + " hasn't been accepted. Find anoter answer to: "
                              + notification['data'])
            return self.__answer
    
    def __get_word(self, prompt):
            print (self.__name + '. ' + prompt)
            self.__input_answer()
            return self.__answer


    def __input_answer(self):
        self.__answer = input();
        return self.__answer

    __answer = ''
    __name = 'Noname'
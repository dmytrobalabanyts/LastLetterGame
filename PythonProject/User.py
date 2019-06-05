import json
import Utils

class User(object):
    """description of class"""
    def __init__(self, name):
        self.__name = name

    def notify(self, string):
        notification = json.loads(string)
        if notification['command'] == 'first_turn':
            self.__get_word('Your go first')
        elif notification['command'] == 'your_turn':
            self.__get_word('Your turn. Answer to: ' + notification['data'])
        elif notification['command'] == 'repeat_turn':
            self.__get_word(self.__answer 
                              + " hasn't been accepted. Find anoter answer to: "
                              + notification['data'])
        elif notification['command'] == 'wrong_letter':
            self.__get_word(self.__answer 
                              + " begins with not correct letter. Find anoter answer to: "
                              + notification['data'])
        elif notification['command'] == 'already_used':
            self.__get_word(self.__answer 
                              + " already was used. Find anoter answer to: "
                              + notification['data'])
        elif notification['command'] == 'not_exist':
            self.__get_word(self.__answer 
                              + " doesn't exist. Find anoter answer to: "
                              + notification['data'])
        self.__save_state()
        return Utils.format_notification('next_word', self.__answer)
    
    def __get_word(self, prompt):
            print (self.__name + '. ' + prompt)
            self.__input_answer()
            return self.__answer

    def __input_answer(self):
        self.__answer = input();

    def __save_state(self):
        pass

    __answer = ''
    __name = 'Noname'
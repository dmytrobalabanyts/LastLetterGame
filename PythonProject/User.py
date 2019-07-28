import json
import Utils
from BaseClass import BaseClass

class User(BaseClass):
    """This class represents the basic functionality of a player entity.
    The real platyer should be a child class of the User.
    Possible commands:
        command - 'first_turn'
        data - none
        
        command - 'your_turn'
        data - word to answer
        
        command - 'repeat_turn'
        data - word to answer
        
        command - 'wrong_letter'
        data - word to answer
        
        command - 'already_used'
        data - word to answer
        
        command - 'not_exist'
        data - word to answer
        """
    def __init__(self, name, restore = False):
        super().__init__()
        self.__name = name

    def run(self):
        while True:
            address, message, tag = self.receive()

            notification = json.loads(message)
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
            self._save_state()
            self.send(address, Utils.format_notification('next_word', self.__answer))
    
    def __get_word(self, prompt):
            print (self.__name + '. ' + prompt)
            self.__input_answer()
            return self.__answer

    def __input_answer(self):
        self.__answer = ""
        while self.__answer.__len__() == 0:
            self.__answer = input();

    __answer = ''
    __name = 'Noname'


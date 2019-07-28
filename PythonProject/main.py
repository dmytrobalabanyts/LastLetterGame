from Game import *
from State import *
from Dictionary import *
from User import *
from BaseClass import BaseClass, dispatcher

class Factory:
    """This class intended to create a game entities for building the new game"""
    def create_user(self, type):
        user = User(type)
        dispatcher.add_address(user, type)
        return user

    def create_dictionary(self, type, arguments):
        dictionary = Dictionary(arguments)
        dispatcher.add_address(dictionary, type)
        return dictionary

    def create_state_machine(self, type, dictionary):
        state_machine = State(dictionary)
        dispatcher.add_address(state_machine, type)
        return state_machine

    def create_game(self, type, player1, player2, state_machine):
        game = Game(player1, player2, state_machine)
        dispatcher.add_address(game, type)
        return game

factory = Factory()

def init():
    """Constructs the game"""
    player1 = factory.create_user("Human")
    player1.start();
    player2 = factory.create_user("Bot")
    player2.start();
    dictionary = factory.create_dictionary("dictionary", [])
    state_machine = factory.create_state_machine("state_machine", dictionary)
    global game
    game = factory.create_game("Game", player1, player2, state_machine)

def run():
    init()

    dispatcher.start()
    game.start()
    game.join()
    print('Game is over!')
    

run()

from Game import *
from State import *
from Dictionary import *
from User import *
from BaseClass import BaseClass

class Factory:
    """This class intended to create a game entities for building the new game"""
    def create_user(self, type):
        return User(type)

    def create_dictionary(self, type, arguments):
        return Dictionary(arguments)

    def create_state_machine(self, type, dictionary):
        return State(dictionary)

    def create_game(self, type, player1, player2, state_machine):
        return Game(player1, player2, state_machine)

factory = Factory()

def init():
    """Constructs the game"""
    player1 = factory.create_user("Human")
    player2 = factory.create_user("Bot")
    dictionary = factory.create_dictionary("dictionary", [])
    state_machine = factory.create_state_machine("state_machine", dictionary)
    global game
    game = factory.create_game("Game", player1, player2, state_machine)

def run():
    init()

    game.go()
    print('Game is over!')
    

run()

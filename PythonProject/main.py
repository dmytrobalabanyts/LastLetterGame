from Game import *
from State import *
from Dictionary import *
from User import *


class Factory:
    def create_user(self, type):
        return User()

    def create_dictionary(self, type, arguments):
        return Dictionary(arguments)

    def create_state_machine(self, type, dictionary):
        return State(dictionary)

    def create_game(self, type, player1, player2, state_machine):
        return Game(player1, player2, state_machine)

factory = Factory()

def init():
    player1 = factory.create_user("Human")
    player2 = factory.create_user("Bot")
    dictionary = factory.create_dictionary("dictionary", [])
    state_machine = factory.create_state_machine("state_machine", dictionary)
    global game
    game = factory.create_game("Game", player1, player2, state_machine)

def run():
    init()

    game.start()
    

run()
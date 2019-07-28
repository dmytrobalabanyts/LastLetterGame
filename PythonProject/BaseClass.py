from threading import Thread
from queue import Queue, Empty

class BaseClass(Thread):
    def __init__(self):
        super().__init__(daemon = True)
        self.__inp_queue = Queue()
        pass

    def _save_state(self):
        pass

    def _restore_state(self):
        pass

    def send(self, address, message):
        common_queue.put((address, self, message))
        pass

    def receive(self):
        return self.__inp_queue.get()

    __inp_queue = Queue()

class Dispatcher(Thread):
    def __init__(self):
        super().__init__(daemon = True)
        self.__addressees.clear()
        self.__senders.clear()
        tag = 0

    def add_address(self, addressee, name):
        self.__addressees[name] = addressee
        self.__senders[addressee] = name

    def run(self):
        while True:
            address, sender, message = common_queue.get();
            addressee = self.__addressees[address]
            addr_from = self.__senders[sender]
            if  addressee != None and addr_from != None:
                addressee._BaseClass__inp_queue.put((addr_from, message, self.tag))
                self.tag += 1

    __addressees = {}
    __senders = {}
    tag = 0

dispatcher = Dispatcher()
common_queue = Queue()

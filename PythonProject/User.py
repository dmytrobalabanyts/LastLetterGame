class User(object):
    """description of class"""
    def __init__(self):
        pass

    def notify(self, notification):
        print (notification)
        self._input_answer()
        return self._answer

    def _input_answer(self):
        self._answer = input();

    _answer = ''
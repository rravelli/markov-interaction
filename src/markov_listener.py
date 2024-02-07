from gramListener import gramListener
from markov import Markov


class MarkovListener(gramListener):

    def __init__(self):
        self.markov = Markov()

    def enterDefstates(self, ctx):
        pass

    def enterDefactions(self, ctx):
        pass

    def enterTransact(self, ctx):
        pass

    def enterTransnoact(self, ctx):
        pass

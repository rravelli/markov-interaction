from antlr4 import (
    StdinStream,
    CommonTokenStream,
    ParseTreeWalker,
)  # FileStream
from gramLexer import gramLexer
from gramParser import gramParser
from markov_listener import MarkovListener


def main():
    lexer = gramLexer(StdinStream())
    # lexer = gramLexer(FileStream("ex.mdp"))
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    markov_listener = MarkovListener()
    walker = ParseTreeWalker()
    walker.walk(markov_listener, tree)
    print(markov_listener.markov.actions)


if __name__ == "__main__":
    main()

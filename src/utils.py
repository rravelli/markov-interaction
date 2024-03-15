from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream
from gramLexer import gramLexer
from gramParser import gramParser
from markov_listener import MarkovListener


def markov_from_file(path: str):
    lexer = gramLexer(FileStream(path))
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    listener = MarkovListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.markov.check_definitions_not_used()
    return listener.markov

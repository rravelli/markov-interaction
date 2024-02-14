from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream
from gramLexer import gramLexer
from gramParser import gramParser
from markov_listener import MarkovListener


def main():
    lexer = gramLexer(FileStream("examples/ex.mdp"))
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    markov_listener = MarkovListener()
    walker = ParseTreeWalker()
    walker.walk(markov_listener, tree)
    markov = markov_listener.markov
    while True:
        choice = None
        print(f"Current state: {markov.current_state}")
        if markov.is_action_state():
            av = markov.available_actions()
            correct = False
            while not correct:
                choice = input(f"Choose an action, choices are {av}\n")
                if choice in av:
                    correct = True
        else:
            print(
                [
                    (trans.to, trans.weight)
                    for trans in markov.graph[markov.current_state]
                ]
            )
            input("Press enter to continue")
        trans = markov.go_to_next_state(choice)
        print(trans.to, trans.weight)


if __name__ == "__main__":
    main()

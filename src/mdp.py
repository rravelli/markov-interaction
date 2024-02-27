from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream
from gramLexer import gramLexer
from gramParser import gramParser
from markov_listener import MarkovListener
from plotting import markov_to_graph
import networkx as nx
from game import open_window
from pygame import Color
from graphics.colors import *


def main():
    lexer = gramLexer(FileStream("examples/ex.mdp"))
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    markov_listener = MarkovListener()
    walker = ParseTreeWalker()
    walker.walk(markov_listener, tree)
    markov = markov_listener.markov

    g = markov_to_graph(markov)
    pos = nx.planar_layout(g)
    print(pos)
    pos = {key: pos[key] * 1000 for key in pos}
    node_color = {
        name: ACTION_NODE_EDGE if d["action"] else DEFAULT_NODE_EDGE
        for name, d in g.nodes(data=True)
    }
    edge_color = {
        (u, v): DEFAULT_NODE_EDGE if d.get("weight") else ACTION_NODE_EDGE
        for u, v, d in g.edges(data=True)
    }
    node_size = {name: 12 if d["action"] else 20 for name, d in g.nodes(data=True)}

    open_window(
        pos,
        edges=g.edges(data=True),
        edge_color=edge_color,
        node_color=node_color,
        node_size=node_size,
        markov=markov,
    )


def simulate_markov(markov: MarkovListener):
    print("\n\nSimulation starts. Enter . to end simulation\n")
    while True:
        choice = None
        print(f"Current state: {markov.current_state}")

        if markov.is_action_state():
            available = markov.available_actions()
            available_names = [action.name for action in available]
            available = [str(action) for action in available]

            correct = False
            while not correct:
                choice = input(
                    f"Choose an action, choices are the following : \n{''.join(available)}\n"
                )
                if choice in available_names:
                    correct = True
                elif choice == ".":
                    return
        else:
            available = [str(trans) for trans in markov.graph[markov.current_state]]
            print(f"Following transitions are possible : {', '.join(available)}")
            choice = input("Press enter to continue \n")
            if choice == ".":
                return

        trans = markov.go_to_next_state(choice)
        print(f"Transition {trans} chosen. \n")


def main_console():
    lexer = gramLexer(FileStream("examples/ex.mdp"))
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    markov_listener = MarkovListener()
    walker = ParseTreeWalker()
    walker.walk(markov_listener, tree)
    markov = markov_listener.markov
    simulate_markov(markov)


if __name__ == "__main__":
    main()

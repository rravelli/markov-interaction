from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream
from gramLexer import gramLexer
from gramParser import gramParser
from markov_listener import MarkovListener
from plotting import markov_to_graph
import networkx as nx
from game import open_window
from pygame import Color


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
    node_color = {
        name: Color(255, 0, 0) if d["action"] else Color(0, 0, 255)
        for name, d in g.nodes(data=True)
    }
    edge_color = {
        (u, v): "blue" if d.get("weight") else "red"
        for u, v, d in g.edges(data=True)
    }
    node_size = {
        name: 12 if d["action"] else 20 for name, d in g.nodes(data=True)
    }

    open_window(
        pos,
        edges=g.edges(data=True),
        edge_color=edge_color,
        node_color=node_color,
        node_size=node_size,
        markov=markov,
    )


if __name__ == "__main__":
    main()

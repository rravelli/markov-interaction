from markov import Markov
import networkx as nx


def markov_to_graph(m: Markov):
    g = nx.DiGraph()
    states = list(m.graph)

    vertices = []
    for index, state in enumerate(states):
        vertices.append((state, {"action": False}))

    g.add_nodes_from(vertices)

    edges = []
    for index, state in enumerate(states):
        if m.is_action_state(state=state):
            actions = m.graph[state]
            g.add_nodes_from([(a.name, {"action": True}) for a in actions])
            edges += [(state, a.name) for a in actions]
            for a in actions:
                edges += [
                    (a.name, trans.to, {"weight": trans.weight})
                    for trans in a.transitions
                ]
        else:
            edges += [
                (state, trans.to, {"weight": trans.weight})
                for trans in m.graph[state]
            ]
    g.add_edges_from(edges)
    return g

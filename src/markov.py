class Transition:
    def __init__(self, weight: int, to: str) -> None:
        self.weight = weight
        self.to = to


class Action:
    def __init__(self, name: str, transitions: list[Transition]) -> None:
        self.name = name
        self.transitions = transitions


class Markov:
    def __init__(self) -> None:
        self.graph: dict[str, list[Action] | list[Transition]] = {}
        self.actions: list[str] = []

    def define_state(self, names: list[str]):
        for name in names:
            self.graph[name] = []

    def define_action(self, names: list[str]):
        self.actions += names

    def add_transition(self, from_node: str, transition: Transition):
        node_transitions = self.graph.get(from_node)

        if node_transitions is None:
            raise KeyError(f"State {from_node} was not defined")

        if self.graph.get(transition.to) is None:
            raise KeyError(f"State {transition.to} was not defined")

        if len(node_transitions) > 0 and isinstance(
            node_transitions[-1], Action
        ):
            raise TypeError(
                "Can't mix transitions with and without actions on the same node"
            )

        if transition.to in [t.to for t in node_transitions]:
            raise TypeError(
                f"Transition from '{from_node}' to '{transition.to}' has been defined twice"
            )

        self.graph[from_node].append(transition)

    def add_action(self, from_node: str, action: Action):
        node_transitions = self.graph.get(from_node)

        if action.name not in self.actions:
            raise KeyError(f"Actions {action.name} was not defined")

        if node_transitions is None:
            raise KeyError(f"State {from_node} was not defined")

        for transition in action.transitions:
            if self.graph.get(transition.to) is None:
                raise KeyError(f"State {transition.to} was not defined")

        if len(node_transitions) > 0 and isinstance(
            node_transitions[-1], Transition
        ):
            raise TypeError(
                "Can't mix transitions with and without actions on the same node"
            )

        if action.name in [t.name for t in node_transitions]:
            raise TypeError(f"Action '{action.name}' has been defined twice")

        self.graph[from_node].append(action)

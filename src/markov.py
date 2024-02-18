from random import randint


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
        self.current_state = None

    def define_states(self, names: list[str]):
        if self.current_state is None:
            self.current_state = names[0]

        for name in names:
            self.graph[name] = []

    def define_actions(self, names: list[str]):
        self.actions += names

    def add_transition(self, from_node: str, transition: Transition):
        state_transitions = self.graph.get(from_node)

        if state_transitions is None:
            raise KeyError(f"State {from_node} was not defined")

        if self.graph.get(transition.to) is None:
            raise KeyError(f"State {transition.to} was not defined")

        if len(state_transitions) > 0 and isinstance(
            state_transitions[-1], Action
        ):
            raise TypeError(
                "Can't mix transitions with and without actions on the same node"
            )

        if transition.to in [t.to for t in state_transitions]:
            raise TypeError(
                f"Transition from '{from_node}' to '{transition.to}' has been defined twice"
            )

        self.graph[from_node].append(transition)

    def add_action(self, from_node: str, action: Action):
        state_transitions = self.graph.get(from_node)

        if action.name not in self.actions:
            raise KeyError(f"Actions {action.name} was not defined")

        if state_transitions is None:
            raise KeyError(f"State {from_node} was not defined")

        for transition in action.transitions:
            if self.graph.get(transition.to) is None:
                raise KeyError(f"State {transition.to} was not defined")

        if len(state_transitions) > 0 and isinstance(
            state_transitions[-1], Transition
        ):
            raise TypeError(
                "Can't mix transitions with and without actions on the same node"
            )

        if action.name in [t.name for t in state_transitions]:
            raise TypeError(f"Action '{action.name}' has been defined twice")

        self.graph[from_node].append(action)

    def go_to_next_state(self, action_choice: str = None) -> Transition:

        if self.is_action_state():
            if action_choice is None:
                raise ValueError(
                    f"Current state {self.current_state} is an action-state. You must choose an action"
                )
            actions = self.graph.get(self.current_state)
            chosen_action = [x for x in actions if x.name == action_choice]
            if len(chosen_action) <= 0:
                raise ValueError(
                    f"Action {action_choice} is not an available action"
                )
            trans = Markov._choose_transitions(chosen_action[0].transitions)

        else:
            transitions = self.graph.get(self.current_state)
            trans = Markov._choose_transitions(transitions)
        self.current_state = trans.to
        return trans

    def is_action_state(self, state=None) -> bool:
        if state is None:
            state = self.current_state

        state_transitions = self.graph.get(state)

        return (
            state_transitions is not None
            and len(state_transitions)
            and isinstance(state_transitions[-1], Action)
        )

    @classmethod
    def _choose_transitions(
        cls, transitions: list[Transition]
    ) -> Transition | None:
        if len(transitions) == 0:
            return None

        sum_ = sum([t.weight for t in transitions])
        val = randint(0, sum_)
        acc = 0
        for t in transitions:
            acc += t.weight
            if val < acc:
                return t
        return transitions[-1]

    def available_actions(self, state: str = None):
        if state is None:
            state = self.current_state
        if not self.is_action_state(state):
            raise ValueError(f"State {state} is not an action-state.")

        actions = self.graph.get(state)
        action_names = [action.name for action in actions]
        return action_names

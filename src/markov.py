from random import randint
from math import log


class Transition:
    def __init__(self, weight: int, to: str) -> None:
        self.weight = weight
        self.to = to

    def __str__(self) -> str:
        return f"To {self.to} with weight {self.weight}"

    def __repr__(self) -> str:
        return f"To {self.to} with weight {self.weight}"


class Action:
    def __init__(self, name: str, transitions: list[Transition]) -> None:
        self.name = name
        self.transitions = transitions

    def __str__(self) -> str:
        transitions_str = [f" - {trans}\n" for trans in self.transitions]
        return f"{self.name} with transitions:\n{''.join(transitions_str)}"

    def __repr__(self) -> str:
        transitions_str = [f" - {trans}\n" for trans in self.transitions]
        return f"{self.name} with transitions:\n{''.join(transitions_str)}"


class Markov:
    def __init__(self) -> None:
        self.graph: dict[str, list[Action] | list[Transition]] = {}
        self.actions: list[str] = []
        self.current_state = None
        self.history: list[str] = []
        self.reward: dict[str, list[int]] = {}
        self.q: dict[str, float] = {}

    def define_states(self, names: list[str], reward: list[int]):
        if self.current_state is None:
            self.current_state = names[0]

        if len(names) > len(reward) > 0:
            raise KeyError(
                "You must either define rewards for all states or none."
            )

        for i in range(len(names)):
            self.graph[names[i]] = []
            if len(reward) > 0:
                self.reward[names[i]] = reward[i]

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
            raise Warning(f"Actions {action.name} was not defined")

        if state_transitions is None:
            raise Warning(f"State {from_node} was not defined")

        for transition in action.transitions:
            if self.graph.get(transition.to) is None:
                raise Warning(f"State {transition.to} was not defined")

        if len(state_transitions) > 0 and isinstance(
            state_transitions[-1], Transition
        ):
            raise TypeError(
                "Can't mix transitions with and without actions on the same node"
            )

        if action.name in [t.name for t in state_transitions]:
            raise TypeError(f"Action '{action.name}' has been defined twice")

        self.graph[from_node].append(action)

    def check_definitions_not_used(self):
        for node, trans in self.graph.items():
            if len(trans) == 0:
                raise Warning(f"State {node} has no transition or action.")

        for action_name in self.actions:
            missing = True
            for node in self.graph.keys():
                if any(
                    action_name == action.name
                    for action in self.graph[node]
                    if isinstance(action, Action)
                ):
                    missing = False
            if missing:
                raise Warning(f"Action {action_name} was defined but not used.")

    def go_to_next_state(
        self, action_choice: str = None, state: str = None
    ) -> Transition:
        trans = self.simulate_next_state(
            action_choice=action_choice, state=state
        )

        if self.is_action_state():
            self.history.append(action_choice)

        self.history.append(trans.to)

        if trans is not None:
            self.current_state = trans.to

        return trans

    def simulate_next_state(
        self, action_choice: str = None, state: str = None
    ) -> Transition:
        if state is None:
            state = self.current_state

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

    def is_markov_chain(self):
        if len(self.actions) == 0:
            return True
        else:
            return False

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
        return actions

    def choose_random_action(self, state=None):
        if state is None:
            state = self.current_state

        actions = [x.name for x in self.available_actions()]
        r = randint(0, len(actions) - 1)
        return actions[r]

    def monte_carlo(
        self,
        states: list[str],
        epsilon: float = None,
        delta: float = None,
        n: int = None,
    ):
        if n is None:
            n = int((log(2) - log(delta)) / (2 * epsilon) ** 2) + 1
        _sum = 0
        for _ in range(n):
            action = None
            if self.is_action_state():
                action = self.choose_random_action()
            self.go_to_next_state(action_choice=action)
            _sum += self.current_state in states

        return _sum / n

    def q_learning(self, Ttot: int, gamma: float = 0.1):
        states = list(self.graph)
        for t in range(Ttot):
            # choose state
            st = states[randint(0, len(states))]
            # choose action
            at = None
            if self.is_action_state(st):
                at = self.choose_random_action()

            # simulate and get next state
            next_state = self.simulate_next_state(
                action_choice=at, state=st
            ).to

            # update de la fonction Q
            delta_t = (
                self.reward[st]
                + gamma
                * max(
                    [
                        self.q[f"{next_state};{actions.name}"]
                        for actions in self.graph[next_state]
                    ]
                )
                - self.q[f"{st};{at}"]
            )
            self.q[f"{st};{at}"] += 1 / (t + 1) * delta_t

        return self.q

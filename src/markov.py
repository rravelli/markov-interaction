from random import randint, choices
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
            raise KeyError("You must either define rewards for all states or none.")

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

        if len(state_transitions) > 0 and isinstance(state_transitions[-1], Action):
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

        if len(state_transitions) > 0 and isinstance(state_transitions[-1], Transition):
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
        trans = self.simulate_next_state(action_choice=action_choice, state=state)

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

        if self.is_action_state(state):
            if action_choice is None:
                raise ValueError(
                    f"Current state {state} is an action-state. You must choose an action"
                )
            actions = self.graph.get(state)
            chosen_action = [x for x in actions if x.name == action_choice]
            if len(chosen_action) <= 0:
                raise ValueError(f"Action {action_choice} is not an available action")

            trans = Markov._choose_transitions(chosen_action[0].transitions)
        else:
            transitions = self.graph.get(state)
            trans = Markov._choose_transitions(transitions)

        return trans

    def simulate(
        self,
        final_states: list[str],
        start_state: str = None,
        max_iter: int = 10000,
    ):
        if start_state is None:
            start_state = self.current_state

        current_state = start_state
        k = 0
        while k < max_iter:
            if current_state in final_states:
                return current_state

            if (
                len(self.graph[current_state]) == 1
                and self.graph[current_state][0].to == current_state
            ):
                return None

            action_choice = None

            if self.is_action_state(current_state):
                action_choice = self.choose_random_action(current_state)

            current_state = self.simulate_next_state(action_choice, current_state).to
            k += 1

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
    def _choose_transitions(cls, transitions: list[Transition]) -> Transition | None:
        if len(transitions) == 0:
            return None
        weights = [trans.weight for trans in transitions]
        choice = choices(transitions, weights, k=1)

        return choice[0]

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
        if not self.is_markov_chain():
            return TypeError("SMC in only possible on Markov Chains")

        if n is None:
            n = int((log(2) - log(delta)) / (2 * epsilon) ** 2) + 1
        _sum = 0
        for _ in range(n):
            start_state = list(self.graph.keys())[0]
            final_state = self.simulate(
                final_states=states,
                start_state=start_state,
            )
            _sum += final_state in states

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
            next_state = self.simulate_next_state(action_choice=at, state=st).to

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

    def sprt(
        self,
        final_states: list[str],
        theta: float,
        alpha: float = 0.01,
        beta: float = 0.01,
        epsilon: float = 0.01,
        max_iter=100,
    ):
        if not self.is_markov_chain():
            raise TypeError("Can't apply this algorithm with MDP")

        gamma1 = theta - epsilon
        gamma0 = theta + epsilon
        A = (1 - beta) / alpha
        B = beta / (1 - alpha)

        done = False
        m = 0
        Rm = 1

        while not done:
            val = self.simulate(max_iter=max_iter, final_states=final_states)
            m += 1
            if val in final_states:
                Rm *= gamma1 / gamma0
            else:
                Rm *= (1 - gamma1) / (1 - gamma0)
            if Rm >= A:
                print(f"gamma<{gamma1}")
                print(m)
                return gamma1
            if Rm <= B:
                print(f"gamma>={gamma0}")
                print(m)
                return gamma0

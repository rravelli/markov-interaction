from gramListener import gramListener
from markov import Markov, Transition, Action


class MarkovListener(gramListener):

    def __init__(self):
        self.markov = Markov()

    def enterDefstates(self, ctx):
        states = [str(x) for x in ctx.ID()]
        rewards = [int(str(x)) for x in ctx.INT()]
        self.markov.define_states(states, rewards)

    def enterDefactions(self, ctx):
        actions = [str(x) for x in ctx.ID()]
        self.markov.define_actions(actions)

    def enterTransact(self, ctx):
        to_states = [str(x) for x in ctx.ID()]
        from_state = to_states.pop(0)
        action_name = to_states.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]

        transitions = []
        for i in range(len(to_states)):
            new_transition = Transition(weights[i], to_states[i])
            transitions.append(new_transition)
        new_action = Action(action_name, transitions)
        self.markov.add_action(from_state, new_action)

    def enterTransnoact(self, ctx):
        to_states = [str(x) for x in ctx.ID()]
        from_state = to_states.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]

        for i in range(len(to_states)):
            new_transition = Transition(weights[i], to_states[i])
            self.markov.add_transition(from_state, new_transition)

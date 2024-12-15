class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def remove_unreachable_states(self):
        reachable_states = set()
        queue = [self.start_state]

        while queue:
            current_state = queue.pop(0)
            if current_state not in reachable_states:
                reachable_states.add(current_state)
                for symbol in self.alphabet:
                    next_state = self.transitions.get((current_state, symbol))
                    if next_state and next_state not in reachable_states:
                        queue.append(next_state)

        self.states = list(reachable_states)
        self.transitions = {
            (state, symbol): target
            for (state, symbol), target in self.transitions.items()
            if state in reachable_states and target in reachable_states
        }
        self.accept_states = [state for state in self.accept_states if state in reachable_states]

    def merge_equivalent_states(self):
        groups = [set(self.accept_states), set(self.states) - set(self.accept_states)]

        while True:
            new_groups = []
            for group in groups:
                partition = {}
                for state in group:
                    key = tuple(
                        next(
                            (i for i, g in enumerate(groups) if self.transitions.get((state, symbol)) in g),
                            None,
                        )
                        for symbol in self.alphabet
                    )
                    if key not in partition:
                        partition[key] = set()
                    partition[key].add(state)
                new_groups.extend(partition.values())
            if new_groups == groups:
                break
            groups = new_groups

        mapping = {state: min(group) for group in groups for state in group}
        self.states = [min(group) for group in groups]
        self.transitions = {
            (mapping[state], symbol): mapping[target]
            for (state, symbol), target in self.transitions.items()
        }
        self.accept_states = list({mapping[state] for state in self.accept_states})
        self.start_state = mapping[self.start_state]

    def minimize(self):
        self.remove_unreachable_states()
        self.merge_equivalent_states()


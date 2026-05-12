def get_next_state(pattern, m, state, char):
    if state < m and char == pattern[state]:
        return state + 1

    for next_s in range(state, 0, -1):
        if pattern[next_s - 1] == char:
            if pattern[:next_s - 1] == pattern[state - next_s + 1:state]:
                return next_s
    
    return 0

def compute_transition_table(pattern):

    m = len(pattern)
    alphabet = set(pattern)  
    table = []

    for state in range(m + 1):
        state_transitions = {char: get_next_state(pattern, m, state, char) for char in alphabet}
        table.append(state_transitions)
    
    return table

def search_finite_automata(haystack, needle):
    n = len(haystack)
    m = len(needle)
    
    if m == 0:
        return []

    transition_table = compute_transition_table(needle)
    
    results = []
    state = 0
    
    for i in range(n):
        char = haystack[i]
        state = transition_table[state].get(char, 0)
        
        if state == m:
            results.append(i - m + 1)
            
    return results

haystack_text = "АБРАКАДАБРА"
needle_text = "АБРА"
indices = search_finite_automata(haystack_text, needle_text)

print(f"Текст: {haystack_text}")
print(f"Шукаємо: {needle_text}")
print(f"Індекси входжень: {indices}")
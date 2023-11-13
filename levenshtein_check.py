def check_input(user_input, options):
    closest_match = None
    min_distance = float('inf')
    for option in options:
        distance = levenshtein_distance(user_input, option)
        if distance < min_distance:
            min_distance = distance
            closest_match = option
    return closest_match

def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

# options = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# user_input = input('Enter a fruit: ')
# closest_match = check_input(user_input, options)
# print(f'You entered {user_input}. Did you mean {closest_match}?')

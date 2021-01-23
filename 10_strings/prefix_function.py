def compare_substrings(string, a_begin, b_begin, length):
    for i in reange(length):
        if string[a_begin + i] != string[b_begin + i]:
            return False
    return True


def prefix_function_naive(string):
    pi = [0] * len(string)
    for i in range(string):
        for prefix_len in range(0, i - 1):
            if compare_substrings(string, 0, i - prefix_len + 1, prefix_len):
                pi.append()


def prefix_function_zero_based(string):
    """
    pi[i] is prefix function on string string[:i+1]
    string[:pi[i]] == [i-pi[i]+1:i+1]
    """
    # pi[i] is prefix function on string[:i + 1]
    if not string:
        return []

    # We already know the answer for the first value
    pi = [0]
    for i in range(1, len(string)):
        # j is a prefix length to extend
        j = pi[i - 1]
        while j and string[i] != string[j]:
            j = pi[j - 1]

        # if extending prefix if it can be extended 
        if string[i] == string[j]:
            j += 1

        pi.append(j)

    return pi


def prefix_function_one_based(string):
    """
    pi[i] is prefix function on string string[:i]
    string[:pi[i]] == [i - pi[i]:i]
    """

    # pi[:0] is an empty string which cannot have a
    # prefix function value by definition ('' == '')
    pi = [-1]

    # Calculating prefix function for every symbol in
    # a string
    for i, symbol in enumerate(string):
        # A big piece of magic that is quite hard to describe
        # `j` is:
        # * before cycle: an index of new symbol
        # * inside cycle: prefix we attempt to extend
        # * outside cycle: prefix length cirresponding to string[:i].
        j = i
        while j:
            j = pi[j]
            if symbol == string[j]:
                j += 1
                break

        pi.append(j)

    return pi


for string_length in 
    str
string = 'abacabadabacabc'
zero_based = prefix_function_zero_based(string)
one_based = prefix_function_one_based(string)

print(string)
print(zero_based)
print(one_based[1:])

assert(zero_based == one_based[1:])

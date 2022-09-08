def binary_to_term(binary):
    term = ""
    for i in range(len(binary)):
        if binary[i] is None:
            continue

        if binary[i]:
            term += chr(97 + i)
        else:
            term += chr(97 + i) + "'"
    return term


alphabets = {}


def construct_alphabet_dict(number_of_letters=26):
    for i in range(number_of_letters):
        alphabets[chr(97 + i)] = i


def term_to_binary(term, length):
    binary_term = [None for _ in range(length)]
    i = 0
    while i < len(term):
        if i == len(term) - 1:
            binary_term[alphabets[term[i]]] = True
            return binary_term
        if term[i + 1] == "'":
            binary_term[alphabets[term[i]]] = False
            i += 1
        else:
            binary_term[alphabets[term[i]]] = True
        i += 1
    return binary_term


def term_len(term):
    length = 0
    for i in term:
        if i != "'":
            length += 1
    return length


def reduce_1_literal(binary_func_TRUE, binary_func_DC=[]):
    expanded_binary = []
    for i in range(len(binary_func_TRUE)):
        binary1 = binary_func_TRUE[i].copy()
        for j in range(len(binary1)):
            if binary1[j] is not None:
                binary1[j] = not binary1[j]
                if binary1 in binary_func_TRUE + binary_func_DC:
                    binary2 = binary1.copy()
                    binary2[j] = None
                    if binary2 not in expanded_binary:  # not efficient
                        expanded_binary.append(binary2)
                binary1[j] = not binary1[j]
    return expanded_binary


def expand(binary_func_TRUE, binary_func_DC=[]):
    output = reduce_1_literal(binary_func_TRUE, binary_func_DC)
    new_terms = output
    while len(new_terms) != 0:
        new_terms = reduce_1_literal(new_terms)
        output = new_terms + output
    return output


def combine(expanded_terms, func_TRUE):
    # print(func_TRUE, expanded_terms)
    combined = []
    for term in func_TRUE:
        expanded = False
        for expanded_term in expanded_terms:
            # print(term, expanded_term, expanded_term in term)
            if expanded_term in term:
                combined.append(expanded_term)
                # print("appended", expanded_term)
                expanded = True
                break
        if not expanded:
            combined.append(term)
    return combined


def contained(expanded_binary, binary_term):
    for i in range(len(expanded_binary)):
        if expanded_binary[i] is not None:
            if expanded_binary[i] != binary_term[i]:
                return False
    return True


def binary_combine(expanded_terms, func_TRUE):
    # print(func_TRUE, expanded_terms)
    combined = []
    for term in func_TRUE:
        expanded = False
        for expanded_term in expanded_terms:
            # print(term, expanded_term, expanded_term in term)
            if contained(expanded_term, term):
                combined.append(expanded_term)
                # print("appended", expanded_term)
                expanded = True
                break
        if not expanded:
            combined.append(term)
    return combined


def comb_function_expansion(func_TRUE, func_DC):
    """
        determines the maximum legal region for each term in the K-map function
        Arguments:
            func_TRUE: list containing the terms for which the output is '1'
            func_DC: list containing the terms for which the output is 'x'
        Return: a list of terms: expanded terms in form of boolean literals
    """

    term_max_len = 0
    for term in func_TRUE + func_DC:
        size = term_len(term)
        if term_max_len < size:
            term_max_len = size

    construct_alphabet_dict(term_max_len)  # extend this later to handle terms like xyz as well

    binary_func_TRUE = [term_to_binary(term, term_max_len) for term in func_TRUE]
    binary_func_DC = [term_to_binary(term, term_max_len) for term in func_DC]

    expanded_binary = expand(binary_func_TRUE, binary_func_DC)
    expanded_terms = [binary_to_term(binary) for binary in expanded_binary]
    combined_terms = combine(expanded_terms, func_TRUE)
    binary_combined = binary_combine(expanded_binary, binary_func_TRUE)

    return [binary_to_term(term) for term in binary_combined]


print(comb_function_expansion(["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"],
                              ["abc'd"]))
print(comb_function_expansion(["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'",
                               "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"],
                              ["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]))

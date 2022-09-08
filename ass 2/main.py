def expandBinaryFunc(func_binary):
    answer = []
    for term in func_binary:
        temp = term.copy()
        for i in range(len(temp)):
            if temp[i] is None:
                continue
            temp[i] = not temp[i]
            if temp in func_binary:
                temp2 = temp.copy()
                temp2[i] = None
                if temp2 not in answer:
                    answer.append(temp2)
            temp[i] = not temp[i]
    return answer


def getTermFromBinaryList(binaryList):
    termList = []
    for binary_term in binaryList:
        term = ""
        for i in range(len(binary_term)):
            if binary_term[i] is None:
                continue

            if binary_term[i]:
                term += chr(97 + i)
            else:
                term += chr(97 + i) + "'"
        termList.append(term)
    return termList


alphabets = {}


def binaryTerm(term, length):
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


def combine(func):
    max_len = 0
    for i in func:
        if len(i) > max_len:
            max_len = len(i)

    func_binary = []
    for term in func:
        func_binary.append(binaryTerm(term, max_len))

    answer = expandBinaryFunc(func_binary)
    sub_answer = expandBinaryFunc(answer)
    answer += sub_answer
    while True:
        sub_answer = expandBinaryFunc(sub_answer)
        answer += sub_answer
        if len(sub_answer) in {0, 1}:
            break

    return getTermFromBinaryList(answer)


def reduce(func, true):
    # func_copy = func.copy()
    # true_copy = true.copy()
    # for i in range(len(func_copy)):
    #     adds_value = False
    #     if func_copy[i] is None:
    #         continue
    #     for j in range(len(true_copy)):
    #         if true_copy[j] is None:
    #             continue
    #         if func_copy[i] is None:
    #             continue
    #
    #         if func_copy[i] in true_copy[j]:
    #             adds_value = True
    #             true_copy[j] = None
    #
    #     if not adds_value:
    #         func_copy[i] = None
    # return [term for term in (func_copy + true_copy) if term is not None]
    print(func, true)
    expanded_terms = {}
    for term1 in func:
        for term2 in true:
            if term1 in term2:
                if term2 not in expanded_terms.keys():
                    expanded_terms[term2] = term1
    return expanded_terms


def comb_function_expansion(func_TRUE, func_DC):
    """
        determines the maximum legal region for each term in the K-map function
        Arguments:
            func_TRUE: list containing the terms for which the output is '1'
            func_DC: list containing the terms for which the output is 'x'
        Return:
            a list of terms: expanded terms in form of boolean literals
    """
    func = func_TRUE + func_DC

    for i in range(26):
        alphabets[chr(97 + i)] = i

    rev = combine(func).copy()
    rev.reverse()
    return reduce(rev, func_TRUE)


print(comb_function_expansion(["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"],
                              ["abc'd"]))
print(comb_function_expansion(["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'",
                               "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"],
                              ["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]))

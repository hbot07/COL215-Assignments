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


def newExpand(func_binary):
    answer = {}
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
                    answer[temp2] = [temp]
                else:
                    if temp2 not in answer[temp2]:
                        answer[temp2].append(temp)
            temp[i] = not temp[i]
    return answer


def binaryToTerm(binary_term):
    term = ""
    for i in range(len(binary_term)):
        if binary_term[i] is None:
            continue

        if binary_term[i]:
            term += chr(97 + i)
        else:
            term += chr(97 + i) + "'"
    return term


def getTermFromBinaryList(binaryList):
    termList = []
    for binary_term in binaryList:
        termList.append(binaryToTerm(binary_term))
    return termList


def getTermFromBinaryDict(binaryDict):
    termDict = {}
    for i in binaryDict.keys():
        termDict[binaryToTerm(i)] = [binaryToTerm(j) for j in binaryDict[i]]
    return termDict


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

    return getTermFromBinaryDict(answer)


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

    # constructing the alphabets dictionary mapping a,b,c... to 1,2,3...
    for i in range(26):
        alphabets[chr(97 + i)] = i

    rev = combine(func)
    return rev


print(comb_function_expansion(["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"],
                              ["abc'd"]))
print(comb_function_expansion(["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'",
                               "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"],
                              ["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]))

def solution(s):
    answer = True
    s = list(s)
    stack = []

    while s :
        bracket = s.pop()
        if not stack :
            if bracket == "(":
                return False
            stack.append(bracket)
            continue

        bracket_con = stack[-1]
        if bracket != bracket_con :
            stack.pop()
        else :
            stack.append(bracket_con)

    if not stack:
        return True
    else :
        return False

# 다른 사람 풀이
def is_pair(s):
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
        """ if x == "(":
            pair=pair+1
        if x == ")" :
            pair-1
        else :
            pair """
    return pair == 0

print(is_pair(")()()("))
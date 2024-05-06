# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations, combinations

# 소수에 대한 함수 필요 (완전 탐색? 으로 짠다면..)
def find_prime_number(num):
    if num < 2 :
        return False
    for i in range(2,num//2+1):
        if num % i == 0 :
            return False
    return True

#123
# 123, 132, 213, 231 ,312 ,321
# 부분 집합 함수 (combinations 사용)
# 순열 함수 (permutations 사용)
def make_perm_numbers(numbers):
    perm_numbers = []
    for i in range(1,len(numbers)+1):
        split_numbers = combinations(numbers,i)
        # split_permutations = list(permutations(split_numbers))
        for split_number in split_numbers :
            perm_numbers.extend(map(int, map(''.join, permutations(split_number))))
    perm_numbers = list(set(perm_numbers))
    return perm_numbers

numbers = "17"
answer = 0
perm_numbers = make_perm_numbers(numbers)
for num in perm_numbers:
    if find_prime_number(num):
        answer+=1
print(answer)


"""
프로그래머스 답

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

    """


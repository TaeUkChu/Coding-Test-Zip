'''
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다.

예제 입력 1
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

예제 출력 1
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate

Sol) 접근 방식
1. 길이를 반환, 비교
2. 사전순 배열
3. 중복 제거
'''
import sys
N = int(input())
words=[]
for _ in range(N):
    word = sys.stdin.readline().strip()
    words.append(word)
def len_sort_rule(value):
    return len(value)
#중복 제거 -> set으로 바꾸기
words = list(set(words))
#사전순 정렬
words.sort()

#길이순 정렬
words.sort(key=len_sort_rule)

for word in words :
    print(word)
'''
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

1,2,3,4,5,6,7
4,5,6,7,1,2, <3>
7,1,2,4,5, <3,6>
4,5,7,1 <3,6,2>
1,4,5 <3,6,2,7>
1,4 <3,6,2,7,5>
완료 <3,6,2,7,5,1,4>

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

예제 입력 1
7 3
예제 출력 1
<3, 6, 2, 7, 5, 1, 4>

3,5,6,8,9,10 / 7

5,6,8,9,10 <3>
8,9,10,5 <3,6>
5,8,9, <3,6,10>
8,9, <3,6,10,5,>
9, <3,6,10,5,8,>


'''
from collections import deque

n,k = map(int, input().split())
deq = deque()
answer = []
for i in range(1,n+1):
    deq.append(i)
while len(deq) > k :
    for i in range(k-1) :
        deq.append(deq.popleft())
    answer.append(deq.popleft())
while len(deq) > 0 :
    temp = k%len(deq)
    if temp == 0:
        temp = len(deq)
    for i in range(temp-1) :
        deq.append(deq.popleft())
    answer.append(deq.popleft())


def print_answer(answer):
    print("<",end="")
    for i in range(len(answer)):
        if i == len(answer)-1:
            print(answer[i], end="")
        else:
            print(f"{answer[i]}, ", end="")
    print(">")

def print_answer2(answer):
    answer = str(answer).strip("[""]")
    print(f"< {answer} >")
print_answer2(answer)

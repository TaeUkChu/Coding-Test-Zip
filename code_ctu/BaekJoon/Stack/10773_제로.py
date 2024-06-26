'''
문제
재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!

입력
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며,
정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

출력
재민이가 최종적으로 적어 낸 수의 합을 출력한다.
최종적으로 적어낸 수의 합은 231-1보다 작거나 같은 정수이다.

예제 입력 2
10
1
3
5
4
0
0
7
0
0
6

예제 2의 경우를 시뮬레이션 해보면,

[1]
[1,3]
[1,3,5]
[1,3,5,4]
[1,3,5] (0을 불렀기 때문에 최근의 수를 지운다)
[1,3] (0을 불렀기 때문에 그 다음 최근의 수를 지운다)
[1,3,7]
[1,3] (0을 불렀기 때문에 최근의 수를 지운다)
[1] (0을 불렀기 때문에 그 다음 최근의 수를 지운다)
[1,6]
합은 7이다.
'''

k = int(input())
stack = []
answer = 0
for i in range(k):
    num = int(input())
    stack.append(num)
    if num == 0:
        stack.pop()
        stack.pop()
for n in stack :
    answer += n
print(answer)




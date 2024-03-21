'''
링크 : https://codeup.kr/problem.php?id=1402
두 수를 거꾸로 출력하기..

세 수를 거꾸로 출력하기...

이런 문제들은 쉽게 풀 수 있었다.

이번에는 데이터의 개수가 n개가 들어오고, n개의 데이터를 거꾸로 출력하는 프로그램을 작성하시오.

입력 예시 :
5
1 3 5 6 8

출력 예시 :
8 6 5 3 1
'''

n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
for i in range(n):
    print(data[i],end=" ")
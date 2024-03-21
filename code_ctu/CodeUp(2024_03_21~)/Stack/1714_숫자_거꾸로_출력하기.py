'''
어떤 수 N이 입력되면 그 수를 거꾸로 출력하는 프로그램을 작성하시오.

예)

입력 : 2571
출력 : 1752


입력 : 1200
출력 : 0021
'''

num = list(input())
for i in range(len(num)-1,-1,-1):
    print(num[i], end="")
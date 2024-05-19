# from collections import deque
# deq = deque(enumerate([-1,1,-1,1,-1],start=1))
# deq = deque(enumerate([3,2,1,-3,-1],start=1))

#  # 3,2,1,-3,-1
# deq.popleft()[0]
# deq.rotate(2) #-3 가정
# print(deq.popleft()[0], deq) #4
# deq.rotate(0)# -1 가정
# print(deq.popleft()[0], deq) #5
# deq.rotate(0) # 1 가정
# print(deq.popleft()[0], deq) #3
# deq.rotate(-1)# 2 가정
# print(deq.popleft()[0], deq) #2

# rule(deq,3)

# input_list = deque(enumerate(map(int,"-1 1 -1 1 -1".split(" "))))
# print(input_list)

# array = [1,2,3,4]
# target= 3

# start=0
# mid=0
# end=len(array)-1

# while start <= end :
#     mid = (start+end) // 2
#     if array[mid] == target:
#         break
#     elif array[mid] > target :
#         end = mid-1
#     else :
#         start = mid+1
# print(mid)

# import sys
# N = int(sys.stdin.readline())
# numbers=[]
# for _ in range(N):
#     numbers.append(int(sys.stdin.readline().strip()))
# numbers.sort()
# for number in numbers:
#     print(number)

# array =[1,2,3]

"""
for i in range(len(array)-1,-1,-1):
    print(i)
    print(array[i]) """

# for i in range(1,10):
#     print("i는",i)
#     if i == 3 :
#         break
#     for j in range(1,10):
#         print("j는",j)
#         if j == 4 :
#             break

# n = 10
# a = [False, False] + [True]*(n-1)
# primes=[]

# for i in range(2, n+1):
#     if a[i]:
#         primes.append(i)
#         for j in range(2*i, n+1, i):
#             a[j] = False

# print (a)

# index_li = [x for x in range(len)]
# print(index_li)

# a = []
# print(a[-1])

# A = [1,2,3]
# B = [4,5,6]

# print([x+y for x,y in zip(A,B)])

""" pair = 0
x = "*"
pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
print(pair) """

# arr = [1, 5, 2, 6, 3, 7, 4]
# print(arr[1:3])

arr = ["3","34","30"]
arr2 = list(map(lambda x:x*3,arr))
arr2.sort()
print(arr2)
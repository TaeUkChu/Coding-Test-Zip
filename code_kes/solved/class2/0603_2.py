# 정리 : https://velog.io/@uiseoo/백준-벌집브론즈2-2292번

# n = int(input())
# adress = 0

# def create_array(s, n):
#     return list(range(s, n + 1))

# v_list1 = create_array(1, 7)
# v_list2 = create_array(8, 19)
# v_list3 = create_array(20, 37)
# v_list4 = create_array(38, 61)
# v_list5 = create_array(62, 70)

# graph = [v_list1,v_list2, v_list3, v_list4,v_list5]
# visited = [False]*len(graph)
# print(graph, visited)

# print(len([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
# print(len([20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]))
# print(len([38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]))
# print(len([62, 63, 64, 65, 66, 67, 68, 69, 70]))

# print(1+6+12+18+24)

n = int(input())

nums, cnt = 1, 1
while n > nums:
    nums += 6 * cnt
    cnt += 1

print(cnt)
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# 원소의 길이가 1,10,100,1000일 때의 구분이 필요
# 문자열로 return

# 1번 해결법 : dictioary 를 이용해서 첫 번째 자리 수 마다 정렬 한 뒤 합치자
# 2번 해결법 : 첫 자리부터 순차적으로 내려가면서 정렬
# 3번 해결법 : 각 숫자를 3번 곱한 후 비교 

numbers = [3,30,34,5,9]
str_numbers = list(map(lambda num: str(num), numbers))

sorted_numbers = sorted(str_numbers, key=lambda x: x*3, reverse=True)
largest_number = ''.join(sorted_numbers)

print(largest_number)
# str_numbers = [str(x) for x in numbers]

# number_tag = {key: [] for key in range(10)}

# for str_number in str_numbers:
#     number_tag[int(str_number[0])].append(str_number)


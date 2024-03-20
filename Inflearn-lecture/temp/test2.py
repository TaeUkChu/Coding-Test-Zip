# a = int(input())
# b = int(input())
num_list = sorted(list(map(int,input().split())))
num_dict = {}
for i in range(len(num_list)):
    num_dict[num_list[i]] = num_list.count(num_list[i])
max_num = max(num_dict, key = num_dict.get)
cnt = num_dict[max_num]
print()
# \    /\
#  )  ( ')
# (  /  )
#  \(__)|

# print('''
# \\    /\\
#  )  ( ')
# (  /  )
#  \\(__)|''')

# print('''|\\_/|
# |q p|   /}
# ( 0 )\"\"\"\\
# |"^"`    |
# ||_/=\\\\__|''')
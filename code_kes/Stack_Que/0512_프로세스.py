priorities = [1,9,9]
location = 0

first = max(priorities)
process_list =[]
complete_list = []

for idx, item in enumerate(priorities):
    process_list.append((idx,item))

for i in range(len(process_list)+1):
    if first > process_list[0][1]:
        back = process_list.pop(0) 
        process_list.append(back)
    
    elif first == process_list[0][1]: # 실행된 요소를 제외하고 process_list의 범위를 갱신해서 first 갱신
        complete = process_list.pop(0)
        complete_list.append(complete)
        if len(process_list) != 0:
            first = max(item[1] for item in process_list)# 줄어든 범위에서 연산이 시작되기 떄문에 시간복잡도 증가하지는 않을 것 같음, first 갱신되긴 함

index_0_values = [item[0] for item in complete_list]
answer = index_0_values.index(location)+1
print(answer)
        
        # 접근
        # 정렬이 필요한가? 우선 순위가 높은 것을 확인하기 위해
        # priorities는 값이 같은 요소가 있을 수 있다. 즉 요소의 값(우선순위 정도)으로는 기준으로 정렬할 수 없다.
        # 그렇기때문에 우선 순위가 높은 것을 확인하기 위해 정렬 시 문제의 정렬 조건에 따라야하고 
        # 같은 값의 요소가 여러 개이기 때문에 각 요소를 식별하기 위해 요소의 위치 인덱스를 사용해야한다.
        # 식별하기 위해 요소의 위치 인덱스를 요소로하는 idx 리스트를 생성한다.
        # priorities의 각 요소를 문제에서 제시한 조건에 맞춰 비교를하면
        # 실제 문제의 조건에 맞춰 정렬이 이루어지는 것은 idx 리스트이고 
        # loaction에서 요구하는 값을 idx 리스트의 위치인덱스를 통해 순서를 정의 확인하고 반환한다. 
        
        # 방법
        # priorities max()를 통해 우선순위가 가장 높은 값을 확인한다.
        # 큐(선입선출)라는 환경의 조건에 따라 pop(0)을 이용해 확인한 요소보다 
        # 대기중인 큐의 요소 중에 높은 우선순위가 있으면 다시 append()를 통해 큐에 삽압한다.
        # 아니면 확인한 요소가 가장 높은 우선순위이면 그대로 종료하고
        # 현재 대기중인 큐의 배열 순서를 확인해서 location위치의 요소가 몇번째 순서로 실행되는지 확인한다.
        
        # 조건
        # 가장 높은 우선순위가 여러개일 경우 여러 것일 경우
        # 대기중인 큐에서 요소를 확인하면서 처음으로 max()의 요소가 같은 경우에 answer == 0인 경우(이전 까지는 가장 높은 우선순위가 없었다는 것을 의미)에는
        # 처음으로 확인한 요소가 max()와 같은 시점의 대기증인 큐 배열 순서를 기준으로
        # 각 요소의 위치 인덱스 값들로 생성한 리스트에서 location과 같은 요소의 위치 인덱스를 반환한 후 +1 하여 answer에 갱신한다.
        
        # 프로세스가 실행 되었을 때 location의 프로세스의 실행 순서
        # 우선순위가 더 높은 프로세스가 없다면

# priorities = 	[1,1,9,9,1]
# location = 3

# idx = list(range(len(priorities)))
# first = max(priorities)
# answer = 0

# for i in range(len(priorities)):
#     if first > priorities[i]: 
#         process = idx.pop(0) 
#         idx.append(process)
        
#     elif first == priorities[i]:
#         if answer == 0:
#             answer = idx.index(location)+1
        
#         elif answer !=0:
#             pass
# 노드 표현
class Node:
  def __init__(self, value = 0, next = None) :
    self.value = value
    self.next = next

# 노드 활용 예시
first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
first.value=6
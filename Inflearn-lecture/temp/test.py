# 노드 표현
class Node:
  def __init__(self, value = 0, next = None) :
    self.value = value
    self.next = next

# 노드 활용 예시
def node_play():
  first = Node(1)
  second = Node(2)
  third = Node(3)
  first.next = second
  second.next = third
  first.value=6

# node_play()

class Node(object):
  def __init__(self, value = 0, next = None) :
    self.value = value
    self.next = next

class LinkedList(object):
    def __init__(self) :
      self.head = None

    def append(self, value) :
      node = Node(value)
      if self.head == None :
        self.head = node
      else :
        current = self.head
        while (current.next) :
          current = current.next
        current.next = node

    def get(self,idx) :
      current = self.head
      for _ in range(idx) :
        current = current.next
      return current.value

    def insert_at(self,idx,value) :
      current = self.head
      new_node = Node(value)
      if idx == 0 :
        new_node.next = self.head
        self.head = new_node
      for _ in range(idx-1) :
        current = current.next
      new_node.next = current.next
      current.next = new_node

    def remove_at(self,idx) :
      current = self.head
      for _ in range(idx-1) :
        current = current.next
      current.next = current.next.next

ll = LinkedList()
ll.append(0)
ll.append(1)
ll.append(2)

print(ll.get(1))

ll.insert_at(1,5)

print(ll.get(0))
print(ll.get(1))

ll.insert_at(0,-1)

print(ll.get(0))

print(ll.get(1))
print(ll.get(2))
ll.remove_at(1)
print(ll.get(1))
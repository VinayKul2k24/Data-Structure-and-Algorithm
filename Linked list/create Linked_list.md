```python
#create a node
#crate a node
class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

```


```python
#create a linked list
class linkedlist:
  def __init__(self):
    self.head = None
  #add node
  def add_node(self,value):
    new_node = Node(value)

    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = new_node

    
```


```python
### create a Linked list
l1 = linkedlist()
l1.add_node(value = 10)
l1.add_node(value = 15)
l1.add_node(value = 20)

```


```python
l1.head.next
print(l1.head.next.value)
```

    15



```python
def print_linkedlist(head):
  while head is not None:
    print(head.value)
    head = head.next
print_linkedlist(l1.head)
```

    10
    15
    20



```python
# for recurive
def print_r(head):
  if head is None:
    return 
  print(head.value)
  print_r(head.next)
print_r(l1.head)

```

    10
    15
    20



```python
# find the lenght
l3 = linkedlist()
for i in range(10):
  l3.add_node(i*2)
```


```python
def find_lenght(head):
  
  len = 0
  while head is not None:
    len+=1
    head = head.next
  
  return len
```


```python
find_lenght(l3.head)
```




    10




```python
#recursively
def find_len(head):
  if head is None:
    return 0
  return 1 + find_len(head.next)
```


```python
find_len(l3.head)
```




    10




```python

```

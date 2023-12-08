# Removing Duplicates from sorted Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```







![image-20231208094039188](/home/saranath/.var/app/io.typora.Typora/config/Typora/typora-user-images/image-20231208094039188.png)

Consider an implementation of a linked list, where each node is created using the given class Node. Suppose it has a head variable that contains the reference to the first node of the linked list.

You are given a non-empty linked list with n nodes, where these nodes are sorted in ascending order of their value. Your task is to remove nodes with duplicate values from the given list.
Write a function remove Duplicate(head), where head is a reference to the first node of the sorted linked list, that removes nodes with duplicate values from the given linked list. The function should not return any value.



## Sample input

```
1 1 2 2 2 3 3 4 4 4 4 5 7 9 #Input linked list elements
```

## Output
``` 
Output Linked List: 1 2 3 4 5 7 9 #Linked list elements after removing duplicates
```


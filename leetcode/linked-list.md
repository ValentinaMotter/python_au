+ [Reverse Linked List](#)
+ [Middle of the Linked List](#)
+ [Palindrome Linked List](#)
+ [Merge Two Sorted Lists](#)
+ [Remove Nth Node From End of List](#)
+ [Linked List Cycle II](#)
+ [Linked List Cycle](#)
+ [Reorder List](#)
+ [Intersection of Two Linked Lists](#)
+ [Sort List](#)
<!-----solution----->

## Sort List



```python

def sortList(self, head: ListNode) -> ListNode:
    node = head
    sorted_nods = []
    while node:
        sorted_nods.append(node.val)
        node = node.next
    sorted_nods.sort()
    i = 0
    node = head
    while node:
        node.val = sorted_nods[i]
        node = node.next
        i += 1
    return head
```

## Intersection of Two Linked Lists



```python

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None
    a,b=headA,headB
    while (a!=b):
        a=headB if a==None else a.next
        b=headA if b==None else b.next
    return a
```

## Reorder List



```python

def reorderList(self, head: ListNode) -> None:
    if not head:
        return
    slow = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    if slow == fast:
        return
    h2 = slow.next
    slow.next = None
    prev = None
    while h2:
        nxt = h2.next
        h2.next = prev
        prev = h2
        h2 = nxt
    h1, h2 = head, prev
    prev = None
    while h1 and h2:
        if prev:
            prev.next = h1
        h1nxt = h1.next
        h1.next = h2
        prev = h2
        h1, h2 = h1nxt, h2.next
    if h1:
        prev.next = h1
    if h2:
        prev.next = h2
```

## Linked List Cycle



```python

def hasCycle(self, head: ListNode) -> bool:
    slow = fast = head
    isLoopExist = False
    if head.next == None:
        isLoopExist = False
    else:
        while slow and fast:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                isLoopExist = True
                break
    return isLoopExist
```

## Linked List Cycle II



```python

def detectCycle(self, head: ListNode) -> ListNode:
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:
        return None
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
```

## Remove Nth Node From End of List



```python

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    count = 1
    prev, cur, ptr = None, None, head
    while(ptr):
        if count == n:
            cur = head
        elif count > n:
            prev = cur
            cur = cur.next

        ptr = ptr.next
        count += 1

    if cur is None:
        return head
    if prev is None:
        return head.next

    prev.next = cur.next
    return head
```

## Merge Two Sorted Lists



```python

a = cur = ListNode(0)
     while l1 and l2:
         cur.next = l1
        if l1.val < l2.val:
             l1 = l1.next
        else:
            tmp = l2.next
            cur.next = l2
            l2.next = l1
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return a.next
```

## Palindrome Linked List



```python

def isPalindrome(self, head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] != arr[j]:
            return False
        else:
            i += 1
            j -= 1
    return True
```

## Middle of the Linked List



```python

 dict = {}

 i = 0
 while head:
     dict[i] = head
     head = head.next
     i += 1


 m = i // 2

 return dict[m]
```

## Reverse Linked List



```python

def reverseList(self, head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head
```
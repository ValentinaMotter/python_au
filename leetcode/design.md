+ [Min Stack](#ems/min-stack)
<!-----solution----->

## Min Stack

    https://leetcode.com/problems/min-stack/

```python
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append((val))

    def pop(self):
        if len(self.stack) != 0:
            del self.stack[-1]
        else:
            return None

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        if len(self.stack) != 0:
            return min(self.stack)
        else:
            return None


232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self,x):
        self.queue.append(x)

    def pop(self):
        if not self.empty():
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.empty():
            return self.queue[0]
        else:
            return None

    def empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False


225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return None

    def top(self):
        if not self.empty():
            return self.stack[-1]
        else:
            return None

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
```
+ [Max Consecutive Ones](#)
+ [Reshape the Matrix](#)
+ [Image Smoother](#)
+ [Flipping an Image](#)
+ [Transpose Matrix](#)
+ [Move Zeroes](#)
+ [Squares of a Sorted Array](#)
<!-----solution----->

## Squares of a Sorted Array



```python

def sortedSquares(self, nums: List[int]) -> List[int]:
sq_nums = []
for num in nums:
    sq_nums.append(num ** 2)

return sorted(sq_nums)
```

## Move Zeroes



```python

def moveZeroes(self, nums: List[int]) -> None:
 """
 Do not return anything, modify nums in-place instead.
 """
 nums.sort()
 i = 0
 while i < len(nums):
     if nums[i] == 0:
         nums.append(nums[i])
         nums.pop(i)
     else:
         break
 return nums
```

## Transpose Matrix



```python

def transpose(self, A: List[List[int]]) -> List[List[int]]:
tr_A = []

for i in range(len(A[0])):
    tr = []
    for j in range(len(A)):
        tr.append(A[j][i])
    tr_A.append(tr)
return tr_A
```

## Flipping an Image



```python

def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
 B = []
 for i in A:
     i.reverse()
     B.append(i)
 for j in B:
     i = 0
     while i < len(j):
         if j[i] == 1:
             j[i] = 0
         else:
             j[i] = 1

         i += 1
 return B
```

## Image Smoother



```python

def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
height = len(M)
width = len(M[0])

for i in range(height):
    prev = -1
    for j in range(width):
        next_prev = M[i][j]
        M[i][j] += (0 if prev == -1 else prev) + (0 if j == width-1 else M[i][j+1])
        prev = next_prev

for j in range(width):
    prev = -1
    for i in range(height):
        next_prev = M[i][j]
        M[i][j] += (0 if prev == -1 else prev) + (0 if i == height-1 else M[i+1][j])
        prev = next_prev

for i in range(height):
    for j in range(width):
        count = (0 if j == 0 else 1) + 1 + (0 if j == width-1 else 1)
        divisor = (0 if i == 0 else count) + count + (0 if i == height-1 else count)
        M[i][j] //= divisor

return M
```

## Reshape the Matrix



```python

def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
 if len(nums) * len(nums[0]) != r * c:
     return nums
 else:
     lst = []
     a = []
     new = []
     for n in nums:
         new.append(n[0])
         new.append(n[1])
     for i in range (0, len(new), c):
         a = new[i:i+c]
         lst.append(a)
     return lst
```

## Max Consecutive Ones



```python

 def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
        max_count = max(count, max_count)
        return max_count
```
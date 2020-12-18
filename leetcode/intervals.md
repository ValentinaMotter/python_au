+ [Non-overlapping Intervals](#)
+ [Merge Intervals](#)
+ [Insert Interval](#)
<!-----solution----->

## Insert Interval



```python

def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for index, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif newInterval[1] < interval[0]:
                result.append(newInterval)
                return result+intervals[index:]
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        result.append(newInterval)
        return result
```

## Merge Intervals



```python

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []
    for i in sorted(intervals, key=lambda i: i[0]):

        if res and i[0] <= res[-1][1]:
            res[-1][1] = max(i[1],res[-1][1])
        else:
            res += [i]

    return res
```

## Non-overlapping Intervals



```python

def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    p = intervals[0]
    deleted = 0
    for c in range(1, len(intervals)):
        s, e = intervals[c]
        if s < p[1]:
            deleted + = 1
        if e < p[1]:
            p = intervals[c]
    else:
        p = intervals[c]
    return(deleted)
```
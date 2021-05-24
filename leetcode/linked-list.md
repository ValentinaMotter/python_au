+ [Merge k Sorted Lists](#ems/merge-k-sorted-lists)
<!-----solution----->

## Merge k Sorted Lists

    https://leetcode.com/problems/merge-k-sorted-lists/

```python
def mergeLists(lists):
    return(sorted(sum(lists, [])))
```
+ [K Closest Points to Origin](#blems/k-closest-points-to-origin)
<!-----solution----->

## K Closest Points to Origin

      https://leetcode.com/problems/k-closest-points-to-origin/

```python
def kClosest(points, k):
      length = [[(point[0]**2 + point[1]**2)**0.5, point] for point in points]
      return [x[1] for x in sorted(length)][0:k]
```
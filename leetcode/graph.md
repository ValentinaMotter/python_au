+ [Course Schedule](#ems/course-schedule)
+ [Course Schedule II](#ems/course-schedule-ii)
+ [Number of Islands](#ems/number-of-islands)
+ [Is Graph Bipartite?](#ems/is-graph-bipartite)
+ [Cheapest Flights Within K Stops](#ems/cheapest-flights-within-k-stops)
<!-----solution----->

## Cheapest Flights Within K Stops

    https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    k += 1
    adj = [[None for j in range(n)] for i in range(n)]
    for fromSrc, to, price in flights:
        adj[fromSrc][to] = price
    dp = [[math.inf for j in range(k + 1)] for i in range(n)]
    for j in range(k + 1):
        dp[src][j] = 0

    for j in range(1, k + 1):
        for i in range(n):
            best = math.inf
            for vertex in range(n):
                if adj[vertex][i] != None and dp[vertex][j - 1] + adj[vertex][i] < best:
                    best = dp[vertex][j - 1] + adj[vertex][i]
            dp[i][j] = min(dp[i][j], best, dp[i][j - 1])

    return dp[dst][k] if dp[dst][k] != math.inf else -1
```

## Is Graph Bipartite?

    https://leetcode.com/problems/is-graph-bipartite/

```python
def isBipartite(self, graph: List[List[int]]) -> bool:
    color = [-1] * len(graph)

    def dfs(curr, color, col):
        if color[curr] == (col + 1) % 2:
            return False
        if color[curr] == col:
            return True

        color[curr] = col
        for j in graph[curr]:
            if not dfs(j, color, (col + 1) % 2):
            return False
        return True

    for i in range(len(graph)):
        if color[i] == -1:
            if not dfs(i, color, 0):
                return False
    return True

```

## Number of Islands

    https://leetcode.com/problems/number-of-islands/

```python
class Solution:
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
            return
        grid[row][col] = '0'
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row+1, col)
        self.dfs(grid, row, col-1)

    def numIslands(self, grid):
        if not grid:
            return
        num = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    num += 1
        return num

```

## Course Schedule II

    https://leetcode.com/problems/course-schedule-ii/

```python
class Solution:
    def findOrder(self, numCourses, prerequisites):
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit, cycle = set(), set()
        output = []

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True
        cycle.add(crs)

        for pre in preMap[crs]:
            if not dfs(pre):
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return []

    return output

```

## Course Schedule

    https://leetcode.com/problems/course-schedule/

```python
class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)} #сопоставляет каждому курсу количество его предшественников
        for crs, pre in prerequisites:
        preMap[crs].append(pre)
        visitSet = set()

    def dfs(crs, visitSet):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True
        visitSet.add(crs)

    for pre in preMap[crs]:
        if not dfs(pre, visitSet):
            return False
    visitSet.remove(crs)
    preMap[crs] = []
    return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True

```
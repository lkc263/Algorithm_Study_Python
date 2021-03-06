# DFS, BFS

**탐색** : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 한다.

**자료구조** : 데이터를 표현하고 처리하는 방법

**스택** : 선입후출 구조 또는 후입선출 구조

**큐** : 선입선출 구조

**dfs** : 깊이 우선 탐색, 그래프를 탐색하는 알고리즘, 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하며 스택 자료구조를 이용한다.

**bfs** : 너비 우선 탐색, 가까운 노드부터 탐색하는 알고리즘, 선입선출 방식의 큐를 이용하면 효과적으로 구현할 수 있다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면, 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색한다.

&nbsp;

### [Q 15]

모든 도로의 거리는 1이다. (간선의 비용 : 1)

**그래프에서 모든 간선의 비용이 동일할 때는 너비 우선 탐색(BFS)을 이용하여 최단 거리를 찾을 수 있다.**

모든 도로의 거리는 '1'이라는 조건 덕분에 너비 우선 탐색을 이용하여 간단히 해결할 수 있다.

너비 우선 탐색을 이용하여 시간 복잡도 O(N + M)으로 동작하는 소스코드를 작성하여 시간 초과 없이 해결할 수 있다.

특정한 도시 X를 시작점으로 BFS를 수행하여 모든 도시까지의 최단 거리를 계산한 뒤에, 각 최단 거리를 하나씩 확인하여 그 값이 K인 경우에 해당 도시의 번호를 출력하면 된다.

소스

```python
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 -1로 초기화
distance = [-1] * (n + 1)

distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()

    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)



# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
```

&nbsp;

### [Q 16] 연구소

벽을 3개 설치하는 모든 경우의 수를 다 계산해야 한다.

전체 맵의 크기가 8 X 8 = 64 이므로, 벽을 설치할 수 있는 모든 조합의 수는 최악의 경우(바이러스가 하나도 존재하지 않는 경우) 64C3이 될 것이다.

이는 100,000보다도 작은 수이므로, 모든 경우의 수를 고려해도 제한 시간 안에 문제를 해결할 수 있다는 것을 알 수 있다.

**모든 조합을 계산할 때는 파이썬의 조합 라이브러리를 이용하거나, DFS 혹은 BFS를 이용하여 해결할 수 있다.**

벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에 그러한 조합에 대해서 안전 영역의 크기를 계산하면 된다.

**안전 영역의 크기를 구하는 것 또한 DFS 혹은 BFS를 이용하여 계산할 수 있다.**

&nbsp;

초기에 비어 있는 모든 공간 중에서 3개를 골라 벽을 설치한다.

매번 벽을 설치할 때마다, 각 바이러스가 사방으로 퍼지는 것을 DFS/BFS로 계산하여 안전 영역을 구해야 한다.

(각 바이러스 위치에서 DFS나 BFS를 수행하여 연결된 모든 부분을 감염시키도록 처리할 수 있다.)

&nbsp;

소스

```python
n, m = map(int, input().split())
data = [] # 초기 list
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(dfs)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for idx  in range(4):
        next_x = x + dx[idx]
        next_y = y + dy[idx]
        
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        if temp[next_x][next_y] == 0:
            # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
            temp[next_x][next_y] = 2
            virus(next_x, next_y)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_zero_cnt():
    zero_cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                zero_cnt += 1

    return zero_cnt

# 깊이 우선 탐색(dfs)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result

    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
		# 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    # 바이러스 위치라면 전파하기
                    virus(i,j)
        # 0의 개수 찾기
        result = max(result, get_zero_cnt())
        return result
    else:
        # 빈 공간에 울타리 설치
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j] = 1
                    count += 1
                    dfs(count)
                    data[i][j] = 0
                    count -= 1



dfs(0)
print(result)
```

이번 문제를 풀며 알게 된 것

백준에서 채점을 할 때

복잡한 코드(반복)을 사용하는 경우 : PyPy3가 우세하기 때문에 PyPy3을 사용한다.

간단한 코드을 사용하는 경우 : Python3가 메모리, 속도 측에서 우세하기 때문에 Python3을 사용한다.

&nbsp;

### [Q 17] 경쟁적 전염

너비 우선 탐색을 이용하여 해결할 수 있다.

문제에 나와 있는대로 각 바이러스가 낮은 번호부터 중식한다.

초기, 큐에 원소를 삽입할 때는 낮은 바이러스의 번호부터 삽입해야 한다.

이후에, 너비 우선 탐색을 수행하며 방문하지 않은 위치를 차례대로 방문하도록 한다.

&nbsp;

소스

```python
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))

    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, cur_s, cur_x, cur_y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == cur_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        # 해당 위치로 이동할 수 없는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, cur_s + 1, nx, ny))


print(graph[x-1][y-1])
```

&nbsp;

### [Q 18] 괄호 변환

DFS 알고리즘의 핵심이 되는 재귀 함수 구현을 요구한다는 점에서 DFS 연습 목적의 문제

이 문제를 실수 없이 풀려면 소스코드를 최대한 단순화하는 것이 좋다.

**특정 문자열에서 "균형잡힌 괄호 문자열"의 인덱스를 반화하는 함수와 특정한 "균형잡힌 괄호 문자열"이 "올바른 괄호 문자열"인지 판단하는 메서드를 별도로 구현한다.**

&nbsp;

소스

```python

# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def corrected(u):
    count = 0 # 왼쪽 괄호의 개수
    for idx in range(len(u)):
        if u[idx] == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1

    return True # 쌍이 맞는 경우에 True 반환


def solution(p):
    answer = ''
    if p == '':
        return answer

    p_cur_index = balanced(p)
    u = p[:p_cur_index + 1]
    v = p[p_cur_index + 1:]

    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if (corrected(u)):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        # 만약 ( 없이 )이 먼저 시작된다면
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])  # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == ')':
                u[i] = '('
            else:
                u[i] = ')'

        answer += "".join(u)

    return answer

a = "()))((()"
b = ")("
print(solution(a))
```

&nbsp;

### [Q 19] 연산자 끼워 넣기

최대 11개의 수가 주어졌을 때, 각 수와 수 사이에 사칙연산 중 하나를 삽입하는 모든 경우에 대하여 만들어질 수 있는 결과의 최댓값 및 최솟값을 구하면 된다.

모든 경우의 수를 계산하기 위하여(완전 탐색) DFS 혹은 BFS를 이용하여 문제를 해결할 수 있다.

**중복 순열(product) 라이브러리**

```python
from itertools import product

n = 4
print(list(product(['+', '-', '*', '/'], repeat=(n-1))))
```

&nbsp;

소스

```python
# from itertools import product
# n = "1+2+3+4"
#
# n = 4
#
# print(list(product(['+','-','*','/'],repeat=(n-1))))

n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    if(i == n):
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / data[i]))
            div += 1


# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)

```

&nbsp;

### [Q 20] 감시 피하기

https://www.acmicpc.net/problem/18428

빅오 표기법 : O(N)이라면, 10억까지 가능하다. O(N^2)이라면 10억에 N으로 나눈 것까지 가능하다.

&nbsp;

장애물을 정확히 3개 설치하는 모든 경우를 확인하며, 매 경우마다 모든 학생을 감시로부터 피하도록 할 수 있는지의 여부를 출력해야 한다.

장애물을 정확히 3개 설치하는 모든 경우의 수

* 복도의 크기 N X N이며 N은 최대 6이다.
* 장애물을 정확히 3채 설치하는 모든 조합의 수는 최악의 경우 36C3이다.

&nbsp;

3개의 장애물이 설치된 모든 조합마다, 선생님들의 위치 좌표를 하나씩 확인하고 각각 선생님의 위치에서 상, 하, 좌, 우를 확인하며 학생이 한 명이라도 감지되는지를 확인해야한다.

선생님의 위치(T)에서 상, 하, 좌, 우의 위치를 확인하며 학생(S)이 존재하는지 확인하면 된다.

&nbsp;

소스

```python
from itertools import combinations

n = int(input()) # 복도의 크기

graph = [] # 복도 정보
teachers = [] # 모든 선생님 위치 정보
space = [] # 모든 빈 공간 위치 정보

for i in range(n):
    graph.append(list(input().split()))

    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        elif graph[i][j] == 'X':
            space.append((i, j))

# 특정 방향으로 감시를 진행(학생 발견: True, 학생 미발견: False)
def watch(x, y, directions):
    # 왼쪽 방향으로 감시
    if directions == 0:
        while y >= 0:
            if graph[x][y] == 'S': # 학생이 있는 경우
                return True
            if graph[x][y] == '0': # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if directions == 1:
        while y < n:
            if graph[x][y] == 'S': # 학생이 있는 경우
                return True
            if graph[x][y] == '0': # 장애물이 있는 경우
                return False

            y += 1
    # 위쪽 방향으로 감시
    if directions == 2:
        while x >= 0:
            if graph[x][y] == 'S': # 학생이 있는 경우
                return True
            if graph[x][y] == '0': # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if directions == 3:
        while x < n:
            if graph[x][y] == 'S':  # 학생이 있는 경우
                return True
            if graph[x][y] == '0':  # 장애물이 있는 경우
                return False
            x += 1
    return False


# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(space,3):
    # 장애물 설치 해보기
    for x, y in data:
        graph[x][y] = '0'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        graph[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
```
&nbsp;
### [Q 21] 인구 이동
https://www.acmicpc.net/problem/16234

전형적인 DFS/BFS 유형의 문제

모든 나라의 위치에서 상, 하, 좌, 우로 국경션을 열 수 있는지를 확인해야 한다.

모든 나라의 위치에서 DFS/BFS를 수행하여 인접한 나라의 인구수를 확인한 뒤에, 가능하다면 국경선을 열고 인구 이동 처리를 진행하면 된다.

ex)

| 50  | 30  |
|-----|-----|
| 30  | 40  |

각 나라의 위치에서 BFS를 수행하여, 연결되어 있는 모든 나라들(연합)을 찾는다.

현재 L = 20, R = 50이기 때문에, BFS를 수행해서 모든 연합을 찾으면 

| ***50*** | ***30*** |
|----------|----------|
| ***30*** | 40       |

이후에 같은 연합끼리 인구를 동일하게 분배하면 다음 그림과 같이 처리된다.

| ***36*** | ***36*** |
|----------|----------|
| ***36*** | 40       |

소스
```python
from collections import deque

# 땅의 크기(N), L, R값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y]  # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하여
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분해
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)

```
&nbsp;
### [Q 22] 블록 이동하기

전형적인 BFS 문제 유형

(1,1) 위치에 존재하는 로봇을 (N, N)의 위치로 옮기는 최단 거리를 계산하는 문제

**일반적인 BFS 문제와 다른 점**

로봇이 차지하고 있는 위치가 두 칸이며 회전을 통해 이동할 수 있다.

위치 정보를 튜플로 처리, 로봇의 상태를 집합 자료형(Set)으로 관리한다.

한 번 방문한 자전거의 상태는 두 번 방문하지 않는다.

**이동 가능한 위치**

**(1) 이동**

로봇이 단순히 '이동'하는 경우는 단순히 상, 하, 좌, 우로 이동하는 모든 경우를 계산하면 된다.

![1](https://user-images.githubusercontent.com/72541544/145530655-d76aad12-5f48-40b9-a6e3-0121e82a02b7.jpeg)

**(2) 회전**

(2-1) 로봇이 가로로 놓인 상태에서 아래쪽으로 회전하는 경우
* 로봇이 가로로 놓인 상태에서 아래쪽으로 회전하고자 한다면, 아래쪽에 벽이 없어야 한다.
* 아래쪽의 두 칸 중에서 하나라도 벽이 존재하는 경우 (값이 1인 경우)를 제외하고, 회전을 수행할 수 있다.
![2](https://user-images.githubusercontent.com/72541544/145530665-c8448831-5160-4420-8fe3-0c070fa1ab12.jpeg)

(2-2) 로봇이 가로로 놓인 상태에서 위쪽으로 회전하는 경우
* 현재 로봇이 가로로 놓인 상태에서 위쪽으로 회전하고자 한다면, 위쪽에 벽이 없어야 한다.
* 왼쪽의 두 칸 중에서 하나라도 벽이 존재하는 경우 (값이 1인 경우)를 제외하고, 회전을 수행할 수 있다.
![3](https://user-images.githubusercontent.com/72541544/145530668-3959e840-f7ed-4a41-acb9-5e6c68453c77.jpeg)

(2-3) 로봇이 세로로 놓인 상태에서 오른쪽으로 회전하는 경우
* 세로로 놓인 상태에서 오른쪽으로 회전하고자 한다면, 오른쪽에 벽이 없어야 한다.
* 오른쪽의 두 칸 중에서 하나라도 벽이 존재하는 경우 (값이 1인 경우)를 제외하고, 회전을 수행할 수 있다.
![4](https://user-images.githubusercontent.com/72541544/145530669-f2776ea6-2b11-46c0-be4b-bc7800c938ab.jpeg)

(2-4) 로봇이 세로로 놓인 상태에서 왼쪽으로 회전하는 경우
* 현재 로봇이 세로로 놓인 상태에서 왼쪽으로 회전하고자 한다면, 왼쪽에 벽이 없어야 한다.
* 왼쪽의 두 칸 중에서 하나라도 벽이 존재하는 경우 (값이 1인 경우)를 제외하고, 회전을 수행할 수 있다.
![5](https://user-images.githubusercontent.com/72541544/145530671-397aa543-a042-4bd1-9543-25cd406e57ce.jpeg)

소스코드를 간단하게 작성하기 위하여, 초기에 주어진 맵을 변형하여 외곽에 벽을 둘 수 있다.

시행시, 로봇이 맵을 벗어나지 않는지, 그 범위 판정을 더 간단히 할 수 있다.
![6](https://user-images.githubusercontent.com/72541544/145530672-5d4a5312-aaf0-4a4b-8316-da5ea065df1f.jpeg)

&nbsp;

소스

```python
from collections import deque


def get_next_pos(pos, board):
    next_pos = []  # 반환 결과(이동 가능한 위치들)
    pos = list(pos)  # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)

    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print("start", pos1_x, pos1_y, pos2_x, pos2_y)
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + \
                                                             dy[i]
        print(pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y)
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})

    print(next_pos)
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:  # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:  # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]:  # 왼쪽으로 회전하거나, 오른쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:  # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos


def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}  # 시작 위치 설정
    q.append((pos, 0))  # 큐에 삽입한 뒤에
    visited.append(pos)  # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인

        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0


data = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]

print(solution(data))

```

&nbsp;

&nbsp;

****

참고 자료

* '이것이 취업을 위한 코딩테스트다.' 한빛미디어
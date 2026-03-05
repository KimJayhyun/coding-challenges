## `itertools.permutations`

**발견:** 종이 조각으로 소수 만들기 (숫자들로 만들 수 있는 모든 순서 조합)  
**용도:** 이터러블에서 r개를 뽑아 순열 생성

**예제:**

```python
from itertools import permutations

list(permutations([1, 2, 3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]
```

**파라미터:**

```python
permutations(iterable, r)  # r개를 뽑아 순열 생성
permutations(iterable)     # r 생략시 전체 길이로 순열 생성
```

**직접 구현하면:**

```python
def my_permutations(arr, r):
    if r == 0:
        yield []
        return
    for i, x in enumerate(arr):
        rest = arr[:i] + arr[i+1:]
        for perm in my_permutations(rest, r - 1):
            yield [x] + perm
```

**이 문제에서의 활용 포인트:**  
길이 1 ~ len(numbers) 까지 모두 순열을 생성해야 함

```python
for r in range(1, len(numbers) + 1):
    permutations(numbers, r)
```

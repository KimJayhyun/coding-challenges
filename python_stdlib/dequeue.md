# Python `collections.deque` 정리

## 개요

`deque` (Double-Ended Queue)는 파이썬 `collections` 모듈에서 제공하는 자료구조로,
**양쪽 끝에서 삽입/삭제가 모두 O(1)** 로 동작한다.

```python
from collections import deque
d = deque()
```

---

## 핵심 특징: O(1) 성능

| 연산                   | list | deque   |
| ---------------------- | ---- | ------- |
| 오른쪽 삽입 `append`   | O(1) | O(1)    |
| 오른쪽 삭제 `pop`      | O(1) | O(1)    |
| 왼쪽 삽입 `appendleft` | O(N) | O(1) ✅ |
| 왼쪽 삭제 `popleft`    | O(N) | O(1) ✅ |

> `list.pop(0)` 은 O(N) 이지만, `deque.popleft()` 는 O(1) 이므로
> 큐(Queue)로 쓸 때 deque가 훨씬 유리하다.

---

# 주요 메서드 요약

```python
d = deque([1, 2, 3])

d.append(4)       # 오른쪽에 추가 → [1, 2, 3, 4]
d.appendleft(0)   # 왼쪽에 추가  → [0, 1, 2, 3, 4]
d.pop()           # 오른쪽 삭제  → [0, 1, 2, 3]
d.popleft()       # 왼쪽 삭제   → [1, 2, 3]
d.rotate(1)       # 오른쪽으로 1칸 회전 → [3, 1, 2]
d.rotate(-1)      # 왼쪽으로 1칸 회전  → [1, 2, 3]
```

---

## maxlen 옵션

크기를 고정할 수 있으며, 초과 시 반대쪽 요소가 자동으로 제거된다.

```python
d = deque(maxlen=3)
d.append(1)  # [1]
d.append(2)  # [1, 2]
d.append(3)  # [1, 2, 3]
d.append(4)  # [2, 3, 4] ← 1이 자동 제거됨
```

---

## 코딩테스트 활용 패턴

- **BFS**: `popleft()`로 큐처럼 사용
- **슬라이딩 윈도우**: 구간 내 최댓값/최솟값 탐색
- **회전 문제**: `rotate()` 메서드 활용
- **스택/큐 혼용**: 양쪽 끝을 모두 활용해야 하는 문제

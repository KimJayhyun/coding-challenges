# Python `heapq` 치트시트

## 기본 개념

- `heapq`는 **리스트를 힙처럼 다루는 함수 모음**
- 기본은 **최소 힙** (heap[0] 항상 최솟값)
- 내부 구조는 **완전 이진 트리를 리스트로 표현**

```
        1         (index 0)
       / \
      3   2       (index 1, 2)
     / \
    5   4         (index 3, 4)
```

---

## 기본 사용법

```python
import heapq

heap = []

# 값 추가
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

# 최솟값 꺼내기
heapq.heappop(heap)  # 1

# 두 개 꺼내기 (pop 후 자동 재정렬)
first = heapq.heappop(heap)
second = heapq.heappop(heap)
```

---

## 최대 힙

```python
# 음수로 변환해서 사용
heapq.heappush(heap, -3)
val = -heapq.heappop(heap)  # 3
```

---

## 튜플 사용

```python
# 첫 번째 값 기준 정렬, 같으면 두 번째 값 비교
heapq.heappush(heap, (-plays, index))
plays, index = heapq.heappop(heap)
plays = -plays
```

---

## 주요 함수 정리

```python
# 리스트를 힙으로 변환 (heappush 반복보다 빠름)
heap = [3, 1, 2]
heapq.heapify(heap)

# push와 pop을 동시에 (push 후 최솟값 반환)
heapq.heappushpop(heap, 4)

# 가장 큰 n개 반환
heapq.nlargest(2, heap)

# 가장 작은 n개 반환
heapq.nsmallest(2, heap)
```

---

## 인덱스 구조

| 노드        | 인덱스         |
| ----------- | -------------- |
| 부모        | `(i - 1) // 2` |
| 왼쪽 자식   | `2 * i + 1`    |
| 오른쪽 자식 | `2 * i + 2`    |

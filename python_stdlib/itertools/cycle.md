## `itertools.cycle`

**발견:** 수포자 문제 (패턴이 무한 반복되는 찍기 방식)  
**용도:** 리스트/이터러블을 무한 반복하는 제너레이터 생성

**예제:**

```python
from itertools import cycle

gen = cycle([2, 1, 2, 3, 2, 4, 2, 5])
next(gen)  # 2
next(gen)  # 1
```

**직접 구현하면:**

```python
def my_cycle(iterable):
    while True:
        for x in iterable:
            yield x
```

**주의:** 무한 루프이므로 `islice` 또는 `break` 없이 `list()`로 변환하면 안 됨 ⚠️

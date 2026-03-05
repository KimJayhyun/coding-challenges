## `itertools.islice`

**발견:** cycle이 무한 루프라 n개만 뽑아야 할 때  
**용도:** 제너레이터 같은 이터레이터에 슬라이싱 적용 (iterator slice)

**예제:**

```python
from itertools import cycle, islice

result = list(islice(cycle([2, 1, 2, 3]), 6))
# [2, 1, 2, 3, 2, 1]
```

**파라미터:**

```python
islice(iterable, stop)
islice(iterable, start, stop)
islice(iterable, start, stop, step)
```

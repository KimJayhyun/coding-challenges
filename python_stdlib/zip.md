`zip()`은 여러 iterable을 **같은 인덱스끼리 묶어주는** 내장 함수예요.

- 결과는 tuple의 iterator
- 길이가 다르면 짧은 쪽 기준으로 멈춤
- `zip_longest()`를 쓰면 긴 쪽 기준으로 동작 (빈 값은 `None`으로 채움)

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']

# 기본 사용
list(zip(a, b))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# for loop
for x, y in zip(a, b):
    print(x, y)  # 1 a, 2 b, 3 c

# 길이가 다를 때
list(zip([1, 2, 3], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# zip_longest
from itertools import zip_longest
list(zip_longest([1, 2, 3], ['a', 'b']))  # [(1, 'a'), (2, 'b'), (3, None)]
```

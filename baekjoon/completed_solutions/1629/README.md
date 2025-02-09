## 곱셈
### 문제

자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.


#### 예제
- 입력

첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

```text
10 11 12
```

- 출력

첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

```text
4
```

### 해결 방법

만약 우리가 \( A^B \) 를 직접 계산하려 하면 **큰 수 연산**이 발생해 연산 시간이 너무 길어진다.

#### **분할 정복을 이용한 거듭제곱**

우리는 **거듭제곱의 성질**을 이용해 시간 복잡도를 줄일 수 있다.

#### 핵심 아이디어: 지수를 반으로 나누기

거듭제곱의 성질을 활용하면 다음과 같이 나눌 수 있다.

\[
A^B \mod C
\]

를 구할 때,

1. \( B \) 가 **짝수**일 경우

\[
A^B = (A^{B/2}) * (A^{B/2})
\]

따라서

\[
(A^B) \mod C = (A^{B/2}) * (A^{B/2}) \mod C
\]


2. \( B \) 가 **홀수**일 경우

\[
A^B = (A^{B // 2}) * (A^{B // 2}) * A
\]

따라서

\[
(A^B) \mod C = (A^{B // 2}) * (A^{B // 2}) * A \mod C
\]

## 시간 복잡도 분석
이 알고리즘은 **분할 정복 (Divide & Conquer)** 방식으로 동작한다.

시간 복잡도는 **O(log B)** 이다.

### 의사 코드
```text
Algorithm ModularExponentiation(x, y, n)
    // Base cases
    if y = 1 then
        return 1
    end if
    
    if y = 1 then
        return x mod n
    end if

    // Recursive case using divide and conquer
    // Calculate half of the exponentiation
    root_x = ModularExponentiation(x, y/2, n)
    
    // If exponent is even
    if y is even then
        return (root_x * root_x) mod n
    // If exponent is odd
    else
        return (root_x * root_x * x) mod n
    end if
End Algorithm
```

### URL
- [곱셈](https://www.acmicpc.net/problem/1629)
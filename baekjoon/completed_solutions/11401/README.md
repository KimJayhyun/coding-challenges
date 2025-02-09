## 이항 계수 3
### 문제
```text
자연수 \(N\)과 정수 \(K\)가 주어졌을 때, 
이항 계수 \(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
```

#### 예제
- 입력

첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 4,000,000, 0 ≤ \(K\) ≤ \(N\))

- 출력 
\(\binom{N}{K}\)를 1,000,000,007로 나눈 나머지를 출력한다.

### 해결 방법

이전에 풀었던 [곱셈](https://www.acmicpc.net/problem/1629)과 페르마의 소정리를 활용하면 문제를 해결할 수 있다.

#### 분할 정복을 활용한 거듭제곱 계산

이 [문서](../1629/README.md)를 참고하여, 지수를 반으로 나누며 계산을 한다면,

`O(log 지수)` 시간에 거듭제곱 값을 구할 수 있다.

#### 페르마의 소정리와 역원

- `a ^ p = a (mod p)`

    임의의 소수 `p`는 모든 정수 `a`에 대해서 위를 만족한다는 것이 페르마의 소정리이다.

이를 활용해서 모듈러 역원을 찾을 수 있다.

```
a ^ p = a (mod p) 이므로
a ^ (p - 1) = 1 (mod p) 이고
a * a ^ (p - 2) == 1 (mod p)이다.

즉, a의 모듈러 역원은 a ^ (p - 2)
```

#### 풀이

`C(n,k) = n! / (k! * (n - k)!)`이다.

우리가 구하고 싶은 값은 소수인 `1000000007`로 나눈 값이므로 아래와 같이 계산할 수 있다.

```text
C(n,k) (mod p) = n! / (k! * (n - k)!) (mod p)

이 때, (k! * (n - k)!)의 모듈러 역원은 { (k! * (n - k)!) } ^ (p - 2)이므로

C(n,k) (mod P) = n ! * { (k! * (n - k)!)} ^ (p - 2)이다.

```

또한 팩토리얼 계산은 `O(n)`의 시간복잡도를 가지므로, 

너무 크지 않은 `n`에 대해서는 생각보다 빠른 연산 속도를 가진다.

### 의사 코드
```text
함수 power(x, y, n):
    만약 x가 1이면:
        1 반환
    
    만약 y가 1이면:
        x를 n으로 나눈 나머지 반환
    
    half ← power(x, y // 2, n)  // x^y를 분할 정복 방식으로 계산
    
    만약 y가 짝수이면:
        반환 (half * half) % n
    아니면:
        반환 (half * half * x) % n

함수 factorial(x, n):
    fact ← 1

    2부터 x까지 반복:
        fact ← (fact * 현재 숫자) % n  // 모듈러 연산을 유지하며 팩토리얼 계산
    
    반환 fact

함수 solution(n, k, DIVISOR):
    num ← factorial(n, DIVISOR)  // n! % DIVISOR 계산
    denom ← factorial(k, DIVISOR) * factorial(n - k, DIVISOR)  // k! * (n-k)! % DIVISOR 계산
    denom_inv ← power(denom, DIVISOR - 2, DIVISOR)  // 페르마의 소정리로 역원 계산

    반환 (num * denom_inv) % DIVISOR  // 이항 계수 C(n, k) % DIVISOR 반환
```

### URL
- [이항 계수 3](https://www.acmicpc.net/problem/11401)
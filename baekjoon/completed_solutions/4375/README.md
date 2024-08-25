## 1
### 문제
```text
2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때,
각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.
```

#### 예제
- 입력
```text
3
7
9901
```

- 출력 
```text
3
6
12
```


### 해결 방법
1. While True 
2. `loop_count`자리 숫자이면서 모든 자릿수가 1인 정수 생성
3. 나머지가 0 인지 확인
4. 맞으면 `break`, 틀리면 `continue`

### 의사 코드
```text
만약 n이 1이라면:
    1을 반환한다

변수 target_num을 1로 초기화
변수 digit을 1로 초기화

무한 루프 시작:
    digit을 1 증가
    target_num을 target_num * 10 + 1로 업데이트
    만약 target_num이 n으로 나누어 떨어지면:
        루프를 종료

digit을 반환
```

### URL
- [1](https://www.acmicpc.net/problem/4375)
## 가장 긴 증가하는 부분 수열 
### 문제
```text

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
```

#### 예제
- 입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

```text
6
10 20 10 30 20 50
```

- 출력 

첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

```text
4
```


### 해결 방법

### 의사 코드
```text
함수 solution():
    value_table을 크기 (max_weight + 1)로 초기화하고 모든 요소를 0으로 설정

    각 아이템 i에 대해 (data의 각 항목에 대해):
        weight = data[i][0]
        value = data[i][1]

        만약 weight가 max_weight보다 크다면:
            다음 아이템으로 건너뜀

        looping_weight를 max_weight에서 1까지 감소시키며 반복: ## 탑다운 방식
            
            만약 looping_weight + weight가 max_weight 이하이고,
            value_table[looping_weight]이 0이 아니라면:
            
                value_table[looping_weight + weight]을 다음 중 큰 값으로 업데이트:
                    - value_table[looping_weight + weight]
                    - value_table[looping_weight] + value

        value_table[weight]을 다음 중 큰 값으로 업데이트:
            - value_table[weight]
            - value

    value_table에서 최대 값을 반환
```

### URL
- [가장 긴 증기하는 부분 수열](https://www.acmicpc.net/problem/11053)
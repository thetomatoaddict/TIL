# 목차

[알고리즘01 시간 복잡도](#알고리즘01 시간 복잡도)

[알고리즘02 문자열](#알고리즘02 문자열)

[알고리즘03 딕셔너리](#알고리즘03 딕셔너리)

[알고리즘04 컴퓨터적 사고](#알고리즘04 컴퓨터적 사고)

[알고리즘05 스택과 큐](#알고리즘05 스택과 큐)

[알고리즘06 이차원 리스트 순회](#알고리즘06 이차원 리스트 순회)

[알고리즘07 DFS](#알고리즘07 DFS)





# 알고리즘01 시간 복잡도



## **시간복잡도**

> 문제를 해결하는데 걸리는 시간과 입력의 함수 관계를 가리킨다



- **단순하게 `알고리즘의 수행 시간` 을 의미**
  - 시간 복잡도가 높다 => 느린 알고리즘
  - 시간 복잡도가 낮다 => 빠른 알고리즘



- **시간 복잡도에 따라 알고리즘 성능 비교**
  - count(), `6n + 4` (선형 증가) => O(n)
  - count(), `3n + 2` (선형 증가) => O(n)
  - count(), `3n2 + 6n + 1` (제곱으로 증가) => O(n2)



- **기본연산의 총 횟수 == 알고리즘의 소요 시간**

------



## **빅오(Big-O) 표기법**

> 입력 n이 `무한대` 로 커진다고 가정하고 시간 복잡도를 간단하게 표시하는 것



- **다양한 시간 복잡도 종류 살펴보기**

[![img](https://github.com/Jobyeongjin/TIL/raw/master/git-start.assets/big_O.jpeg)](https://github.com/Jobyeongjin/TIL/blob/master/git-start.assets/big_O.jpeg)

| 표기       | 내용                                                         | 1초가 걸리는 입력의 크기(1억 기준) |
| ---------- | ------------------------------------------------------------ | ---------------------------------- |
| O(1)       | 단순 산술 계산 (덧셈, 뺄셈, 곱셉, 나눗셈) a + b, 100 * 200   | 1억                                |
| O(log N)   | 크기 N인 리스트를 반절씩 순회 / 탐색 이진탐색 (Binary Search), 분할정복 (Divide & Conquer) | 500만                              |
| O(N)       | 크기 N인 리스트를 순회 1중 for 문                            | -                                  |
| O(N log N) | 크기 N인 리스트를 반절씩 탐색 * 순회 높은 성능의 정렬 (Merge / Quick / Heap Sort) | -                                  |
| O(N^2)     | 크기 M, N인 2중 리스트를 순회 2중 for 문                     | 1만                                |
| O(N^3)     | 3중 리스트를 순회 3중 for 문                                 | 500                                |
| O(2^N)     | 크기 N 집합의 부분 집합                                      | 20                                 |
| O(N!)      | 크기 N 리스트의 순열                                         | 10                                 |



### **가우스의 합 공식 **

- 내장 함수, 메서드의 시간 복잡도도 확인할 필요가 있다 

```python
# for문을 사용할 경우
def get_total(n):
  total = 0
 	for i in range(1, n + 1):
    total += 1
  return total

print(get_total(10))
print(get_total(1000000000))



# 가우스의 합 공식을 사용할 경우
def get_total(n):
	return (n * (n + 1)) // 2

print(get_total(10))
print(get_total(1000000000))

```

------



## **리스트**

> 파이썬은 배열의 장점과 연결 리스트의 장점을 모두 가지고 있다



### **배열(Array)**

> 여러 데이터들이 연속된 메모리 공간에 저장되어 있는 자료구조

- `인덱스` 를 통해 데이터에 빠르게 접근
- 배열의 길이는 변경 불가능 => 길이를 변경하고 싶다면 새로 생성
- 데이터 타입은 고정



### **연결 리스트 (Linked List)**

> 데이터가 담긴 여러 노드들이 순차적으로 연결된 형태의 자료구조

- 맨 처음 노드부터 순차적으로 탐색
- 연결리스트의 `길이 자유롭게` 변경 가능 => `삽입, 삭제가 편리`
- `다양한 데이터 타입` 저장
- 데이터가 메모리에 연속적으로 저장되지 않음



### **파이썬 리스트의 메소드**

| 메소드      | 설명                                              | 표기       |
| ----------- | ------------------------------------------------- | ---------- |
| .append()   | 리스트 맨 끝에 새로운 원소 `삽입`                 | O(1)       |
| .pop()      | 특정 인덱스에 있는 원소를 `삭제 및 반환`          | O(1)       |
| .count()    | 리스트에서 행당 원소의 `개수` 를 반환             | O(n)       |
| .index()    | 리스트에서 처음으로 원소가 등장하는 `인덱스` 반환 | O(n)       |
| .sort()     | 리스트를 오름차순으로 `정렬`                      | O(n log n) |
| .reverse()  | 리스트를 원소들의 순서를 `거꾸로 뒤집기`          | O(n)       |
| .len()      | 리스트 `길이(원소의 개수)` 를 반환                | O(1)       |
| .sum()      | 리스트의 모든 원소의 `합` 을 반환                 | O(n)       |
| .max()      | 리스트의 원소 중 `최대값` 을 반환                 | O(n)       |
| .min()      | 리스트의 원소 중 `최소값` 을 반환                 | O(n)       |
| .sorted()   | 오름차순으로 `정렬된 새로운 리스트` 반환          | O(n log n) |
| .reversed() | 리스트의 순서를 `거꾸로 뒤집은 새로운 객체` 반환  | O(n)       |

------



#### 📚 참조

- 파이썬 연산자의 시간복잡도가 궁금하다면 [클릭](https://wiki.python.org/moin/TimeComplexity)
- 정리된 블로거가 궁금하다면 [클릭](https://dev.plusblog.co.kr/42) [/ 클릭](https://velog.io/@ggyungjun0913/파이썬-내장함수-시간-복잡도)





# 알고리즘02 문자열

## **문자열**

> 문자열은 **immutable(변경 불가능한)** 자료형

- 순회 가능한 자료형

```python
word = 'apple'
print(word)
print(id(word)) # 메모리 주소 확인
>>> apple
>>> 1352749370800

word += 'banana' # 추가된 데이터로 인해 word 기존의 'apple' 은 찾을 수 없다 🚨
print(word)
print(in(word))
>>> apple banana
>>> 1352749417520
```

------



## **슬라이싱**

> 문자열 자르기

```python
s = 'abcdefghi'

# 인덱스번호 2부터 4까지 사용하려면
s[2:5] # 'cde'

# -n을 마지막에 입력하면 n만큼 건너뛰며 회문하게 된다
s[2:5:-1] # ''
s[5:2:-1] # 'fed'

```

------



## **메소드**

| 메소드     | 설명                                                         |
| ---------- | ------------------------------------------------------------ |
| .split()   | 문자열을 일정 기준으로 나누어 리스트로 변환 <br />괄호 안에 값을 넣지 않으면 `공백을 기준`으로 설정 |
| .strip()   | 문자열의 양쪽 끝에 있는 특정 문자를 모두 제거한 새로운 문자열 반환<br />괄호 안에 값을 넣지 않으면 `공백을 제거 문자`로 설정<br />제거할 문자를 여러 개 넣으면 해당하는 모든 문자들을 제거 |
| .find()    | 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환<br />찾을 문자가 없다면 `-1` 반환 |
| .index()   | 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환<br />찾을 문자가 없다면 `오류` 발생 |
| .count()   | 문자열에서 특정 문자가 몇 개인지 반환<br />문자 뿐만 아니라, 문자열의 개수도 확인 가능 |
| .replace() | 문자열에서 기존 문자를 새로운 문자로 수정한 새로운 문자열 반환<br />특정 문자를 `빈 문자열('')로 수정`하여 마치 해당 문자를 삭제한 것 같은 효과 가능 |
| .join()    | iterable의 각각 원소 사이에 특정 문자를 삽입한 새로운 문자열 반환<br />공백 출력, 콤마 출력 등 원하는 출력 형태를 위해 사용 |

------



## **아스키(ASCII) 코드**

> 가장 본질적인 공통 코드 방식, American Standard Code for Information Interchange



- **알파벳을 표현**하는 대표 인코딩 방식



- **각 문자를 표현하는데 1byte (8bits) 사용**
  - `1bit` : 통신 에러 검출용
  - `7bit` : 문자 정보 저장 (총 128개)



- 컴퓨터는 **숫자만 이해** 할 수 있다
  - `비트(bit`) : 0과 1, 두 가지 정보만 표현
  - `바이트(byte)` : 데이터를 저장하는 기본 단위 (1 byte == 8 bits)



- ord(문자)
  - `문자 => 아스키코드` 로 변환하는 내장함수



- chr(아스키코드)
  - `아스키코드 => 문자` 로 변환하는 내장함수



- [아스키코드표](https://stepbystep1.tistory.com/10)





# 알고리즘03 딕셔너리



## **해시 테이블**

> 딕셔너리(dict)의 정식 이름, 파이썬에는 딕셔너리 자료구조가 내장 되어 있다



- 순서가 없음
- `Key` 는 `immutable (변경 불가능)`
- `해시 함수` : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수
  - `매핑` 이란 `하나의 값을 다른 값으로 대응` 시키는 것
- `해시` : 해시 함수를 통해 얻어진 값
- 해시 함수와 해시 테이블을 이용하기 때문에 **삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다**
  - 산술 계산으로 값이 있는 위치를 바로 알 수 있기 때문



### **리스트와 딕셔너리 비교**

| 연산 종류   | 딕셔너리(Dictionary) | 리스트(List)   |
| ----------- | -------------------- | -------------- |
| Get Item    | O(1)                 | O(1)           |
| Insert Item | O(1)                 | O(1) 또는 O(N) |
| Update Item | O(1)                 | O(1)           |
| Delete Item | O(1)                 | O(1) 또는 O(N) |
| Search Item | O(1)                 | O(N)           |



### **딕셔너리는 언제 사용할까?**

- 리스트를 사용하기 힘든 경우

- 데이터에 대한

   

  ```
  빠른 접근 탐색
  ```

   

  이 필요한 경우

  - 현실 세계의 대부분의 데이터를 다룰 경우

------



## **기본 문법**

> 변수 = {key1: value1, key2: value2}



```python
# 'Key' : Value 구성의 딕셔너리
a = {
  'name': 'kyle',
  'gender': 'male',
  'address': 'Seoul'
}
print(a)


# 삽입
a['job'] = 'coach'


# 수정
a['name'] = 'john'


# 삭제 및 반환
# default 값을 지정하여 KeyError 방지 가능
gender = a.pop('name')
gender = a.pop('age', 29)
print(gender)


# 조회
# get은 default 값을 지정하여 조절 가능
age = a['age']
age = a.get('age', 30)


# Counting
scores = ['A', 'A', 'B', 'C', 'D', 'A', 'B']

counter = {
  'A' = 0,
  'B' = 0,
  'C' = 0,
  'D' = 0
}

for score in scores:
  counter[score] += 1

print(counter)


# Counter 내장함수 활용
from collections import Counter

socres = ['A', 'A', 'B', 'C', 'D', 'A', 'B']

easy_counter = Counter(scores)

print(easy_counter)
```

------



## **메소드**



| 메소드   | 설명                                         |      |
| -------- | -------------------------------------------- | ---- |
| .keys()  | Key 목록이 담긴 dict_keys 객체 반환          |      |
| .valus() | Value 목록이 담긴 dict_values 객체 반환      |      |
| .items() | Key, Value 목록이 담긴 dict_values 객체 반환 |      |

```python
john = {
  'name': 'john',
  'role': 'ceo'
}

# 키를 전부 뽑아낼 때
for key in john.keys():
  print(key)


# 키, 밸류 전부 뽑아낼 때
for k, v in john.items():
  print(k, v)
data = {}


# Counter함수로 리스트를 요소:빈도수 형태의 딕셔너리로 변환 

user_input = ['Jay', 'John', 'John', 'Jay', 'Jack', 'Jack', 'John', 'Jo', 'Jo']

from collections import Counter

print(Counter(user_input))

# most_common 메서드
print(Counter(user_input).most_common())
```

------







# 알고리즘04 컴퓨터적 사고



## **논리**

> 논리를 바탕으로 짜여진 게 컴퓨터 과학



### **비둘기집 원리**

> n + 1 개의 물건을 n 개의 상자에 넣은 경우, 최소한 한 상자에는 그 물건이 반드시 두 개 이상 들어있다는 원리



1. `n 개의 비둘기 집` 과 `n + 1 마리의 비둘기` 가 있다는 것을 가정한다.
2. 각각의 집에 한 마리 이하의 비둘기만 들어 있다면, 전체 비둘기 집에는 모두 합쳐 n 마리 이하의 비둘기가 존재한다.
3. 비둘기의 전체 숫자는 n + 1 마리이므로, 2번은 모순이 된다. 따라서 `어느 비둘기 집에는 두 마리 이상의 비둘기가 존재` 한다.



이 과정을 통해 어느 비둘기 집에 2마리의 비둘기가 있다는 것을 증명할 순 있다. 그러나 비둘기 집이 어느 집인지는 이 증명으로는 알 수 없다.

------



## **Computational Thinking**

> 컴퓨터적 사고

- 컴퓨터적 사고는 우리가 `복잡한 문제들을 해결` 하고, `무슨 문제인지 이해` 하고, `가능한 해결책` 들을 개발할 수 있게 한다. 우리는 컴퓨터 또는 인간이 이해할 수 있는 해결책들을 제시할 수 있다.



### **구성 요소**

| 요소      | 설명                                                         | 비고 |
| --------- | ------------------------------------------------------------ | ---- |
| 분해      | **큰 문제를 작은 문제로 쪼개는 것** 복잡한 문제, 어려운 문제라도 분해하면 쉽게 해결할 수 있음 |      |
| 추상화    | 문제를 해결하기 위해 필요한 요소를 파악하고 그것을 **단순화**하여 표현 |      |
| 패턴 인식 | 사람이 **반복적으로 행동**하는 방식 데이터에 반복적으로 나타나는 패턴 |      |
| 알고리즘  | 문제 해결을 위한 **논리적 처리 과정**                        |      |
| 자동화    | 사람의 개입 없이 **컴퓨터가 혼자 수행**하도록 하는 것        |      |



### **문제 풀이 순서**

> 반드시 시각적으로 정리를 한다. 구글 형님들도 종이에 적으면서. 정리하면서 접근한다!

- 문제 인식
- 접근 방법
- 수도 코드 / 주석
- 코드 구현
- 디버깅



## **해외 알고리즘 사이트**



| 사이트     | 특징                                                         |
| ---------- | ------------------------------------------------------------ |
| LeetCode   | 경력직 개발자 코딩테스트 준비의 정석 개인용 문제 풀이 서비스 |
| HackerRank | 카카오, 네이버 경력 채용 등 적극 활용 신입과 유사하게 정리 가능 |
| Codility   | 카카오, 네이버 경력 채용 등 적극 활용 신입과 유사하게 정리 가능 |





# 알고리즘05 스택과 큐





## **스택 (Stack)**

> 스택(Stack)은 쌓는다는 의미로써, 마치 접시를 쌓고 빼듯이 데이터를 한쪽에서만 넣고 빼는 자료구조
>
> 가장 마지막에 들어온 데이터가 가장 먼저 나가는 LIFO(Last-in First-out, 후입선출) 방식



### **스택 자료구조의 대표 동작**

- 스택에 `새로운 데이터를 삽입 `하는 행위 ==> **push**
- 스택의 가장 `마지막 데이터를 가져오는` 행위 ==> **pop**
- 파이썬은 리스트(List)로 스택을 간편하게 사용할 수 있다
  - append, pop 활용

### **왜 (why) 스택을 써야할까 ?**

1. 데이터를 뒤집어야 할 때 `뒤집기, 되돌리기, 되돌아가기`
2. 마무리 되지 않은 일을 `임시 저장`



### **스택 활용 예시**

- **함수 호출 (재귀 호출)**

```python
print(sum(max(min(2, 5), 10), min(2, 5))) # 출력하려고 하니 함수가 끝나지 않음
>>> print(sum(max(2, 10), min(2, 5)))
>>> print(sum(10, min(2, 5)))
>>> print(sum(10, 2))
>>> 12
```

- **백트래킹**
- **DFS(깊이 우선 탐색)**



## **큐 (Queue)**

> 한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조
>
> 가장 먼저 들어온 데이터가 가장 먼저 나가므로 FIFO(First-in First-out, 선입선출) 방식



### **큐 자료구조의 대표 동작**

- 맨 뒤에 데이터를 삽입하는 행위 ==> enqueue
- 맨 앞 데이터를 가져오는 행위 ==> dequeue
- 파이썬은 리스트(List)로 큐를 간편하게 사용할 수 있다
  - 넣을 때 ==> append
  - 뺄 때 ==> pop(0)



### **큐의 단점**

> 데이터를 뺄 때 큐 안에 있는 데이터가 많은 경우 비효율적이다

- 맨 앞 데이터가 빠지면서, 리스트의 인덱스가 하나씩 당겨지기 때문
- 큐보다는 덱을 활용하는 게 낫다



### **큐 활용 예시**

```python
n = int(input())
queue = list(range(1, n + 1))

while len(queue) > 1:
  print(queue.pop(0), end=' ')
  queue.append(queue.pop(0))

print(queue[0])
```

------



## **덱(Deque, Double-Ended ) 자료구조**

- `양 방향` 으로 삽입과 삭제가 자유로운 큐
- **삽입, 추출이 모두 큐보다 훨씬 빠르다**



### **덱 활용 예시**

```python
# 큐
from collections import deque

n = int(input())
queue = deque(range(1, n + 1))

while len(queue) > 1:
  print(queue.popleft(), end=' ')
  queue.append(queue.popleft())

print(queue[0])


# 덱
numbers = [1, 2, 3, 4, 5]

queue = deque(numbers)

queue.append(6)

queue.popleft()

print(queue)
>>> deque([2, 3, 4, 5, 6])

# 리스트 형태로 출력
print(list(queue))
>>> [2, 3, 4, 5, 6]

# 하나씩 출력
for num in queue:
  print(num, end=' ')
>>> 2 3 4 5 6
```



# 알고리즘06 이차원 리스트 순회

## **순회**

1. **인덱스를 통해 각각 출력**

```
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3])

>>> 1 2 3 4
>>> 5 6 7 8
>>> 9 0 1 2
```

1. **이중 for 문을 이용한 `행 우선` 순회**

```
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

for i in range(3): # 행
  for j in range(4): # 열
    print(matrix[i][j], end=' ') # 좌표 (i, j)
  print()

>>> 1 2 3 4
>>> 5 6 7 8
>>> 9 0 1 2


# n * m
n = len(matrix)
m = len(matrix[0])

for i in range(n):
  for j in range(m):
    print(matrix[i][j], end=' ')
  print()

>>> 1 2 3 4
>>> 5 6 7 8
>>> 9 0 1 2


# matrix
for row in matrix:
  for elem in row:
    print(elem, end=' ')
  print()

>>> 1 2 3 4
>>> 5 6 7 8
>>> 9 0 1 2
```

1. **이중 for 문을 이용한 `열 우선` 순회**

```
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

for i in range(4): # 열
  for j in range(3): # 행
    print(matrix[j][i], end=' ')
  print()

>>> 1 5 9
>>> 2 6 0
>>> 3 7 1
>>> 4 8 2
```

------



### **총합 구하기**

```
matrix = [
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1]
]

total = sum(map(sum, matrix)) # map() => sum을 matrix 안 리스트에 각각 적용 💡

print(total)
>>> 12


# n * m
matrix = [
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1]
]

n = len(matrix)
m = len(matrix[0])

total = 0
for i in range(n):
  for j in range(m):
    total += matrix[i][j]

print(total)
>>> 12


# matrix
matrix = [
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1]
]

total = 0
for row in matrix:
    total += sum(row)

print(total)
>>> 12


#
def matrix_sum(matrix):
  return sum(map(sum, matrix))

matrix_sum(matrix)
```



### **최대값과 최소값 구하기**

```
# 최대값
matrix = [
  [0, 5, 3, 1],
  [4, 6, 10, 8],
  [9, -1, 1, 5]
]

max_value = 0

for i in range(3):
  for j in range(4):
    if matrix[i][j] > max_value:
      max_value = matrix[i][j]

print(max_value)
>>> 10


# 최소값
matrix = [
  [0, 5, 3, 1],
  [4, 6, 10, 8],
  [9, -1, 1, 5]
]

min_value = 99999999

for i in range(3):
  for j in range(4):
    if matrix[i][j] < min_value:
      min_value = matrix[i][j]

print(min_value)
>>> -1


# Pythonic 💡
matrix = [
  [0, 5, 3, 1],
  [4, 6, 10, 8],
  [9, -1, 1, 5]
]

max_value = max(map(max, matrix))
min_value = min(map(min, matrix))

print(max_value)
>>> 10

print(min_value)
>>> -1
```



### **이차원 리스트 순회 연습**

```
list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]
list_c = [[0] * 3 for _ in range(2)]

# 두 배열의 같은 위치끼리 곱하여 새로운 이차원 리스트에 저장
for i in range(2):
  for j in range(3):
    list_c[i][j] = list_a[i][j] * list_b[i][j]

# 결과 출력하기
for i in range(2):
  for j in range(3):
    print(list_c[i][j], end=' ')
  print()
```

------



## **전치**

> 행렬의 행과 열을 서로 맞바꾸는 것

```
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 0, 1, 2]
]

transposed_matrix = [[0] * 3 for _ in range(4)] # 전치 행렬을 담을 이차원 리스트 초기화 (행과 열의 크기가 반대)

for i in range(4):
  for j in range(3):
    transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기
```

------



## **회전**

> 이차원 리스트를 왼쪽, 오른쪽으로 90도 회전

```
# 왼쪽으로 90도 회전하기
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

n = 3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    rotated_matrix[i][j] = matrix[j][n - i - 1]


# 오른쪽으로 90도 회전하기
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

n = 3
rotated_matrix = [[0] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    rotated_matrix[i][j] = matrix[n - j - 1][i]
```



# 알고리즘07 DFS

> 깊이 우선 탐색
>
> 부모->자식 순으로 탐색함
>
> stack 혹은 재귀함수 사용
>
> 방문기록 확인 필요

- 재귀함수
  - 자기 자신을 호출하는 함수
  - DFS, 백트래킹에서 사용
  - 처리할 데이터 양이 많으면 사용X



## 주어진 자료가 인접행렬일 경우

> 델타행렬이 필요함

```python
def dfs(y,x):
    for d in delta:
        dy=y+d[0]
        dx=x+d[1]
        if 0<=dy<h and 0<=dx<w :
            if graph[dy][dx] == 1 and visit[dy][dx] == False :
                visit[dy][dx] = True
                dfs(dy,dx)
```



## 주어진 자료가 인접리스트인 경우

```python
def dfs(s):
    for i in graph[s]:
        if visit[i] == 0:
            visit[i] = visit[s] + 1
            dfs(i)
```


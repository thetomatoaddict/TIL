# 👻Python🧠



## 목차

- 기초문법
- 자료형
- 컨테이너
- 함수
- 내장함수





### 기초문법



#### 코드 스타일 가이드

> 코드를 '어떻게 작성할지'에 대한 가이드라인

• 파이썬에서 제안하는 스타일 가이드

   PEP8 (https://www.python.org/dev/peps/pep-0008/ )

• 기업, 오픈소스 등에서 사용되는 스타일 가이드

   Google Style guide (https://google.github.io/styleguide/pyguide.html) 등



#### Space Sensitive

• 문장을 구분할 때, 들여쓰기 (indentation)>를 사용 

• 들여쓰기를 할 때는 4칸(space키 4번) 혹은 1탭(Tab키 1번)을 입력 

• 주의! 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용 → 혼용하면 안됨 

• Tab으로 들여쓰면 계속 탭으로 들여써야 함 

• 원칙적으로는 공백 (빈칸, space) 사용을 권장* PEP8 권장사항



#### 변수

• 변수는 할당 연산자(=)를 통해 값을 할당(assignment) 

• type()

   변수에 할당된 값의 타입 

• id()

   변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리주소



#### 식별자

파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name) 

• 규칙

   • 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성

   • 첫 글자에 숫자가 올 수 없음

   • 길이제한이 없고, 대소문자를 구별

   • 다음의 키워드(keywords)는 예약어(reserved words)로 사용할 수 없음

> False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield



#### 주석

• 코드에 대한 설명

   • 중요한 점이나 다시 확인하여야 하는 부분을 표시

   • 컴퓨터는 주석을 인식하지 않음 사용자만을 위한 것

• 가장 중요한 습관

​    • 개발자에게 주석을 작성하는 습관은 매우 중요

​    • 쉬운 이해와 코드의 분석 및 수정이 용이

​          ✓ 주석은 코드 실행에 영향을 미치지 않을 뿐만 아니라

​          ✓ 프로그램의 속도를 느리게 하지 않으며, 용량을 늘리지 않음





### 자료형



#### Boolean Type

- True or False

- 0, 0.0, (), [], {}, '', None = 모두 False

- 논리연산자(and, or, not) 사용하여 검증

- bool() 함수로 True인지 False인지 검증
  
- int(x==y) 로 사용할 경우 true가 1, false가 0으로 출력됨

  

#### Numeric Type

- int
- float
- complex(복소수)
- 비교연산자(<,<=,==,!=..)를 이용해 true나 false 리턴
- 산술연산자(+,-,*,%,/,//,**)에 =을 붙여 복합연산자로 사용
- 비트시프트 연산자 (>>,<<)



#### String Type

- 삼중따옴표(''')를 사용하면 모든 내용을 그대로 출력한다.
- 리스트처럼 인덱싱, 슬라이싱 가능
- 결합(+), 반복(*****n), 포함('a' **in** 'apple' =>true or false 리턴) 사용
- %s, %d, %f 사용하여 변수 활용



#### Typecasting(자료형 변환)

- 파이썬에서 데이터 형태는 서로 변환할 수 있음





### 컨테이너



#### 시퀀스 (ordered)

- 문자열 : 문자들의 나열
  - [문자 개수 세기(count)](https://wikidocs.net/13#count)
  - [위치 알려주기1(find)](https://wikidocs.net/13#1find)
  - [위치 알려주기2(index)](https://wikidocs.net/13#2index)
  - [문자열 삽입(join)](https://wikidocs.net/13#join)
  - [소문자를 대문자로 바꾸기(upper)](https://wikidocs.net/13#upper)
  - [대문자를 소문자로 바꾸기(lower)](https://wikidocs.net/13#lower)
  - 대문자를 소문자로, 소문자를 대문자로 (swapcase)
  - 첫번째 글자를 대문자로 (capitalize)
  - [왼쪽 공백 지우기(lstrip)](https://wikidocs.net/13#lstrip)
  - [오른쪽 공백 지우기(rstrip)](https://wikidocs.net/13#rstrip)
  - [문자열 지우기(strip)](https://wikidocs.net/13#strip)
  - [문자열 바꾸기(replace)](https://wikidocs.net/13#replace)
  - [문자열 나누기(split)](https://wikidocs.net/13#split)
  - 문자열이 ~로 끝나는 것을 찾기(endwith)
  - 문자열이 ~로 시작하는 것을 찾기(startswith)
- 레인지 : 숫자의 나열, range(n, m s) 로 수열 생성 가능
- 리스트 : 변경 가능한 값들의 나열, []
  - [리스트에 요소 추가(append)](https://wikidocs.net/14#append)
  - [리스트 정렬(sort)](https://wikidocs.net/14#sort)
  - [리스트 뒤집기(reverse)](https://wikidocs.net/14#reverse)
  - [위치 반환(index)](https://wikidocs.net/14#index)
  - [리스트에 요소 삽입(insert)](https://wikidocs.net/14#insert)
  - [리스트 요소 제거(remove)](https://wikidocs.net/14#remove)
  - [리스트 마지막 요소 리턴 후 제거(pop)](https://wikidocs.net/14#pop)
  - [리스트에 포함된 요소 x의 개수 세기(count)](https://wikidocs.net/14#x-count)
  - [리스트+리스트 확장(extend)](https://wikidocs.net/14#extend)
- 튜플 : 변경 불가능한 값들의 나열, ()
- 시퀀스형 연산자 : len() min() max() 등



#### 비시퀀스 (unordered)

- 세트 : 값들의 집합 (중복값 없음, 순서 없음)
- 딕셔너리 : 키-값들의 집합
  - [Key 리스트 만들기(keys)](https://wikidocs.net/16#key-keys)
  - [Value 리스트 만들기(values)](https://wikidocs.net/16#value-values)
  - [Key, Value 쌍 얻기(items)](https://wikidocs.net/16#key-value-items)
  - [Key: Value 쌍 모두 지우기(clear)](https://wikidocs.net/16#key-value-clear)
  - [Key로 Value얻기(get)](https://wikidocs.net/16#key-valueget)
  - [해당 Key가 딕셔너리 안에 있는지 조사하기(in)](https://wikidocs.net/16#key-in)





### 함수

> ![img](https://wikidocs.net/images/page/24/mixer.png)

- def 함수명 (파라미터) 

  ```python
  def 함수명(매개변수):
      <수행할 문장1>
      <수행할 문장2>
      ...
  ```

- 파라미터나 리턴값이 없는 함수도 가능함
- def 함수명 (*파라미터이름)
  파라미터의 갯수가 정해져있지 않는 경우 이렇게 작성하면 입력값을 튜플 형식으로 저장한다.
- def 함수명 (**파라미터이름)
  파라미터의 갯수가 정해져있지 않는 경우 이렇게 작성하면 입력값을 딕셔너리 형식으로 저장한다.





### 내장함수



#### map

- map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.

- map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.

- 예제 : 정수에 2를 곱해주는 함수를 만들어서 map으로 리스트의 모든 요소에 적용

  ```python
  >>> def two_times(x): 
  ...     return x*2
  ...
  >>> list(map(two_times, [1, 2, 3, 4]))
  [2, 4, 6, 8]
  ```


#### print
- f string 사용하기
	- 변수와 문자열을 같이 출력하기
		- print(f'{n}일차\n')
	- 결과값을 반올림하여 출력하기
		- print(f'#{i+1}',f'{sum(nums)/10:.0f}')


### 1. 내장된 math 함수

어떤 모듈도 import 하지 않고 사용할 수 있는 내장함수들입니다.

#### min, max 함수

min은 최소값, max는 최대값을 리턴해줍니다.

```python
x = min(-5, 0, 5, 10)
y = max(-5, 0, 5, 10)
print(x)
print(y)
```

Output:

```log
-5
10
```

#### abs 함수

abs는 절대값을 리턴해 줍니다.

```python
x = abs(-12.34)
y = abs(12.34)
print(x)
print(y)
```

Output:

```log
12.34
12.34
```

#### pow 함수

pow는 숫자를 제곱하여 리턴합니다. 아래 코드는 2를 4번 제곱한 값을 리턴합니다.

```python
x = pow(2, 4)
print(x)
```

Output:

```log
16
```

#### round 함수

round는 정수를 반올림한 값을 리턴합니다. 소수가 `0.5`라면 무조건 올림하지 않고 짝수에 가까운 값을 리턴합니다.

```python
x = round(2.5)
y = round(3.5)
z = round(-5.6)
print(x)
print(y)
print(z)
```

Output:

```log
2
4
-6
```

### 2. math 모듈 import 및 사용 방법

다음과 같이 math 모듈을 import할 수 있습니다.

```python
import math
```

#### ceil 함수

ceil은 소수를 올림한 값을 리턴합니다.

```python
x = math.ceil(2.5)
y = math.ceil(3.5)
print(x)
print(y)
```

Output:

```log
3
4
```

#### floor 함수

floor는 소수를 버림한 정수를 리턴합니다.

```python
x = math.floor(2.5)
y = math.floor(3.5)
print(x)
print(y)
```

Output:

```log
2
3
```

#### sqrt 함수

sqrt는 인자로 전달된 정수의 제곱근을 리턴합니다.

```python
x = math.sqrt(36)
print(x)
```

Output:

```log
6
```

#### fabs 함수

fabs는 abs와 마찬가지로 절대값을 리턴합니다.

```python
x = math.fabs(-12.34)
y = math.fabs(12.34)
print(x)
print(y)
```

Output:

```log
12.34
12.34
```

#### pi 함수

pi는 PI 값을 리턴합니다.

```python
x = math.pi
print(x)
```

Output:

```log
3.141592653589793
```

#### exp 함수

exp는 지수함수 값을 리턴합니다.

```python
x = math.exp(1)
print(x)
```

Output:

```log
2.718281828459045
```
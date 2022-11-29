## 변수와 식별자

- 식별자는 변수를 구분할 수 있는 변수명
- 식별자는 반드시 문자, 달러 또는 밑줄로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능

### let, const

- let: 재할당 가능, 재선언 불가능
- const: 재할당 불가능, 재선언 불가능
- 블록 스코프

### var

- var: 재선언, 재할당 모두 가능
- 함수 스코프

### 호이스팅

- 변수를 선언 이전에 참조할 수 있는 현상
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환
- var, let, const 모두 호이스팅 발생하지만, var는 선언과 초기화가 동시에 발생하여 일시적 사각지대 존재하지 않음

## 데이터 타입

### 원시 타입

- 객체가 아닌 기본 타입
- 변수에 해당 타입의 값이 담김
- 다른 변수에 복사할 때 실제 값이 복사

### 참조 타입

- 객체 타입의 자료형
- 변수에 해당 객체의 참조 값이 담김
- 다른 변수에 복사할 때 참조 값이 복사됨

### 숫자 타입

- 정수, 실수 구분 없는 하나의 숫자 타입
- 부동 소수점 형식을 따름

```
const a = 13;
const b = -5;
const c = 3.14;
const d = 2.998e8;
const e = Infinity;
const f = -Infinity;
const g = NaN;
```

### 문자열 타입

- 텍스트 데이터를 나타내는 타입
- 16비트 유니코드 문자의 집합
- 작은 따옴표 또는 큰 따옴표 모두 가능
- 템플릿 리터럴
  - backtick으로 표현
  - ${expression} 형태로 표현식 삽입 가능

### undefined

- 변수의 값이 없음을 나타내는 데이터 타입
- 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨

### null

- 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입

### boolean 타입

- 논리적 참 또는 거짓을 나타내는 타입
- true 혹은 false로 표현
- 조건문 또는 반복문에서 유용하게 사용

## 연산자

### 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자

### 비교 연산자

- 피연산자를 비교하여 결과값을 boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  - 알파벳 순서상 후순위가 더 큼
  - 소문자가 대문자보다 더 큼

### 동등 비교 연산자(==)

- 두 피연산자가 값은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교

```
const a = 1004;
const b = "1004";
console.log(a == b); //true
```

### 일치 비교 연산자(===)

- 두 피연산자가 값은 값으로 평가되는지 비교 후 boolean 값을 반환
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음

```
const a = 1004;
const b = "1004";
console.log(a === b); //false
```

### 논리 연산자

- and: '&&'
- or: '||'
- not: '!'

### 삼항 연산자

- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 왼쪽의 조건식이 참이면 콜론 앞의 값을 사용하고 그렇지 않으면 콜론 뒤의 값을 사용

```
const result = Math.PI > 4 ? "YES" : "NO";
console.log(result); //NO
```

## 조건문

- 'if' statement
  - 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단
- 'switch' statement
  - 조건 표현식의 결과값이 어느 값에 해당하는지 판별

## 반복문

- while
- for
- for ... in
  - 객체 속성(key)들을 순회할 때 사용
- for ... of
  - 반족 가능한 객체를 순회하며 값을 꺼낼 때 사용

## 함수

### 함수의 정의

```
function name(args) {
  //do something
}
```

- 인자 작성 시 '='문자 뒤 기본 인자 선언 가능
- 매개 변수와 인자의 개수 불일치 허용

### 함수 표현식 (airbnb)

```
const add = function (args) {};
```

### 함수 선언식

```
function sub(args) {}
```

### 표현식 vs 선언식

- 호이스팅
  - 함수 선언식: var로 정의한 변수처럼 호이스팅 발생
  - 함수 표현식: 함수 정의 전에 호출 시 에러 발생

## Arrow Function

### 화살표 함수

- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드 생략 가능
- 함수 매개변수 단 하나뿐이라면 '()' 생략 가능
- 함수 몸통이 표현식 하나라면 '{}'과 return도 생략 가능

## 문자열

### includes

- string.includes(value)
  - 문자열에 value가 존재하는 판별 후 참 또는 거짓 반환

### split

- string.split(value)
  - value가 없을 경우, 기존 문자열을 배열에 담아 반환
  - value가 빈 문자열일 경우, 각 문자로 나눈 배열을 반환
  - value가 기타 문자열이 경우, 해당 문자열로 나눈 배열을 반환

### replace

- string.replace(from, to)
  - 문자열에 from 값이 존재할 경우, '1개만' to 값으로 교체하여 반환
- string.replaceAll(from, to)
  - 문자열에 from 값이 존재할 경우, '모두' to 값으로 교체하여 반환

### trim

- string.trim()
  - 문자열 시작과 끝 모든 공백 문자를 제거한 문자열 반환
- string.trimStart()
  - 문자열 시작의 공백 문자를 제거한 문자열 반환
- string.trimEnd()
  - 문자열 끝의 공백 문자를 제거한 문자열 반환

## 배열

### 정의와 특징

- 키와 속성들을 담고 있는 참조 타입의 객체
- 순서 보장
- 주로 대괄호 이용하여 생성, 0을 포함한 양의 정수 인덱스로 특정 값 접근 가능
- array.length 형태로 배열 길이 접근 가능

### reverse

- array.reverse()
  - 원본 배열의 요소들의 순서를 반대로 정렬

### push & pop

- array.push()
  - 배열의 가장 뒤에 요소 추가
- array.pop()
  - 배열의 마지막 요소 제거

### unshift & shift

- array.unshift()
  - 배열의 가장 앞에 요소 추가
- array.shift()
  - 배열의 첫번째 요소 제거

### includes

- array.includes(value)
  - 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

### indexOf

- array.indexOf(value)
  - 배열에 특정 값이 존재하는지 확인 후 가장 첫번째로 찾은 요소의 인덱스 반환
  - 만약 해당 값이 없을 경우 -1 반환

### join

- array.join([separator])
  - 배열의 모든 요소를 연결하여 반환
  - 구분자는 선택적으로 지정 가능하며, 생략 시 쉼표 기본 값으로 사용

### Spread operator

- (...)을 사용하면 배열 내부에서 배열 전개 가능
- 얕은 복사에 활용 가능

### forEach

- array.forEach(callback(element[,index[,array]]))
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 반환 값이 없는 메서드

### map

- array.map(callback(element[,index[,array]]))
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
  - 기존 배열 전체를 다른 형태로 바꿀 때 유용

### filter

- array.filter(callback(element[,index[,array]]))
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
  - 기본 배열의 요소들을 필터링 할 때 유용

### reduce

- array.reduce[callback(acc,element[index[,array]]](, initialValue))
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환
  - reduce 메서드의 주요 매개변수
    - acc
      - 이전 callback 함수의 반환 값이 누적되는 변수
    - initialValue(optional)
      - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값

### find

- array.find(callback(element[,index[,array]]))
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
  - 찾는 값이 배열에 없으면 undefined 반환

### some

- array.some(callback(element[, index[, array]]))
  - 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
  - 모든 요소가 통과하지 못한 거짓 반환

### every

- array.every(callback(element[, index[, array]]))
  - 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
  - 하나의 요소라도 통과하지 못하면 거짓 반환

## 객체

### 정의와 특징

- 객체는 속성의 집합이며 중괄호 내부에 key, value의 쌍으로 표현
- key는 문자열 타입만 가능
- value는 모든 타입(함수 포함) 가능
- 객체 요소 접근은 점 또는 대괄호로 가능
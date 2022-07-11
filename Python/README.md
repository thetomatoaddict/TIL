# 👻Python🧠

## 목차

- 기초문법
- 자료형
- 컨테이너



### 기초문법

- 코드 스타일 가이드

  > 코드를 '어떻게 작성할지'에 대한 가이드라인

  • 파이썬에서 제안하는 스타일 가이드

     PEP8 (https://www.python.org/dev/peps/pep-0008/ )

  • 기업, 오픈소스 등에서 사용되는 스타일 가이드

     Google Style guide (https://google.github.io/styleguide/pyguide.html) 등

- Space Sensitive

  • 문장을 구분할 때, 들여쓰기 (indentation)>를 사용 

  • 들여쓰기를 할 때는 4칸(space키 4번) 혹은 1탭(Tab키 1번)을 입력 

  • 주의! 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용 → 혼용하면 안됨 

  • Tab으로 들여쓰면 계속 탭으로 들여써야 함 

  • 원칙적으로는 공백 (빈칸, space) 사용을 권장* PEP8 권장사항

- 변수

  • 변수는 할당 연산자(=)를 통해 값을 할당(assignment) 

  • type()

     변수에 할당된 값의 타입 

  • id()

     변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리주소

- 식별자

  파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name) 

  • 규칙

     • 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성

     • 첫 글자에 숫자가 올 수 없음

     • 길이제한이 없고, 대소문자를 구별

     • 다음의 키워드(keywords)는 예약어(reserved words)로 사용할 수 없음

  > False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

- 주석

  • 코드에 대한 설명

     • 중요한 점이나 다시 확인하여야 하는 부분을 표시

     • 컴퓨터는 주석을 인식하지 않음 사용자만을 위한 것

  • 가장 중요한 습관

  ​    • 개발자에게 주석을 작성하는 습관은 매우 중요

  ​    • 쉬운 이해와 코드의 분석 및 수정이 용이

  ​          ✓ 주석은 코드 실행에 영향을 미치지 않을 뿐만 아니라

  ​          ✓ 프로그램의 속도를 느리게 하지 않으며, 용량을 늘리지 않음



### 자료형

- Boolean Type
  - True or False
  - 0, 0.0, (), [], {}, '', None = 모두 False
  - 논리연산자(and, or, not) 사용하여 검증
  -  bool() 함수로 True인지 False인지 검증
- Numeric Type
  - int
  - float
  - complex(복소수)
  - 산술연산자(+,-,*,%,/,//,**)에 =을 붙여 복합연산자로 사용
  - 비교연산자(<,<=,==,!=..)를 이용해 true나 false 리턴
- String Type
  - 삼중따옴표(''')를 사용하면 모든 내용을 그대로 출력한다.
  - 리스트처럼 인덱싱, 슬라이싱 가능
  - 결합(+), 반복(*****n), 포함('a' **in** 'apple' =>true or false 리턴) 사용
  - %s, %d, %f 사용하여 변수 활용
- Typecasting(자료형 변환)
  - 파이썬에서 데이터 형태는 서로 변환할 수 있음



### 컨테이너

- 시퀀스 (ordered)
  - 문자열 : 문자들의 나열
  - 레인지 : 숫자의 나열, range(n, m s) 로 수열 생성 가능
  - 리스트 : 변경 가능한 값들의 나열, []
  - 튜플 : 변경 불가능한 값들의 나열, ()
  - 시퀀스형 연산자 : len() min() max() 등
- 비시퀀스 (unordered)
  - 세트 : 값들의 집합 (중복값 없음, 순서 없음)
  - 딕셔너리 : 키-값들의 집합


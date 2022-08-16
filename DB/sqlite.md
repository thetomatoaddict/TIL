## SQLite

- **서버 형태가 아닌 파일 형식**으로 응용 프로그램에 넣어서 사용하는 **비교적 가벼운 데이터베이스**
- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 사용됨
- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능



#### **SQLite 데이터 타입**

| 타입    | 설명                                                        |
| ------- | ----------------------------------------------------------- |
| INTEGER | 정수                                                        |
| TEXT    | 문자열                                                      |
| BLOB    | 이진 데이터 (대용량의 바이너리 데이터를 저장하기 위한 타입) |
| REAL    | 실수                                                        |
| NUMERIC | 정수 또는 실수                                              |



------

## **SQL**

> 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어

- **스키마 생성 및 수정**
- **자료의 검색 및 관리**
- **데이터베이스 객체 접근 조정 관리**



| 분류                                                         | 개념                                                      |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| **DDL** (Data **Definition** Language) - **데이터 정의 언어** | 관계형 데이터베이스 `구조를 정의` 하기 위한 명령어        |
| **DML** (Data **Maripulation** Language) - **데이터 조작 언어** | `데이터를 저장, 조회, 수정, 삭제` 들을 하기 위한 명령어   |
| **DCL** (Data **Control** Language) - **데이터 제어 언어**   | 데이터베이스 `사용자의 권한 제어` 를 위해 사용하는 명령어 |



### **필드 제약 조건** 

- `NOT NULL` : null 값 입력 금지
- `UNIQUE` : 중복 값 입력 금지
- `PRIMARY KEY` : 유일한 값
- `FOREIGN KEY` : 외래키
- `CHECK` : 조건으로 설정된 값만 입력 허용
- `DEFAULT` : 기본 설정 값



```sqlite
-- classmates라는 이름의 테이블 생성
CREATE TABLE classmates(
	id INTEGER PRIMARY KEY,
  name TEXT
);


-- 테이블 목록 조회
.tables


-- 특정 테이블 스키마 조회
.schema classmates


-- 값 추가
INSERT INTO calssmates VALUES (1, '조세호');


-- 테이블 조회
SELECT * FROM classmates;


-- 테이블 삭제
DROP TABLE classmates;


-- 해석
-- students라는 테이블을 생성할건데,
-- id는 정수고 유일한 값이야.
-- name은 문자이고 비어있어서는 안돼.
-- age는 정수고 기본값은 1이면서, 0보다는 큰지 확인해줘.
CREATE TABLE students(
	id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER DEFAULT 1 CHECK (0 < age)
)
```



------

## **CREATE** 



### **INSERT** 

> Insert a single row into a table

- 테이블에 단일 `행 삽입`
- 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력

```sqlite
-- CREATE


-- Parse error: table classmates has 3 column but 2 values were supplied -> 테이블에 열이 3개인데 2개만 넣었어. 어디에 넣을려고 하는거야?
INSERT INTO classmates VALUES ('홍길동', 23); 


-- 테이블에 데이터를 삽입하고 조회하기
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;


INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES ('김철수', 23, '서울');


-- 한번에 삽입하고 싶다면
INSERT INTO classmates VALUES
	('홍길동', 30, '서울'),
  ('김철수', 30, '제주'),
  ('이호영', 26, '인천'),
  ('박민희', 29, '대구'),
  ('최혜영', 28, '전주');
```



------

## **READ** 



### **SELECT** 

> Query data from a table

- 테이블에서 `데이터를 조회`

  - SELECT 문은 SQLite에서 가장 기본이 되는 문이며, 다양한 절(clause)과 함께 사용

    ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY ...

```sqlite
SELECT 컬럼1, 컬럼2, ... FROM 테이블명;
```



### **LIMIT** 

> 'constrain the number of rows retrurned by a qeury'

- 퀴리에서 `반환되는 행 수를 제한`
- 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함
  - `OFFSET` : 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형

```sqlite
SELECT 컬럼1, 컬럼2, ... FROM 테이블명 LIMIT 숫자;

SELECT 컬럼1, 컬럼2, ... FROM 테이블명 LIMIT 숫자 OFFSET 숫자;
```



### **WHERE** 

> 'specify the search condition for rows returned by the query'

- 쿼리에서 반환된 행에 대한 `특정 검색 조건` 을 지정

```sqlite
SELECT 컬럼1, 컬럼2, ... FROM 테이블명 WHERE 조건;
```



### **SELECT DISTINCT** 

> 'remove duplicate rows in the result set'

- 조회 결과에서 `중복 행을 제거`
- DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

```sqlite
SELECT DISTINCT 컬럼 FROM 테이블명;
```







## 실습

### CREATE, DROP

- 데이터베이스 생성하기

  ```sqlite
  $ sqlite3 tutorial.sqlite3
  sqlite> .database
  ```

- csv 파일을 table로 만들기

  ```sqlite
  sqlite> .mode csv
  sqlite> .import hellodb.csv examples
  sqlite> .tables
  examples
  sqlite> SELECT * FROM examples;
  1,"길동","홍",600,"충청도",010-0000-0000
  ```

- `CREATE TABLE`

  - 데이터베이스에서 테이블 생성

  ```sqlite
  CREATE TABLE classmates (
      id INTEGER PRIMARY KEY,
      name TEXT
  );
  ```

  ```sqlite
  sqlite> CREATE TABLE classmates (
     ...> id INTEGER PRIMARY KEY,
     ...> name TEXT
     ...> );
  sqlite> .tables
  classmates examples
  ```

- 특정 테이블의 schema 조회

  ```sqlite
  sqlite> .schema classmates
  CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
  );
  ```

- `DROP TABLE`

  - 데이터베이스에서 테이블 제거

  ```sqlite
  sqlite> DROP TABLE classmates;
  sqlite> .tables
  examples
  ```

- 필드 제약 조건

  - NOT NULL : NULL 값 입력 금지
  - UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 입력 가능)
  - PRIMARY KEY : 테이블에서 반드시 하나. NOT NULL + UNIQUE
  - FOREIGN KEY : 외래키. 다른 테이블의 Key
  - CHECK : 조건으로 설정된 값만 입력 허용
  - DEFAULT : 기본 설정 값

### INSERT

- 테이블에 단일 행 삽입

  ```sqlite
  INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
  ```

- 테이블에 정의된 모든 열에 맞춰 순서대로 입력

  ```sqlite
  INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);
  ```

- `rowid` : SQLite에서 PRIMARY KEY가 없는 경우 자동으로 증가하는 PRIMARY KEY 열

  ```sqlite
  sqlite> SELECT rowid, * FROM classmates;
  rowid       name        age         address
  ----------  ----------  ----------  ----------
  1           홍길동       23
  2           홍길동       30          서울
  ```

  - 만약 스키마에 id 기본키를 직접 작성할 경우, 입력할 column들을 명시하지 않으면 자동으로 입력되지 않음

    ```sqlite
    INSERT INTO classmates VALUES (1, '홍길동', 30, '서울'); 
    # id를 포함한 모든 value를 작성
    
    INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울'); 
    # 각 value에 맞는 column들을 명시적으로 작성
    ```

- 여러 값 한번에 넣기

  ```sqlite
  INSERT INTO classmates VALUES
  ('홍길동', 30, '서울'), 
  ('김철수', 30, '제주'),
  ('이호영', 26, '인천'),
  ('박민희', 29, '대구'),
  ('최혜영', 28, '전주');
  ```

### SELECT

```sqlite
SELECT col1, col2, ... FROM table_name;
SELECT * FROM table_name;
```

- 테이블에서 데이터를 조회

- 가장 기본이 되는 문이며 다양한 절과 함께 사용

  - `ORDER BY`, `DISTINCT`, `WHERE`, `LIMIT`, `GROUP BY` …

  - `LIMIT`

    - 쿼리에서 반환되는 행 수를 제한
    - 특정 행부터 시작해서 조회하기 위해 `OFFSET` 키워드와 함께 사용하기도 함

  - `OFFSET`

    - 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형

    - 0부터 시작함

      ```sqlite
      SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5;
      # 6번째 행 부터 10개 행을 조회 (6번째 행부터 10개를 출력)
      ```

  - `WHERE`

    - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정

  - `SELECT DISTINCT`

    - 조회 결과에서 중복 행을 제거
    - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

  - `ORDER BY`

    - 쿼리에서 반환되는 행을 특정 열을 기준으로 오름차순 혹은 내림차순 정렬

  - `GROUP BY`

    - 특정 열에 대해 같은 값을 가진 행끼리 묶어서 그룹화
    - 그룹화한 결과에 조건 처리를 하기 위해선 `HAVING` 절을 사용해야 함
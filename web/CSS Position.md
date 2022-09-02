# CSS Position

- 브라우저마다 설정값이 다르게 나타날 수 있어서 Reboot CSS를 통해 변수를 없앤다 [Reboot CSS (github.com)](https://gist.github.com/marharyta/b83a3683085eb42867bbcefb34687af8)
- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  1. relative : 상대 위치
     - 자기 자신의 static 위치를 기준으로 이동(*normal flow유지*)
     - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음(normal position 대비 offset)
     - (**요소를 일반적인 문서의 흐름에 따라 배치합니다 요소 자기 자신인 정위치 static 일때 기준으로 배치됨**)
       [![스샷](https://github.com/kleenex1/TIL/raw/master/WEB/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-08-31%20122432.png)](https://github.com/kleenex1/TIL/blob/master/WEB/스크린샷/화면 캡처 2022-08-31 122432.png)
  2. absolute : 절대 위치
     - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지 하지 않음(*normal flow에서 벗어남*) (**가장 가까운 위치에 있는 부모(조상)요소를 기준으로 배치됨)
       [![스샷](https://github.com/kleenex1/TIL/raw/master/WEB/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-08-31%20122453.png)](https://github.com/kleenex1/TIL/blob/master/WEB/스크린샷/화면 캡처 2022-08-31 122453.png)
  3. fixed : 고정 위치
     - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지 하지 않음(*normal flow에서 벗어남*)
     - 부모 요소와 관계 없이 viewport 기준으로 이동(스크롤 시에도 항상 같은 곳에 위치함)
  4. sticky : 스크롤에 따라 static → fixed로 변경
     - 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

# Float 예시

[![스샷](https://github.com/kleenex1/TIL/raw/master/WEB/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-08-31%20122504.png)](https://github.com/kleenex1/TIL/blob/master/WEB/스크린샷/화면 캡처 2022-08-31 122504.png)

# Flexbox

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
  - main axis (메인 축)
  - cross axis (교차 축)
- 구성 요소
  - Flex Container (부모 요소)
    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    - Flex Item들이 놓여있는 영역
    - display 속성을 flex 혹은 inline-flex로 지정
  - Flex Item (자식 요소)
    - 컨테이너에 속해 있는 컨텐츠(박스)
- 왜 Flexbox를 써야할까? 기존에 Normal Flow를 벗어나는 수단은 Float 혹은 Position밖에 없었는데 (수동 값 부여 없이) 1. 수직 정렬 2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치 하기 어려웠다.

```
.flex-container {
  display: flex; /*부모 요소에 flex 혹은 inline-flex */
}
```

# Flex 속성

- Flex 속성은 display 속성에 flex로 설정한 부모 요소여야 한다.
- Flex 컨테이너의 직속 자식 요소들은 자동적으로 flex 개별 아이템이 된다.
- 배치 설정
  - flex-direction
    - row
      [![스샷](https://github.com/kleenex1/TIL/raw/master/WEB/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-08-31%20122513.png)](https://github.com/kleenex1/TIL/blob/master/WEB/스크린샷/화면 캡처 2022-08-31 122513.png)
    - row-reverse
      [![스샷](https://github.com/kleenex1/TIL/raw/master/WEB/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-08-31%20122524.png)](https://github.com/kleenex1/TIL/blob/master/WEB/스크린샷/화면 캡처 2022-08-31 122524.png)
    - column
      [![스샷](https://github.com/kleenex1/TIL/raw/master/WEB/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-08-31%20122534.png)](https://github.com/kleenex1/TIL/blob/master/WEB/스크린샷/화면 캡처 2022-08-31 122534.png)
    - column-reverse
      [![스샷](https://github.com/kleenex1/TIL/raw/master/WEB/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-08-31%20122544.png)](https://github.com/kleenex1/TIL/blob/master/WEB/스크린샷/화면 캡처 2022-08-31 122544.png)
  - flex-wrap
    - wrap
      [![스샷](https://github.com/kleenex1/TIL/raw/master/WEB/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-08-31%20122552.png)](https://github.com/kleenex1/TIL/blob/master/WEB/스크린샷/화면 캡처 2022-08-31 122552.png)
  - nowrap: 기본값
    [![스샷](https://github.com/kleenex1/TIL/raw/master/WEB/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-08-31%20122600.png)](https://github.com/kleenex1/TIL/blob/master/WEB/스크린샷/화면 캡처 2022-08-31 122600.png)
- 공간 나누기
  - justify-content (main axis)
    - flex-start / flex-end / center / space-between / space-arount / space-evenly 예) space-between
      [![스샷](https://github.com/kleenex1/TIL/raw/master/WEB/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-08-31%20122609.png)](https://github.com/kleenex1/TIL/blob/master/WEB/스크린샷/화면 캡처 2022-08-31 122609.png)
  - align-content (cross axis) - 수업시간에 다루지않음
- 정렬
  - align-items (모든 아이템을 cross axis 기준으로)
  - align-self (개별 아이템)
- 기타 속성
  - flex-grow : 남은 영역을 아이템에 분배
  - order : 배치 순서
- 활용 레이아웃 - 카드 배치

```
#layout_03 {
  display : flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-around;
  align-content: space-around;
}
```

# Position : static ; fixed; sticky;

- static
  - 기본적으로 HTML 요소들은 정적으로 배치된다. 정적인 요소란 말은 top, bottom, right, left 속성의 영향을 받지 않는다. 그러나 포지션 속성을 부여하고 속성 값을 부여한 후 top, bottom, right, left 속성과 속성값을 부여하면 작동한다.
- fixed
  - 화면의 특정 위치에 고정되어 스크롤해도 계속 그 자리에 머문다.
- sticky
  - 스크롤되는 가장 가까운 상위 요소에 대해 오프셋이 적용된다. 요소가 컨테이너보다 커서 스크롤이 생겨날때 자기 상위 요소에 달라붙는다. 상위 요소 혹은 하위 요소에 가면 딱 붙는다.
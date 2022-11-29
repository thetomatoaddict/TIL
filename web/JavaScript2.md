# JS



# JavaScript

## 필요성

- 브라우저 화면을 ‘동적’으로 만들기 위함
- 브라우저를 조작할 수 있는 유일한 언어

## DOM (Document Object Model)

### DOM이란?

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델 주요 객체 Window: DOM을 표현하는 창. 가장 최상위 객체 Document: 페이지 컨텐츠의 Entry Point을 역할을 하며 body 등 수 많은 다른 요소 포함 navigator, location, history, screen

### BOM(Browser Object Model)이란?

- 자바스크립트가 브라우저랑 소통하기 위한 모델
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단

### DOM 조작

- DOM 조작 순서
  - 선택
  - 변경

### DOM 선택

- document.querySelector(selector)
  - 제공한 선택자와 일치하는 element 하나 선택
  - 제공한 CSS selector를 만족하는 첫 번째 element 객체 반환 (없다면 null)
- document.querySelectorAll(selector)
  - 제공한 선택자와 일치하는 여러 element를 선택
  - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  - 지정된 셀렉터에 일치하는 NodeList를 반환
- getElementById(id) - getElementsByTagName(name) - getElementsByClassName(names)

### DOM 변경

- document.createElement()
  - 작성한 태그 명의 HTML 요소를 생성하여 반환
- Element.append()
  - 특정 부모 Node 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString 삽입
  - 여러개의 Node 객체, DOMString을 추가할 수 있음
  - 반환 값이 없음
- Node.appendChild()
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능)
  - 한번에 오직 하나의 Node만 추가할 수 있음
  - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동
- Node.innerText
- Element.innerHTML

### DOM 삭제

- ChildNode.remove()
- Node.removeChild()

### DOM 속성

- Element.setAttribute(name, value)
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성 추가
- Element.getAttribute(attributeName)
  - 해당 요소의 지정된 값(문자열)을 반환
  - 인자는 값을 얻고자 하는 속성의 이름
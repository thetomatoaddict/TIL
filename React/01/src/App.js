import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

//props 이용한 동적인 UI
//1. 스위치처럼 사용할 스테이트 만들기
//2. 값이 변경되는 곳, 그 결과가 출력될 곳에 코드 작성

function App() {

  let [글제목,글제목변경] = useState(['상태 변경 및 관리하기', '반복문 대신 매핑하기', '리액트 독학'])
  let [따봉, 따봉변경] = useState([0,0,0])
  let [모달, 모달변경] = useState(false)
  let [title, settitle] = useState(0)
  let [입력값, 입력값변경] = useState('')

  //이벤트 버블링 막으려면 (e)=>{e.stopPropagation();}

  return (
    <div>
      <div className='black-nav'>
        <h4>React Blog</h4></div>

    {
      글제목.map(function(a,i){
        return(
        <div className='list' key={i}>
          <h4 onClick={()=>{모달변경(true); settitle(i)}}>{a}
          <span onClick={(e)=>{
            e.stopPropagation();
            let copy = [...따봉]
            copy[i] ++
            따봉변경(copy)
          }}>👍</span>
          <span>{따봉[i]}</span>
          <button onClick={(ee)=>{
            ee.stopPropagation();
            let copy = [...글제목]
            copy.splice(i, 1)
            글제목변경(copy)
          }}>삭제</button>
          </h4>
          <p>{getTodayDate()} 발행</p>          
        </div>
      )})
    }

    <input onChange={(e)=>{입력값변경(e.target.value)}}>
    </input>
    <button onClick={()=>{
      let copy = [...글제목]
      copy.unshift(입력값)
      글제목변경(copy)
      let copy2 = [...따봉]
      copy2.unshift(0)
      따봉변경(copy2)
    }}>submit</button>

    {
      모달 === true ? <Modal 글제목={글제목} i={title}/> : null
    }     

    </div>
  );
}

function Modal(props){
  return(
    <div className='modal'>
      <h4>{props.글제목[props.i]}</h4>
      <p>{getTodayDate()} 발행</p>
      <p>내용</p>
    </div>
  )
}


function getTodayDate() {
  const today = new Date(); // Mon Dec 20 2021 22:04:03 GMT+0900 (한국 표준시)

  const year = today.getFullYear(); // 2021
  const month = ('0' + (today.getMonth() + 1)).slice(-2); // 12
  const day = ('0' + today.getDate()).slice(-2); // 20

  // 원하는 문자열 형태로 날짜 가공하기
  // const dateString = year + month + day; // 20211220
  const dateString = year + '-' + month + '-' + day; // 2021.12.20

  return dateString;
}

export default App;
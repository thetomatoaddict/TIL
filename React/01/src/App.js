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


  return (
    <div>
      <div className='black-nav'>
        <h4>React Blog</h4></div>

    {
      글제목.map(function(a,i){
        return(
        <div className='list' key={i}>
          <h4 onClick={()=>{모달변경(true); settitle(i)}}>{a}
          <span onClick={()=>{
            let copy = [...따봉]
            copy[i] ++
            따봉변경(copy)
          }}>👍</span>
          <span>{따봉[i]}</span>
          </h4>
          <p>2022-12-13 발행</p>          
        </div>
      )})
    }

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
      <p>날짜</p>
      <p>내용</p>
    </div>
  )
}

export default App;
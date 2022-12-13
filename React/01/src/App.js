import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {

  let [글제목,글제목변경] = useState(['상태 변경 및 관리하기', '반복문 대신 매핑하기', '리액트 독학'])
  let [따봉, 따봉변경] = useState([0,0,0])
  let [모달, 모달변경] = useState(false)


  return (
    <div>
      <div className='black-nav'>
      <h4>Blog for React</h4>
      </div>

      {
        글제목.map(function(a, i){
          return(
          <div className='list' key={i}>

            <h4 onClick={()=>{모달 === false ? 모달변경(true) : 모달변경(false)}}>
              {a}
              <span onClick={()=>{
                let copy = [...따봉]
                copy[i] ++
                따봉변경(copy)
              }}>
                👍
              </span>
              <span>
                {따봉[i]}
              </span>
            </h4>

            <p>2022-12-09 발행</p>


          </div>
          )


        })
        
      }
      
      {
        모달 === true ? <Modal></Modal> : null
      }


    </div>
  );
}


function Modal(){
  return(
  <div className='modal'>
    <h4>제목</h4>
    <p>내용</p>
  </div>
  )
}
export default App;
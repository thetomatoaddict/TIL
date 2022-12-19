import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Container, Nav, Navbar, NavDropdown, Row, Col, Card } from 'react-bootstrap';
import data from './data.js'
import { useState } from 'react';
import { Routes, Route, Link } from 'react-router-dom'
import Detail from './Detail';


function App() {
  let [shoes] = useState(data)
  return (
    <div>


      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/">Home</Nav.Link>
              <Nav.Link href="#link">Link</Nav.Link>
              <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">
                  Another action
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">
                  Separated link
                </NavDropdown.Item>
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>



      <Routes>
        <Route path="/" element={<>
          <div className='main-bg'></div>
          <Container className='p-3 d-flex justify-content-center'>
            <Row className='p-3 d-flex justify-content-center'>

              {
                shoes.map(function (a, i) {
                  return (
                    <Ccard a={a} i={i}></Ccard>

                  )
                })
              }

            </Row>
          </Container>
        </>} />
        <Route path="/detail" element={<Detail />} />
      </Routes>









    </div>
  );
}

function Ccard(props) {
  return (
    <Col className='p-3 d-flex justify-content-center'>
      <Card style={{ width: '18rem' }}>
        <Card.Img variant="top" src={'https://codingapple1.github.io/shop/shoes' + (props.i + 1) + '.jpg'} />
        <Card.Body>
          <Card.Title>{props.a.title}</Card.Title>
          <Card.Text>
            {props.a.content}
          </Card.Text>
          <Card.Text>
            {props.a.price}
          </Card.Text>
          <Button variant="primary">Go somewhere</Button>
        </Card.Body>
      </Card>
    </Col>
  )
}




export default App;

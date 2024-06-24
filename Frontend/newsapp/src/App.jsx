import Signin from './components/Signin'
import './App.css'
import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Main from './components/Main.jsx'
import Navbar from './components/Navbar.jsx'
function App() {
  return (
    <>
       <Routes>
        <Route path="/signin" element={<Signin/>}/>
        <Route path="/" element={<Main/>}/>
       </Routes>
    </>
  )
}

export default App

import React from "react";
import Signin from "../components/Signin.jsx";
import Navbar from "../components/Navbar.jsx";
import Home from "./Home.jsx";
function Main() {
  return (
    <>
    <div className="grid grid-row-2">
    <Navbar />
    <Home/>

    </div>
      
    </>
  );
}

export default Main;

import React from "react";
import front from "../images/front.png";
function Signin() {
  return (
    <div className="grid grid-cols-2 bg-black h-screen">
      <div className="text-center">
        <h1 className="text-white text-3xl mt-52">Sign In</h1>
        <button class="bg-green-500 hover:bg-green-800 text-white font-bold py-2 px-4 rounded h-12 w-96 ">
          Sign In
        </button>
      </div>
      <div>
        <img src={front} className="h-screen" />
      </div>
    </div>
  );
}

export default Signin;

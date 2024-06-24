import React, { useState } from "react";
import search from "../images/search.png";
import { Link } from "react-router-dom";

// Array of country names
const countries = [
  "United States",
  "United Kingdom",
  "Canada",
  "Australia",
  "Germany",
  "France",
  "Japan",
  "China",
  "India",
  "Brazil",
  // Add more countries as needed
];

function Navbar() {
  const [showDropdown, setShowDropdown] = useState(false);

  const toggleDropdown = () => {
    setShowDropdown(!showDropdown);
  };

  // Function to handle scrolling to the desired country section
  const scrollToCountrySection = (country) => {
    // Assuming you have a section with id corresponding to each country
    const countrySection = document.getElementById(country.toLowerCase().replace(/\s+/g, '-'));
    if (countrySection) {
      countrySection.scrollIntoView({ behavior: "smooth" });
    }
    setShowDropdown(false); // Hide the dropdown after scrolling
  };

  return (
    <div className="grid grid-cols-3 bg-black text-white py-3">
      {/* Left Section */}
      <div className="flex items-center">
        {/* LOGO element */}
        <div className="mr-4 p-2 rounded-xl">
          LOGO
        </div>
        {/* Sign In button */}
        <Link to="/signin">
        <button className="nav-button mr-4 hover:bg-white hover:text-black p-2 rounded-xl">
          Sign In
        </button>
        </Link>
        
      </div>

      {/* Center Section */}
      <div className="flex items-center justify-center space-x-8">
        {/* Top News button */}
        <button className="nav-button hover:bg-white hover:text-black p-2 rounded-xl">
          Top News
        </button>
        {/* Country button */}
        <div className="relative">
          <button
            className="nav-button hover:bg-white hover:text-black p-2 rounded-xl"
            onClick={toggleDropdown}
          >
            Country
          </button>
          {/* Dropdown menu */}
          {showDropdown && (
            <div className="absolute m-5 mt-3 p-4 bg-black text-white shadow-lg rounded-lg border-2">
              <ul>
                {countries.map((country, index) => (
                  <li
                    key={index}
                    className="cursor-pointer p-3 hover:bg-gray-800 hover:text-white"
                    onClick={() => scrollToCountrySection(country)}
                  >
                    {country}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
        {/* Sports button */}
        <button className="nav-button hover:bg-white hover:text-black p-2 rounded-xl">
          Sports
        </button>
      </div>

      {/* Right Section */}
      <div className="flex items-center justify-end">
        {/* Search News button */}
        <button className="nav-button flex items-center hover:bg-white hover:text-black p-2 rounded-xl">
          <img src={search} className="h-5 pr-2" alt="Search Icon" />
          Search News
        </button>
      </div>
    </div>
  );
}

export default Navbar;

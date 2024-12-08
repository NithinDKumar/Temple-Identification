import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';
import logo from './logo.png';

const Header = ({ isLoggedIn, handleLogout }) => {
  return (
    <header className="header">
      <img src={logo} alt="Logo" className="logo" />
      <nav className="nav">
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/temples">Temples</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      {isLoggedIn ? (
        <button onClick={handleLogout} className="login-button">Logout</button>
      ) : (
        <Link to="/login" className="login-button">Login</Link>
      )}
    </header>
  );
};

export default Header;

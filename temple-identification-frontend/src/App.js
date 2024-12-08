import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './components/HomePage';
import AboutPage from './components/AboutPage';
import TemplesPage from './components/TemplesPage';
import ContactPage from './components/ContactPage';
import LoginPage from './components/LoginPage';
import './App.css';

const App = () => {
  return (
    <Router>
      <div className="App">
        <nav>
          <a href="/">Home</a>
          <a href="/about">About</a>
          <a href="/temples">Temples</a>
          <a href="/contact">Contact</a>
          <a href="/login">Login</a>
        </nav>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/temples" element={<TemplesPage />} />
          <Route path="/contact" element={<ContactPage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;

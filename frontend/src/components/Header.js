// src/components/Header.js
import React from 'react';
import 'bulma/css/bulma.min.css';

const Header = () => {
  return (
    <nav className="navbar is-primary">
      <div className="navbar-brand">
        <a className="navbar-item" href="/">
          QGIS Plugins Website
        </a>
      </div>
    </nav>
  );
}

export default Header;

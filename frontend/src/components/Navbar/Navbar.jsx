import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { FiSearch, FiShoppingCart, FiUser, FiMenu, FiX } from 'react-icons/fi';
import './Navbar.css';

const Navbar = () => {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <nav className="navbar">
      <div className="container navbar-container">
        {/* Mobile Menu Toggle */}
        <button className="mobile-menu-btn" onClick={toggleMobileMenu}>
          {isMobileMenuOpen ? <FiX size={24} /> : <FiMenu size={24} />}
        </button>

        {/* Logo */}
        <Link to="/" className="navbar-logo">
          PHNTM<span className="logo-dot">.</span>
        </Link>

        {/* Desktop Links */}
        <ul className={`navbar-links ${isMobileMenuOpen ? 'mobile-open' : ''}`}>
          <li><Link to="/shop" onClick={() => setIsMobileMenuOpen(false)}>Shop</Link></li>
          <li><Link to="/shop?category=new" onClick={() => setIsMobileMenuOpen(false)}>New Arrivals</Link></li>
          <li><Link to="/shop?category=trending" onClick={() => setIsMobileMenuOpen(false)}>Trending</Link></li>
          <li><Link to="/shop?collection=streetwear" onClick={() => setIsMobileMenuOpen(false)}>Streetwear</Link></li>
        </ul>

        {/* Action Icons */}
        <div className="navbar-actions">
          <button className="icon-btn" aria-label="Search">
            <FiSearch size={20} />
          </button>
          <Link to="/profile" className="icon-btn" aria-label="Profile">
            <FiUser size={20} />
          </Link>
          <Link to="/cart" className="icon-btn cart-btn" aria-label="Cart">
            <FiShoppingCart size={20} />
            <span className="cart-badge">0</span>
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;

import React from 'react';
import { Link } from 'react-router-dom';
import MainLayout from '../../layouts/MainLayout';
import ProductCard from '../../components/ProductCard/ProductCard';
import Button from '../../components/Button/Button';
import './Home.css';

// Mock Data for Phase 1
const featuredProducts = [
  { id: 1, name: 'Deep Sea Oversized Tee', price: 1299, stock: 15, images: [{ image_url: '/assets/placeholders/product-placeholder.png' }] },
  { id: 2, name: 'Midnight Cargo Pants', price: 2499, stock: 5, images: [{ image_url: '/assets/placeholders/product-placeholder.png' }] },
  { id: 3, name: 'Soft Blue Essential Hoodie', price: 1899, stock: 0, images: [{ image_url: '/assets/placeholders/product-placeholder.png' }] },
  { id: 4, name: 'Steel Blue Classic Jacket', price: 3499, stock: 20, images: [{ image_url: '/assets/placeholders/product-placeholder.png' }] },
];

const Home = () => {
  return (
    <MainLayout>
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-overlay"></div>
        <div className="container hero-content">
          <h1>Redefine Your Style.</h1>
          <p>Premium oversized streetwear crafted for comfort and built for the streets.</p>
          <div className="hero-actions">
            <Link to="/shop">
              <Button size="lg" variant="primary">Shop Now</Button>
            </Link>
            <Link to="/shop?category=new">
              <Button size="lg" variant="secondary">New Arrivals</Button>
            </Link>
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="section container">
        <div className="section-header">
          <h2>Trending Now</h2>
          <Link to="/shop" className="view-all-link">View All</Link>
        </div>
        
        <div className="product-grid">
          {featuredProducts.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      </section>

      {/* Category Highlights */}
      <section className="section bg-light">
        <div className="container">
          <div className="category-grid">
            <div className="category-card dark">
              <div className="category-card-content">
                <h3>Oversized Fits</h3>
                <Link to="/shop?category=oversized"><Button variant="outline">Explore</Button></Link>
              </div>
            </div>
            <div className="category-card light">
              <div className="category-card-content">
                <h3>Bottom Wear</h3>
                <Link to="/shop?category=bottoms"><Button variant="outline">Explore</Button></Link>
              </div>
            </div>
          </div>
        </div>
      </section>
    </MainLayout>
  );
};

export default Home;

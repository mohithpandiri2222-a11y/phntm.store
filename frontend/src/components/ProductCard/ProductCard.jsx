import React from 'react';
import { Link } from 'react-router-dom';
import './ProductCard.css';
import Button from '../Button/Button';

const ProductCard = ({ product }) => {
  // Use placeholder image if none provided
  const imageUrl = product?.images?.[0]?.image_url || '/assets/placeholders/product-placeholder.png';
  
  // Format price
  const formattedPrice = new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0
  }).format(product?.price || 0);

  return (
    <div className="product-card">
      <Link to={`/product/${product?.id}`} target="_blank" rel="noopener noreferrer" className="product-card-img-wrapper">
        <img src={imageUrl} alt={product?.name} className="product-card-img" />
        {product?.stock <= 5 && product?.stock > 0 && (
          <span className="product-badge badge-warning">Few Left</span>
        )}
        {product?.stock === 0 && (
          <span className="product-badge badge-error">Sold Out</span>
        )}
      </Link>
      
      <div className="product-card-content">
        <Link to={`/product/${product?.id}`} target="_blank" rel="noopener noreferrer" className="product-title">
          {product?.name || 'Unknown Product'}
        </Link>
        <div className="product-price">{formattedPrice}</div>
        
        <div className="product-card-actions">
          <Button variant="outline" fullWidth disabled={product?.stock === 0}>
            {product?.stock === 0 ? 'Sold Out' : 'Add to Cart'}
          </Button>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;

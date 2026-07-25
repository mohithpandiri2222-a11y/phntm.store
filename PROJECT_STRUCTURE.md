# `e-com` Project Structure

```text
e-com/
│
├── frontend/                  # React + Vite Frontend
│   ├── public/
│   │   ├── images/
│   │   ├── videos/
│   │   └── favicon.ico
│   │
│   ├── src/
│   │   ├── assets/
│   │   │   ├── fonts/
│   │   │   ├── icons/
│   │   │   ├── images/
│   │   │   └── logo/
│   │   │
│   │   ├── components/        # Reusable UI components
│   │   │   ├── Badge/         # (Contains Badge.jsx, Badge.css)
│   │   │   ├── Button/        # (Contains Button.jsx, Button.css)
│   │   │   ├── CartItem/      
│   │   │   ├── CategoryCard/  
│   │   │   ├── Footer/        
│   │   │   ├── Hero/          
│   │   │   ├── Input/         
│   │   │   ├── Loader/        
│   │   │   ├── Modal/         
│   │   │   ├── Navbar/        
│   │   │   ├── ProductCard/   
│   │   │   ├── QuantitySelector/
│   │   │   ├── Rating/        
│   │   │   └── SearchBar/     
│   │   │
│   │   ├── config/            # Axios config, environment settings
│   │   ├── constants/         # routes.js, colors.js, messages.js
│   │   ├── context/           # AuthContext.jsx, CartContext.jsx, ThemeContext.jsx
│   │   ├── data/              # products.js, categories.js (fake data)
│   │   ├── hooks/             # useAuth.js, useCart.js, useProducts.js
│   │   ├── layouts/           # MainLayout.jsx, AdminLayout.jsx
│   │   ├── pages/             # Page level components
│   │   │   ├── Cart/          
│   │   │   ├── Checkout/      
│   │   │   ├── Home/          
│   │   │   ├── Login/         
│   │   │   ├── NotFound/      
│   │   │   ├── Orders/        
│   │   │   ├── Product/       
│   │   │   ├── Profile/       
│   │   │   ├── Register/      
│   │   │   ├── Shop/          
│   │   │   └── Wishlist/      
│   │   │
│   │   ├── routes/            # AppRoutes.jsx, ProtectedRoute.jsx, AdminRoute.jsx
│   │   ├── services/          # authService.js, productService.js, etc.
│   │   ├── store/             # Zustand/Redux store (future)
│   │   ├── styles/            # globals.css, variables.css, animations.css
│   │   ├── types/             # TypeScript definitions / Shared types (future)
│   │   ├── utils/             # formatPrice.js, validators.js, helpers.js, etc.
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
│
├── backend/                   # Flask + SQLAlchemy Backend
│   ├── app/
│   │   ├── controllers/       # auth_controller.py, product_controller.py, etc.
│   │   ├── extensions/        # db.py, jwt.py, cors.py
│   │   ├── middlewares/       # auth.py, admin.py, error_handler.py
│   │   ├── models/            # user.py, product.py, order.py, cart.py, category.py, review.py
│   │   ├── routes/            # auth.py, products.py, cart.py, orders.py, users.py, admin.py
│   │   ├── schemas/           # user_schema.py, product_schema.py, order_schema.py
│   │   ├── services/          # jwt_service.py, email_service.py, payment_service.py, upload_service.py
│   │   ├── utils/             # helpers.py, validators.py, response.py
│   │   ├── static/
│   │   └── templates/
│   │
│   ├── database/              # SQLite database storage
│   ├── instance/              # Flask instance-specific files
│   ├── logs/                  # Application logs
│   ├── migrations/            # DB migrations
│   ├── tests/                 # test_auth.py, test_product.py, test_cart.py
│   ├── uploads/               # products/, users/
│   ├── config.py              
│   ├── requirements.txt       
│   ├── run.py                 
│   ├── .env                   
│   └── .env.example           
│
├── assets/                    # Shared project assets
│   ├── avatars/
│   ├── banners/
│   ├── categories/
│   ├── hero/
│   ├── icons/
│   ├── logo/
│   ├── placeholders/
│   └── products/
│
├── docs/                      # Project documentation
│   ├── API.md
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── DATABASE.md
│   ├── DEPLOYMENT.md
│   └── FEATURES.md
│
├── media/                     # Code Red episode assets
│   ├── final-video/
│   ├── intro/
│   ├── recordings/
│   └── thumbnails/
│
├── planning/
├── screenshots/
├── .env.example
├── .gitignore
├── LICENSE
├── PROJECT_STRUCTURE.md
└── README.md
```

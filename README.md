# 🛒 Ecommerce Product API

A RESTful CRUD API for an ECommerce shopping website built with Django and Django Rest Framework, deployed on PythonAnywhere.

## 🔗 Live API
Base URL: `https://ssneha.pythonanywhere.com`

| Endpoint | Description |
|----------|-------------|
| `GET /api/products/` | List all products |
| `POST /api/products/` | Create a new product |
| `GET /api/products/{id}/` | Retrieve a product |
| `PUT /api/products/{id}/` | Update a product |
| `DELETE /api/products/{id}/` | Delete a product |
| `GET /swagger/` | API Documentation |

## 🛠️ Tech Stack

- **Python** 3.11
- **Django** - Web framework
- **Django Rest Framework** - API framework
- **SQLite** - Database
- **drf-yasg** - Swagger API documentation
- **PythonAnywhere** - Deployment
- **Docker** - Containerization (bonus)

## 📦 Product Model Fields

- `id` - Auto generated primary key
- `name` - Product name
- `description` - Product description
- `price` - Product price
- `stock` - Available stock quantity
- `created_at` - Timestamp when created

## 🚀 Local Setup

### Without Docker

1. **Clone the repository**
```bash
git clone https://github.com/snehasivadas21/ecommerce-product-api.git
cd ecommerce-product-api/shop
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Start server**
```bash
python manage.py runserver
```

6. **Access API**
- API: `http://localhost:8000/api/products/`
- Swagger Docs: `http://localhost:8000/swagger/`

---

### With Docker (MySQL)

1. **Clone the repository**
```bash
git clone https://github.com/snehasivadas21/ecommerce-product-api.git
cd ecommerce-product-api
```

2. **Create `.env` file**
```env
MYSQL_DATABASE=ecommerce_db
MYSQL_ROOT_PASSWORD=root
MYSQL_HOST=db
MYSQL_PORT=3306
DOCKER=True
```

3. **Run with Docker**
```bash
docker-compose up --build
```

4. **Access API**
- API: `http://localhost:8000/api/products/`
- Swagger Docs: `http://localhost:8000/swagger/`

## 📖 API Documentation

Swagger UI is available at:
- Local: `http://localhost:8000/swagger/`
- Live: `https://ssneha.pythonanywhere.com/swagger/`

## 🌐 Deployment

Deployed on **PythonAnywhere** at `https://ssneha.pythonanywhere.com`

### Deployment Steps
1. Clone repo on PythonAnywhere console
2. Create virtual environment with Python 3.11
3. Install requirements
4. Run migrations
5. Configure WSGI file
6. Reload web app

## 👩‍💻 Author

**Sneha**
- GitHub: [@snehasivadas21](https://github.com/snehasivadas21)
- Live API: [ssneha.pythonanywhere.com](https://ssneha.pythonanywhere.com/api/products/)


# **FastAPI Bookstore API**

## **Overview**

This project implements a simple online bookstore backend using **FastAPI**. It supports the following key functionalities:

-   User registration and login using JWT-based token authentication.
-   Browsing and searching for books by title, author, or genre.
-   Shopping cart management (adding/removing books).
-   Placing orders and managing order history.
-   Admin privileges to manage books (CRUD) and view all user orders.
-   Stock management (updates stock quantities when an order is placed).
-   Pagination for browsing books and viewing order history.

----------

## **Table of Contents**

-   [Installation](#installation)
-   [Running the Application](#running-the-application)
-   [API Endpoints](#api-endpoints)
-   [Environment Variables](#environment-variables)
-   [Database Setup](#database-setup)
-   [Authentication and Authorization](#authentication-and-authorization)
-   [Admin Role](#admin-role)
-   [Testing](#testing)

----------

## **Installation**

### **Prerequisites**

-   **Python 3.8+**: Ensure Python is installed on your machine.
-   **Pip**: Python package installer.

### **Steps**

1.  **Clone the repository**:
    
    
    ```bash
    git clone https://github.com/your-username/fastapi-bookstore.git
    cd fastapi-bookstore
    ```
    
2.  **Create and activate a virtual environment**:
    
    ```bash python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
    
3.  **Install dependencies**:
    
    ```bash 
    pip install -r requirements.txt
    ``` 
    
4.  **Set up the database**: Initialize the SQLite database and apply migrations:
    
    ```bash
    alembic upgrade head 
    ``` 
    

----------

## **Running the Application**

### **Local Development**

1.  **Run the application**:
    
    ```bash
    uvicorn main:app --reload
    ```
    
2.  **Access the API** at:
    
    -   **API Docs**: `http://127.0.0.1:8000/docs` (Swagger UI)
    -   **ReDoc**: `http://127.0.0.1:8000/redoc`
3.  **Default SQLite Database**: The database file `bookstore.db` will be created in the project root.
    

----------

## **API Endpoints**

### **Authentication**

Method

Endpoint

Description

POST

`/users/register`

Register a new user

POST

`/users/login`

Login and get a JWT token

GET

`/users/me`

Get current authenticated user

### **Bookstore Endpoints**

Method

Endpoint

Description

GET

`/books/`

Retrieve all books with pagination

GET

`/books/{book_id}`

Retrieve book by ID

GET

`/books/search/`

Search books by title, author, or genre

POST

`/cart/`

Add book to the shopping cart

GET

`/cart/`

Get the current user's shopping cart

DELETE

`/cart/{item_id}`

Remove book from the shopping cart

POST

`/orders/`

Place a new order

GET

`/orders/`

Retrieve the user's order history

### **Admin Endpoints**

Method

Endpoint

Description

POST

`/admin/books/`

Add a new book

PUT

`/admin/books/{book_id}`

Update a book by ID

DELETE

`/admin/books/{book_id}`

Delete a book by ID

GET

`/admin/orders/`

View all user orders

----------

## **Environment Variables**

You can set up environment variables in a `.env` file (optional):

Variable

Description

Default

`SECRET_KEY`

JWT secret key

`your_secret_key`

`ACCESS_TOKEN_EXPIRE_MINUTES`

Token expiration in minutes

`30`

`DATABASE_URL`

Database connection URL

`sqlite:///./bookstore.db`

If you're using a PostgreSQL or other production-grade database, adjust `DATABASE_URL` accordingly.

----------

## **Database Setup**

### **SQLite (default)**

The project uses SQLite by default. To change the database (e.g., to PostgreSQL), modify the `SQLALCHEMY_DATABASE_URL` in `database.py` and update the `alembic.ini` file for migrations.

```python
# database.py
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
``` 

### **Alembic (Database Migrations)**

If you want to handle database migrations:

1.  Initialize alembic in the project:
    
    
    ```bash
    alembic init alembic
    ``` 
    
2.  Edit the `alembic.ini` file and `env.py` for your database URL and models.
3.  Generate and apply migrations:
   
    
    ```bash
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    ``` 
    

----------

## **Authentication and Authorization**

This API uses **JWT (JSON Web Tokens)** for user authentication. Users must first register and then login to get an access token. This token must be passed in the `Authorization` header for accessing protected routes.

### Example:

-   **Login**:
    
    ```bash
    curl -X POST "http://127.0.0.1:8000/users/login" -d "username=user1&password=password123"
    ``` 
    
-   **Get Books (Protected)**:
    
    
    
    ```bash
    curl -X GET "http://127.0.0.1:8000/books/" -H "Authorization: Bearer <token>"
    ``` 
    

----------

## **Admin Role**

Admin users can manage books (add, update, delete) and view all user orders. To create an admin user, manually set the `is_admin` flag in the database for that user.

```bash
sqlite3 bookstore.db
UPDATE user SET is_admin = TRUE WHERE username = 'admin';
``` 

----------

## **Testing**

You can write and run tests for your FastAPI application using **pytest**:

1.  **Install test dependencies**:
    
    
    ```bash
    pip install pytest pytest-asyncio httpx
    ``` 
    
2.  **Create tests**: Add your test files in a `tests/` directory.
    
3.  **Run tests**:
    
  
    
    ```bash
    pytest
    ``` 
    

----------

## **Future Enhancements**

-   Implement caching for frequently accessed books.
-   Add email notifications on order completion.
-   Integrate a payment gateway.
-   Add a frontend client using React or Vue.js.

----------

## **Contributing**

Contributions are welcome! Please open a PR with any enhancements, bug fixes, or additional features.

----------

## **License**

This project is licensed under the MIT License.# **FastAPI Bookstore API**

## **Overview**

This project implements a simple online bookstore backend using **FastAPI**. It supports the following key functionalities:

-   User registration and login using JWT-based token authentication.
-   Browsing and searching for books by title, author, or genre.
-   Shopping cart management (adding/removing books).
-   Placing orders and managing order history.
-   Admin privileges to manage books (CRUD) and view all user orders.
-   Stock management (updates stock quantities when an order is placed).
-   Pagination for browsing books and viewing order history.

----------

## **Table of Contents**

-   [Installation](#installation)
-   [Running the Application](#running-the-application)
-   [API Endpoints](#api-endpoints)
-   [Environment Variables](#environment-variables)
-   [Database Setup](#database-setup)
-   [Authentication and Authorization](#authentication-and-authorization)
-   [Admin Role](#admin-role)
-   [Testing](#testing)

----------

## **Installation**

### **Prerequisites**

-   **Python 3.8+**: Ensure Python is installed on your machine.
-   **Pip**: Python package installer.

### **Steps**

1.  **Clone the repository**:
    
   
    
    ```bash
    git clone https://github.com/kwakuOfosuAgyeman/fastapi-bookstore.git
    cd fastapi-bookstore
    ``` 
    
2.  **Create and activate a virtual environment**:
    
    
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ``` 
    
3.  **Install dependencies**:
    
    
    
    ```bash
    pip install -r requirements.txt
    ``` 
    
4.  **Set up the database**: Initialize the SQLite database and apply migrations:
    
    
    
    ```bash
    alembic upgrade head  # Optional if using migrations
    ``` 
    

----------

## **Running the Application**

### **Local Development**

1.  **Run the application**:
    
    
    
    ```bash
    uvicorn main:app --reload
    ``` 
    
2.  **Access the API** at:
    
    -   **API Docs**: `http://127.0.0.1:8000/docs` (Swagger UI)
    -   **ReDoc**: `http://127.0.0.1:8000/redoc`
3.  **Default SQLite Database**: The database file `bookstore.db` will be created in the project root.
    

----------

## **API Endpoints**

### **Authentication**

Method

Endpoint

Description

POST

`/users/register`

Register a new user

POST

`/users/login`

Login and get a JWT token

GET

`/users/me`

Get current authenticated user

### **Bookstore Endpoints**

Method

Endpoint

Description

GET

`/books/`

Retrieve all books with pagination

GET

`/books/{book_id}`

Retrieve book by ID

GET

`/books/search/`

Search books by title, author, or genre

POST

`/cart/`

Add book to the shopping cart

GET

`/cart/`

Get the current user's shopping cart

DELETE

`/cart/{item_id}`

Remove book from the shopping cart

POST

`/orders/`

Place a new order

GET

`/orders/`

Retrieve the user's order history

### **Admin Endpoints**

Method

Endpoint

Description

POST

`/admin/books/`

Add a new book

PUT

`/admin/books/{book_id}`

Update a book by ID

DELETE

`/admin/books/{book_id}`

Delete a book by ID

GET

`/admin/orders/`

View all user orders

----------

## **Environment Variables**

You can set up environment variables in a `.env` file (optional):

Variable

Description

Default

`SECRET_KEY`

JWT secret key

`your_secret_key`

`ACCESS_TOKEN_EXPIRE_MINUTES`

Token expiration in minutes

`30`

`DATABASE_URL`

Database connection URL

`sqlite:///./bookstore.db`

If you're using a PostgreSQL or other production-grade database, adjust `DATABASE_URL` accordingly.

----------

## **Database Setup**

### **SQLite (default)**

The project uses SQLite by default. To change the database (e.g., to PostgreSQL), modify the `SQLALCHEMY_DATABASE_URL` in `database.py` and update the `alembic.ini` file for migrations.



```python
# database.py
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
``` 

### **Alembic (Database Migrations)**

If you want to handle database migrations:

1.  Initialize alembic in the project:
    
    
    
    ```bash
    alembic init alembic
    ``` 
    
2.  Edit the `alembic.ini` file and `env.py` for your database URL and models.
3.  Generate and apply migrations:
    
    ```bash
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    ```
    

----------

## **Authentication and Authorization**

This API uses **JWT (JSON Web Tokens)** for user authentication. Users must first register and then login to get an access token. This token must be passed in the `Authorization` header for accessing protected routes.

### Example:

-   **Login**:
    
    ```bash
    curl -X POST "http://127.0.0.1:8000/users/login" -d "username=user1&password=password123"
    ``` 
    
-   **Get Books (Protected)**:
    
    ```bash
    curl -X GET "http://127.0.0.1:8000/books/" -H "Authorization: Bearer <token>"
    ```
    

----------

## **Admin Role**

Admin users can manage books (add, update, delete) and view all user orders. To create an admin user, manually set the `is_admin` flag in the database for that user.


```bash
sqlite3 bookstore.db
UPDATE user SET is_admin = TRUE WHERE username = 'admin';
```

----------

## **Testing**

You can write and run tests for your FastAPI application using **pytest**:

1.  **Install test dependencies**:
    
    ```bash
    pip install pytest pytest-asyncio httpx
    ```
    
2.  **Create tests**: Add your test files in a `tests/` directory.
    
3.  **Run tests**:
    
    ```bash
    pytest
    ``` 
    

----------

## **Future Enhancements**

-   Implement caching for frequently accessed books.
-   Add email notifications on order completion.
-   Integrate a payment gateway.
-   Add a frontend client using React or Vue.js.

----------

## **Contributing**

Contributions are welcome! Please open a PR with any enhancements, bug fixes, or additional features.

----------

## **License**

This project is licensed under the MIT License.
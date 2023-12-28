import sqlite3

connection = sqlite3.connect('bookshop.db')
cursor = connection.cursor()


def create_users_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS users('
                   'id INTEGER PRIMARY KEY, '
                   'user_id INTEGER,'
                   'name VARCHAR(50),'
                   'phone_number VARCHAR(16));')
    connection.commit()
    return True


def get_users():
    cursor.execute(f"SELECT * FROM users;")
    result = cursor.fetchall()
    return result


def add_user(user_id, name: str):
    cursor.execute(f"INSERT INTO users("
                   f"user_id, name) "
                   f"VALUES({user_id}, '{name}');")
    connection.commit()
    return True


def check_user(user_id):
    cursor.execute(f"SELECT user_id FROM users WHERE user_id={user_id};")
    result = cursor.fetchone()
    if result is None:
        return False  # agar foydalanuvchi users table ni ichida bo'lmasa False qaytaradi
    else:
        return True  # agar foydalanuvchi users table ni ichida bo'lsa True qaytaradi


def create_category_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS category('
                   'id INTEGER PRIMARY KEY, '
                   'name VARCHAR(50));')
    connection.commit()
    return True


def add_category(name: str):
    cursor.execute(f"INSERT INTO category("
                   f"name) "
                   f"VALUES('{name}');")
    connection.commit()
    return True


def get_categories():
    cursor.execute(f"SELECT * FROM category;")
    result = cursor.fetchall()
    return result


def create_books_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS books('
                   'id INTEGER PRIMARY KEY, '
                   'name VARCHAR(50),'
                   'price INTEGER,'
                   'photo VARCHAR(255),'
                   'author VARCHAR(50),'
                   'category_id INTEGER,'
                   'FOREIGN KEY (category_id) REFERENCES category(id));')
    connection.commit()
    return True


def add_book(name: str, price: int, photo: str, author: str, category_id: int):
    cursor.execute(f"INSERT INTO books("
                   f"name, price, photo, author, category_id) "
                   f"VALUES('{name}', {price}, '{photo}', '{author}', {category_id});")
    connection.commit()
    return True


def get_books(category_id: int):
    cursor.execute(f"SELECT * FROM books where category_id=={category_id};")
    result = cursor.fetchall()
    return result


def get_book(book_id: int):
    cursor.execute(f"SELECT * FROM books where id=={book_id};")
    result = cursor.fetchone()
    return result


def create_orders_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS orders('
                   'id INTEGER PRIMARY KEY, '
                   'user_id INTEGER,'
                   'book_id INTEGER,'
                   'FOREIGN KEY (user_id) REFERENCES users (user_id),'
                   'FOREIGN KEY (book_id) REFERENCES books (id));')
    connection.commit()
    return True


def add_order(user_id, book_id):
    cursor.execute(f"INSERT INTO orders("
                   f"user_id, book_id) "
                   f"VALUES({user_id}, {book_id});")
    connection.commit()
    return True


def get_orders(user_id):
    cursor.execute(f"SELECT * FROM orders where user_id=={user_id};")
    result = cursor.fetchall()
    return result


def get_all_orders():
    cursor.execute(f"SELECT * FROM orders;")
    result = cursor.fetchall()
    return result

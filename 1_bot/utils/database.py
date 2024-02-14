import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()


    def get_categories(self):
        categories = self.cursor.execute(
            "SELECT id ,category_name FROM Catigories;")
        return categories.fetchall()

    def get_categories_1(self):
        categories = self.cursor.execute(
            "SELECT id ,catigory FROM Catigories1;")
        return categories.fetchall()

    def get_products(self, cat_id: int):
        products = self.cursor.execute(
            f"SELECT id, product_name, product_price, product_image FROM products WHERE product_category=?;",
            (cat_id,))
        return products.fetchall()

    def get_products_1(self, cat_id: int):
        products = self.cursor.execute(
            f"SELECT id, product_name, product_price, product_image FROM products1 WHERE product_category=?;",
            (cat_id,))
        return products.fetchall()


    def __del__(self):
        self.cursor.close()
        self.conn.close()
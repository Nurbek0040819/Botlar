import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # WORK WITH CATEGORIES
    def get_categories(self):  # get all categories
        categories = self.cursor.execute(
            "SELECT id, category_name FROM categories;"
        )
        return categories.fetchall()

    def add_category(self, new_category):
        try:
            self.cursor.execute(
                "INSERT INTO categories (category_name) VALUES(?);",
                (new_category,)
            )
            self.conn.commit()
            return True
        except:
            return False

    def rename_category(self, old_name, new_name):
        try:
            self.cursor.execute(
                "UPDATE categories SET category_name=? WHERE category_name=?;",
                (new_name, old_name)
            )
            self.conn.commit()
            return True
        except:
            return False

    def delete_category(self, name):
        try:
            self.cursor.execute(
                "DELETE FROM categories WHERE category_name=?;",
                (name,)
            )
            self.conn.commit()
            return True
        except:
            return False

    def check_category_exists(self, name):
        lst = self.cursor.execute(
            f"SELECT * FROM categories WHERE category_name=?",
            (name,)
        ).fetchall()
        if not lst:
            return True
        else:
            return False

    def add_product(self, title, text, image, price, phone, cat_id, u_id):
         try:
            self.cursor.execute(
                f'INSERT INTO products (product_title,product_text,product_image,product_price,product_phone,product_category,produc_owner)'
                f'VALUES(?,?,?,?,?,?,?)',
                (title, text, image, price, phone, cat_id, u_id)
            )
            self.conn.commit()
            return True
         except:
             return False

    def get_my_last_product(self, u_id):
        product = self.cursor.execute(
            f"SELECT id, product_title,product_text,product_image,product_price,product_phone FROM products WHERE produc_owner=? ORDER BY id DESC LIMIT 1",
            (u_id,)
        )
        return product.fetchone()

    def get_my_all_product(self, u_id):
        product = self.cursor.execute(
            f"SELECT id, product_title,product_text,product_image,product_price,product_phone FROM products WHERE product_category=? and produc_owner ORDER BY id",
            (u_id,)
        )
        return product.fetchall()

    def update_my_last_product(self, u_id, new_product_title, new_product_text, new_product_image, new_product_price, new_product_phone):
        self.cursor.execute(
            "UPDATE products SET product_title=?, product_text=?, product_image=?, product_price=?, product_phone=? WHERE product_owner=?",
            (new_product_title, new_product_text, new_product_image, new_product_price, new_product_phone, u_id)
        )
        self.conn.commit()



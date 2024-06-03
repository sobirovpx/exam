# Azimhojayev Muhammadrizo


import requests
import psycopg2

# conn = psycopg2.connect(dbname='n47',
#                         user='postgres',
#                         password='0060',
#                         host='localhost',
#                         port=5432)


# 1 - masala

# create_table_product = """
# create table  Product(
#     id serial primary key,
#     name varchar(55),
#     price decimal(10,2),
#     image varchar(255)
#
#
# );"""
#
# cur = conn.cursor()
# cur.execute(create_table_product)
# conn.commit()


# 2 - masala
# cur = conn.cursor()

# insert_product = """
# INSERT INTO product (name, price, image) VALUES (%s, %s, %s)"""
#
# info = ['Phone', '25', 'https://www.product.com']
#
# cur.execute(insert_product, info)
# conn.commit()
#


# select_all_products = """
# SELECT * FROM product"""
#
# cur.execute(select_all_products)
# print(cur.fetchall())
#


# update_product = """
# UPDATE product SET name = %s, price = %s, image = %s WHERE id = %s"""
# update_info = ['Pen', '1', 'https://www.product.com', 1]
#
# cur.execute(update_product, update_info)
# conn.commit()


# delete_info = [2]
# delete_product = """delete from product where id = %s"""
# cur.execute(delete_product, delete_info, )
# conn.commit()


# 3 - masala

# class Alphabet:
#     def __init__(self):
#         self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#                         't', 'u', 'v', 'w', 'x', 'y', 'z']
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.index < len(self.letters):
#             letter = self.letters[self.index]
#             self.index += 1
#             return letter
#         else:
#             raise StopIteration
#
#
# alphabet = Alphabet()
# for letter in alphabet:
#     print(letter)


# # 4 - masala
#
# import threading
# import time
#
# def print_numbers(start, end):
#     for i in range(start, end+1):
#         print(i)
#         time.sleep(1)
#
# def print_letters():
#     for letter in 'ABCDE':
#         print(letter)
#         time.sleep(1)
#
# thread1 = threading.Thread(target=print_numbers, args=(1, 5))
# thread2 = threading.Thread(target=print_letters)
#
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()


# 5 - masala
# class Product:
#     def __init__(self, name, price, image):
#         self.name = name
#         self.price = price
#         self.image = image
#
#     def save(self):
#         conn = psycopg2.connect(dbname='n47',
#                                 user='postgres',
#                                 password='0060',
#                                 host='localhost',
#                                 port=5432)
#
#         cur = conn.cursor()
#         sava_data = """INSERT INTO product (name, price, image) VALUES (%s, %s, %s)"""
#         data = (self.name, self.price, self.image)
#         cur.execute(sava_data, data, )
#         conn.commit()
#
#
# vacuum_caleaner = Product('Vacuum cleaner', '1.00', "https://www.vacuum_cleaner.com")
# vacuum_caleaner.save()

# 6 - masala
#
# class ConnectDb:
#     def __init__(self,):
#
#
#     def __enter__(self):
#         self.conn = psycopg2.connect(
#             dbname="n47",
#             user="postgres",
#             password="0060",
#             host="localhost",
#             port="5432"
#         )
#         self.cursor = self.conn.cursor()
#         return self.cursor
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type is not None:
#             self.conn.rollback()
#         else:
#             self.conn.commit()
#         self.cursor.close()
#         self.conn.close()
#
# # 7 - masala
#
# import requests
# import psycopg2
#
#
# url = 'https://dummyjson.com/products/'
#
# r = requests.get(url)
#
# conn = psycopg2.connect(dbname='n47',
#                         user='postgres',
#                         password='0060',
#                         host='localhost',
#                         port=5432)
# cur = conn.cursor()
#
# insert_into_query = """insert into product (name, price, image) values (%s,%s,%s);
#
# """
#
# # for product in r.json()['products']:
# #     cur.execute(insert_into_query, (
# #         product['title'], product['price'],str(product['images'])))
# #     conn.commit()
# #
#
#
# with ConnectDb() as cursor:
#
#     for product in r.json()['products']:
#         cur.execute(insert_into_query, (
#             product['title'], product['price'],str(product['images'])))
#         conn.commit()





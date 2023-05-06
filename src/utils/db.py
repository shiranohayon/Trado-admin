
import pymongo
from urllib.parse import quote
from bson import ObjectId
import random

# Credentials
password = 
encoded_password = quote(password)
user_name =
db_name =
id_meshi =


def create_mongo_connection():
    # Connect to MongoDB using the given credentials and return the database object
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{encoded_password}@cluster0.qnr3p.mongodb.net/{db_name}?retryWrites=true&w=majority")
    db = client[db_name]
    return db

def get_all_numbers_orders_from_db(db):
    collection = db["orders"]
    distinct_values = collection.distinct("number")
    return distinct_values


def get_random_product(db):
    product_collection = db["products"]
    all_products = product_collection.find()
    return all_products[0]

def get_product_by_id(db, id):
    product_collection = db["products"]
    product = product_collection.find_one({"id": id})
    return product

    # db is the connection object to mongo
def is_product_in_db(db, barcode):
    product_collection = db["products"]
    product = product_collection.find_one({"barcode": barcode})
    if product:
        return True
    else:
        return False

    # db is the connection object to mongo


def count_products_by_barcode_number(db, barcode):
    products_count = db.products.count_documents({"barcode": barcode})
    return products_count

def get_price_from_db_by_barcode(db, barcode):
    product_collection = db["products"]
    product = product_collection.find_one({"barcode": barcode})
    price = product['price']
    price = float(price)
    return price

def get_name_from_db_by_barcode(db, barcode):
    product_collection = db["products"]
    product = product_collection.find_one({"barcode": barcode})
    name = product['name']
    return name

def get_description_from_db_by_barcode(db, barcode):
    product_collection = db["products"]
    product = product_collection.find_one({"barcode": barcode})
    name = product['description']
    return name

def get_barcode_from_db_by_barcode(db):
    product = get_random_product(db)
    barcode = product["barcode"]
    return barcode


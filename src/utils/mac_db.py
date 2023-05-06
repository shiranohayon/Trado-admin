import pymongo
from urllib.parse import quote
from bson import ObjectId
# from key import pass_w, user_name, db_name
import ssl

pass_w = 'veHt1JK5'
user_name = 'qa_agency'
db_name = "trado_qa"

# Credentials
password = pass_w
encoded_password = quote(password)
user_name = user_name
db_name = db_name
ca_cert_file_path = '/Users/maayan/Documents/GitHub/DemonBlazeAuomationProject/venv/lib/python3.11/site-packages/pip/_vendor/certifi/cacert.pem'


# Function to create MongoDB connection
def create_mongo_connection(user_name, encoded_password, db_name ,ca_cert_file_path):

    # Connect to MongoDB using the given credentials and return the database object
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{encoded_password}@cluster0.qnr3p.mongodb.net/{db_name}?retryWrites=true&w=majority",tls=True, tlsCAFile=ca_cert_file_path)
    db = client[db_name]
    return db


# Function to test the MongoDB connection
def check_connection(db):
    try:
        db.command("ping")
        print("Connected to MongoDB.")
    except Exception as e:
        print("Error connecting to MongoDB:", e)


def show_all_collections(db):
    print("All collections:")
    for collection_name in get_collections(db):
        print(f"- {collection_name}")


def find_document_by_key_value(db, collection_name, key, value):
    collection = db[collection_name]
    document = collection.find_one({key: value})
    return document

def find_document_id(db, collection_name, key, value):
    collection = db[collection_name]
    document = collection.find_one({key: value})
    return document









def sum_values_in_key(db, collection_name, document_id, key):
    collection = db[collection_name]
    document = collection.find_one({'_id': ObjectId(document_id)})
    if document:
        value_list = document.get(key, [])
        return sum(value_list)
    else:
        return None


def count_specific_values(db, collection_name, document_id, key, value):
    collection = db[collection_name]
    document = collection.find_one({'_id': ObjectId(document_id)})
    if document:
        value_list = document.get(key, [])
        return value_list.count(value)
    else:
        return None


# Function to get a list of collection names in the given database
def get_collections(db):
    collections = db.list_collection_names()
    return collections


# Function to display collection names in the given database
def display_collections(db):
    collections = db.list_collection_names()
    for collection in collections:
        print(f'Collection name: {collection}')


# Function to display document count and an example document for each collection in the given database
def display_samples(db, collection):
    collections = get_collections(db)
    sample_collection = db[collection]
    print(f'Example data set: {sample_collection.find_one()}')


# Function to display all documents in a given collection
def display_all_documents_in_a_collection(db, collection_name):
    collection = db[collection_name]
    documents = collection.find()
    for document in documents:
        print(document)


# Function to get the value of a specific key in a document identified by its ID in a given collection
def get_specific_key_value(db, collection_name, document_id, key):
    collection = db[collection_name]
    document = collection.find_one({'_id': ObjectId(document_id)})
    if document:
        value = document.get(key)
        return value
    else:
        return None

def get_loginCode(db):
    collection = db['users']
    document = collection.find_one({'_id': ObjectId('6419ad27c122f37221c04426')})
    if document:
        value = document.get('loginCode')
        return value
    else:
        return None


# Function to count the documents with a specific key-value pair in a given collection
def count_key_value(db, collection_name, key, value):
    collection = db[collection_name]
    count = collection.count_documents({key: value})
    return count


# Function to get the distinct values of a specific key in a given collection
def get_distinct_key_values(db, collection_name, key):
    collection = db[collection_name]
    distinct_values = collection.distinct(key)
    return distinct_values


# Function to test the stock status of products in the 'products' collection
def show_product_stock(db):
    products = db['products']
    out_of_stock_products = products.count_documents({"productStock": 0})
    print(f"There are {out_of_stock_products} out-of-stock products.")


# Function to test the order status in the 'orders' collection
def show_orders(db):
    orders = db['orders']
    pending_orders = orders.count_documents({"status": "ready"})
    print(f"There are {pending_orders} ready orders.")

def get_random_departments(db):
    departments_collecton = db["departments"]
    all_departments = departments_collecton.find()
    return all_departments[0]


# Main function
def main():
    db = create_mongo_connection(user_name, encoded_password, db_name,ca_cert_file_path)
    check_connection(db)

    # Main menu
    while True:
        print("\n--- Main Menu ---")
        print("1. Show all collections")
        print("2. Display sample documents")
        print("3. Display all documents in a collection")
        print("4. Get specific key-value")
        print("5. Count key-value pairs")
        print("6. Get distinct key values")
        print("7. Test product stock")
        print("8. Test order status")
        print("9. Find document by key and value")
        print("10. Sum all values in a specific key")
        print("11. Count specific values of a specific key")
        print("12. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_collections(db)
        if choice == "2":
            collection_name = input("Enter collection name: ")
            display_samples(db, collection_name)
        elif choice == "3":
            collection_name = input("Enter collection name: ")
            display_all_documents_in_a_collection(db, collection_name)
        elif choice == "4":
            collection_name = input("Enter collection name: ")
            document_id = input("Enter document ID: ")
            key = input("Enter key: ")
            value = get_specific_key_value(db, collection_name, document_id, key)
            print(f"The {key} for document with ID '{document_id}' is: {value}")
        elif choice == "5":
            collection_name = input("Enter collection name: ")
            key = input("Enter key: ")
            value = input("Enter value: ")
            count = count_key_value(db, collection_name, key, value)
            print(f"There are {count} documents with '{key}': '{value}'.")
        elif choice == "6":
            collection_name = input("Enter collection name: ")
            key = input("Enter key: ")
            distinct_values = get_distinct_key_values(db, collection_name, key)
            print(f"The distinct {key} values in {collection_name} are: {distinct_values}")
        elif choice == "7":
            show_orders(db)
        elif choice == "8":
            show_orders(db)

        elif choice == "9":
            collection_name = input("Enter collection name: ")
            key = input("Enter key: ")
            value = input("Enter value: ")
            document = find_document_by_key_value(db, collection_name, key, value)
            if document:
                print(f"Document found: {document}")
            else:
                print("No document found.")
        elif choice == "10":
            collection_name = input("Enter collection name: ")
            document_id = input("Enter document ID: ")
            key = input("Enter key: ")
            total = sum_values_in_key(db, collection_name, document_id, key)
            if total is not None:
                print(f"Total sum of values in key '{key}': {total}")
            else:
                print("Document not found.")
        elif choice == "11":
            collection_name = input("Enter collection name: ")
            document_id = input("Enter document ID: ")
            key = input("Enter key: ")
            value = input("Enter value: ")
            count = count_specific_values(db, collection_name, document_id, key, value)
            if count is not None:
                print(f"Count of value '{value}' in key '{key}': {count}")
            else:
                print("Document not found.")
        elif choice == "12":
            break
        else:
            print("Invalid choice. Please try again.")


# if __name__ == '__main__':
#     main()


db = create_mongo_connection(user_name, encoded_password, db_name, ca_cert_file_path)
logincode = get_loginCode(db)
print(logincode)

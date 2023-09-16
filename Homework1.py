import mysql.connector
from mysql.connector import Error
# Reference from TA during Class week 3 demonstration
# Connecting my SQL Workbench to python
try:
    connection = mysql.connector.connect(
        host = "cis3368fall.cpvsnyxrpwn2.us-east-1.rds.amazonaws.com", 
        user = "Cmao5", 
        password = "Takai2020!", 
        database = "cis3368falldb" 
    )
except Error as err:
    print("failure in establishing connection")
    exit()

print("connection successful")


cursor = connection.cursor(dictionary=True)
sql = "select * from Retail"
cursor.execute(sql)

results = cursor.fetchall()


for datarow in results:
    print(f"seller: {datarow['seller']}, product: {datarow['product']}, quantity: {datarow['quantity']},price: {datarow['price']}")    

# Reference FROM the Homework 1 instruction example
data = [
 {'id': 1, 'Seller': 'Gregory', 'Product': 'Toothbrush', 'Quantity': 50, 'Price': 16.29},
 {'id': 2, 'Seller': 'Laslow', 'Product': 'GTA 5', 'Quantity': 10, 'Price': 60.00},
 {'id': 3, 'Seller': 'Arthur', 'Product': 'Xbox Series X', 'Quantity': 20, 'Price': 499.00},
 {'id': 4, 'Seller': 'Gregory', 'Product': 'ToothPaste', 'Quantity': 50, 'Price': 5.29},
 {'id': 5, 'Seller': 'Laslow', 'Product': 'Red Dead Redemption 2', 'Quantity': 20, 'Price': 60.00},
 {'id': 6, 'Seller': 'Arthur', 'Product': 'Playstation 5', 'Quantity': 40, 'Price': 500.00},
 {'id': 7, 'Seller': 'Gregory', 'Product': 'Floss', 'Quantity':  50, 'Price': 1.99},
 {'id': 8, 'Seller': 'Laslow', 'Product': 'LA Norie', 'Quantity': 10, 'Price':  40.00},
{'id': 9, 'Seller': 'Arthur', 'Product': 'Nintendo Switch', 'Quantity': 30, 'Price': 299.00},
]

# Reference from ChatGPT generated example, using the example templet to apply my data in it
# Created a calculation Module by showing each seller and what product they are selling 
def calculate_total_sales(seller_name):
    seller_data = {
        'Gregory': [
            {'Product': 'Toothbrush', 'Quantity': 50, 'Price': 16.29},
            {'Product': 'ToothPaste', 'Quantity': 50, 'Price': 5.29},
            {'Product':'Floss' , 'Quantity':50 , 'Price':1.99}     
        ],
        'Laslow': [
            {'Product': 'GTA 5', 'Quantity': 10, 'Price': 60.00},
            {'Product': 'Red Dead Redemption 2', 'Quantity': 20, 'Price': 60.00},
             {'Product':'LA Norie' , 'Quantity':10 , 'Price':40.00} 
        ],
        'Arthur': [
            {'Product': 'Xbox Series X', 'Quantity': 20, 'Price': 499.00},
            {'Product': 'Playstation 5', 'Quantity': 40, 'Price': 500.00},
            {'Product':'Nintendo Switch' , 'Quantity':30 , 'Price':299.00}
        ]
    }

    total_sales = 0
# make the calculation using if for each of the sellers
    if seller_name in seller_data:
        print(f"Sales Report for {seller_name}:")
        for product in seller_data[seller_name]:
            product_name = product['Product']
            quantity = product['Quantity']
            price = product['Price']
            total = quantity * price
            total_sales += total

            print(f"- Product: {product_name}, Quantity: {quantity}, Price: ${price:.2f}, Total: ${total:.2f}")
        
        print(f"Total Sales for {seller_name}: ${total_sales:.2f}")
    else:
        print(f"Sorry, {seller_name} is not in our list.")

# Show sellers
print("Available Sellers:")
print("Gregory")
print("Laslow")
print("Arthur")

# Dial in a seller name
seller_name = input("Enter the seller's name: ")

# Display the result of total price for all the sellers merchant
calculate_total_sales(seller_name)



    


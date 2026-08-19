import sqlite3
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "people.db")
from users import users_data


conn = sqlite3.connect(db_path) # Insert the name of your database inside the quotes
cursor = conn.cursor()

for user in users_data:
    #cursor.execute("INSERT INTO fertilizers (brand, price, type) VALUES (?, ?, ?)", (fertilizer['brand'], fertilizer['price'], fertilizer['type']))
    # create a similar line of code to the above line insert the user INSTEAD of fertilizer data into the users table
    cursor.execute("INSERT INTO users (username, password, auth_level) VALUES (?, ?, ?)", (user['username'], user['password'], user['auth_level']))
    pass
conn.commit()
conn.close()

print("Data inserted successfully.")

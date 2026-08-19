
import sqlite3
import os

# Get the folder where createDB.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Create people.db in the repository root
db_path = os.path.join(base_dir, "people.db")

conn = sqlite3.connect(db_path)# Add the name of your database inside the quotes

cursor = conn.cursor()
### Add SQL to define your table inside the quotes below
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY autoincrement,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    auth_level INTEGER NOT NULL
                )''')
conn.commit()
conn.close()
# Add the name of your database in the quotes below
print("Database 'people.db' created successfully.")


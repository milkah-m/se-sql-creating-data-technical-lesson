#1. imports
import sqlite3 

#2. establish connection
conn = sqlite3.connect("database.sqlite")
cur = conn.cursor()

#3. create the table
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        signup_date DATE DEFAULT CURRENT_DATE
                );
""")

# #4. alter the table
# cur.execute("""
# ALTER TABLE users ADD COLUMN phone_number TEXT;
# """)

#5. drop the table
# cur.execute("""
# DROP TABLE users;
# """)

#6. insert data
# cur.execute("""
# INSERT INTO users (name, email)
# VALUES ("Milkah Gee", "milkah@gee.com"),
#         ("Kimmy Gracie", "kimmy@gracie.com");
# """)

# # conn.commit()
# cur.execute("""
# SELECT * from users;
# """)
# print(cur.fetchall())

#7. update data
cur.execute("""
UPDATE users 
SET phone_number = '+254000000'
WHERE id = 1;
""")
conn.commit()
cur.execute("""
SELECT * from users;
""")
print(cur.fetchall())

# cur.execute("""
#     INSERT INTO users (name, email)
#     VALUES 
#         ('Test User', 'test@test.com');
# """)

# conn.commit()



cur.execute("""
    DELETE FROM users
    WHERE name = 'Test User';
""")

conn.commit()

cur.execute("""
SELECT * from users;
""")
print(cur.fetchall())

cur.execute("""SELECT * FROM users WHERE name = 'Test User';""")
print(cur.fetchall())

conn.close()
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="testdatabase"
)

mycursor = db.cursor()

# creating tables
# ---------------

# mycursor.execute("CREATE TABLE Person(name varchar(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT )")
# mycursor.execute("DESCRIBE Person")
# for x in mycursor:
#     print(x)

# inserting data into TABLE
# ---------------------------

# mycursor.execute("INSERT INTO Person (name,age) VALUES ('tim',19)")
# db.commit()

# mycursor.execute("select * from person")

# for x in mycursor:
#     print(x)

# create a new table
# -------------------

# mycursor.execute("CREATE TABLE test (name varchar(50) , created datetime NOT NULL, gender ENUM('M','F','O') not null,id int primary key NOT NULL AUTO_INCREMENT)")

# INSERT DATA INTO TABLE
# -----------------------

# mycursor.execute("insert into test (name,created,gender) VALUES (%s,%s,%s)",("SIAM",datetime.now(),"M"))
# db.commit()

# view data from table by filtering
# ----------------------------------

# mycursor.execute("select * from test where gender = 'f' order by id DESC")
# for x in mycursor:
#     print(x)


# Alter table
# ------------

# add a new column
# -----------------

# mycursor.execute("ALTER TABLE test ADD COLUMN food varchar(50) NOT NULL ")
# delete a column from a table
# ----------------------------
# mycursor.execute("ALTER TABLE test DROP food")

# change a column name
# ----------------------------

# mycursor.execute("ALTER TABLE test change name first_name varchar(50)")

# Foreign keys
user = [("tim", "techwithtim"),
        ("siam", "SiamAhmed"),
        ("sarah", "sarah")
        ]
user_scores = [(45, 100),
               (30, 200),
               (50, 400)
               ]
Q1 = "create table users (id int primary key AUTO_INCREMENT, name varchar(50), passwd varchar(50))"
Q2 = "create table scores (userId int primary key, foreign key(userid) references users(id),  game1 int default 0,  game2 int default 0)"

# mycursor.execute(Q1)
# mycursor.execute(Q2)

# mycursor.execute("Show tables")

# for x in mycursor:
#     print(x)

#insert more than one value into a table
#---------------------------------------------------------------

# mycursor.executemany("insert into users (name,passwd) values (%s,%s)",user)

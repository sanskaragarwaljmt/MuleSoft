import sqlite3
try:
    sqliteConnection = sqlite3.connect('MSmovies.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

cursor.execute("""CREATE TABLE Movies_Table (
    Movie_Name     VARCHAR PRIMARY KEY,
    Movie_Actor    VARCHAR,
    Movie_Actress  VARCHAR,
    Movie_Year     INTEGER,
    Movie_director VARCHAR,
    Movie_lang     VARCHAR
)""")

# Inserting data into table
cursor.execute("INSERT INTO Movies_Table VALUES('Avengers','Robert Downey','Brie  Larson','2019','Sarah Finn','English')")
print("Command executed successfully")
cursor.execute("INSERT INTO Movies_Table VALUES('Spider-man no way home','Tom Holland','Zendaya','2021','Sami Raimi ','English')")
cursor.execute("INSERT INTO Movies_Table VALUES('Joker','Joaquin','Frances','2019','Shayna','English')")
cursor.execute("INSERT INTO Movies_Table VALUES('The Dark Knight','Christian bale','Anne','2008','John Papsidera','English')")
cursor.execute("INSERT INTO Movies_Table VALUES('Edge of Tomorrow','Tom Cruise','Emily Blunt','2014','Doung Liman','English')")
cursor.execute("INSERT INTO Movies_Table VALUES('Parasite','Choi Woo-shik','Park So-dam','2019','Bong Joon-ho','English')")
cursor.execute("INSERT INTO Movies_Table VALUES('F9 ','Vin Deisel','Michelle','2021','Justin Lin','English')")
cursor.execute("INSERT INTO Movies_Table VALUES('Inception','leonardo','Mario Cotillard','2010','Christopher','English')")

cursor.execute("SELECT * FROM Movies_Table")
movie_list = cursor.fetchall()
for i in movie_list:
    print (i)
print("\n")

f=0
name = input("Enter the actor name to print his movie:")
name = name.upper()         
for i in movie_list:
    t=i[1].upper()          
    if(t==name):
        cursor.execute("SELECT * FROM Movies_Table WHERE Movie_Actor='i[1]'")
        mov_list = cursor.fetchall()
        print(i)
        f=1
if(f==0):
    print("Actor not found in the database!!")
    cursor.close()
    sqliteConnection.close()
    print("The SQLite connection is closed")

import sqlite3
import uuid

def get_all():

    try:

        sqliteConnection = sqlite3.connect('identifier.sqlite') #DB'ye bağlanıldı ve bir kursör oluşturuldu.
        cursor = sqliteConnection.cursor()
        print('DB Init')

        sql_query = """SELECT * FROM ToDoList;"""  # Kürsör yardımıyla SQL sorgusu kullanılarak DB'den veri çekildi
        cursor.execute(sql_query) 

        result = cursor.fetchall()  
        print(result)

        cursor.close()

    except sqlite3.Error as error:  # Hataları yakalayabilmek için Except kod bloğu kullanıldı.
        print('Error occured - ', error)

    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

    return  result


def add_item(name,description,date,status): # DB'de girdi oluşturmak amacı ile fonksiyon tanımlandı
    try:

        sqliteConnection = sqlite3.connect('identifier.sqlite')
        cursor = sqliteConnection.cursor()
        print('DB Init')

        val=str(uuid.uuid4())
        print(val,name,description,date,status)
        sql_query = f"""INSERT into ToDoList(id,name,description,date,status) VALUES('{val}','{name}','{description}','{date}','{status}');"""
        print(sql_query)
        cursor.execute(sql_query)
        sqliteConnection.commit() # Veri DB'ye kaydedilir.


        cursor.close()

    except sqlite3.Error as error:
        print('Error occured - ', error)

    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')


def update(id,name,description,date,status): # Girilen girdi uuid ile çağrılır kullanıcı tarafından güncellenir.
    try:

        sqliteConnection = sqlite3.connect('identifier.sqlite')
        cursor = sqliteConnection.cursor()
        print('DB Init')


        sql_query = f"""UPDATE  ToDoList SET name='{name}' ,  description= '{description}',date='{date}',status='{status}'    WHERE   id= '{id}';"""

        print(sql_query)
        cursor.execute(sql_query)
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print('Error occured - ', error)

    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

def delete(id): # Girdiler ID numarasına göre çağrılır ve SQL sorgusu ile silme işlemi gerçekleşir.
    try:

        # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('identifier.sqlite')
        cursor = sqliteConnection.cursor()
        print('DB Init')

        sql_query = f"""DELETE FROM   ToDoList;"""

        print(sql_query)
        cursor.execute(sql_query)
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print('Error occured - ', error)


    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

def getTodosByState(state): #Girilen Status durumuna göre ekrana aynı status değerine sahip girdiler ekrana yazdılır.
    try:

        sqliteConnection = sqlite3.connect('identifier.sqlite')
        cursor = sqliteConnection.cursor()
        print('DB Init')


        sql_query = f"""SELECT * FROM ToDoList WHERE  status= '{state}';"""

        print(sql_query)
        cursor.execute(sql_query)
        sqliteConnection.commit()

        result = cursor.fetchall()
        print("result", result)

        cursor.close()

        return result
    except sqlite3.Error as error:
        print('Error occured - ', error)

    finally:

        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

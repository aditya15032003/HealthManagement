#LOGIN PORTAL FOR THE APP

'''
1. CREATE A  CONNECTION FOR THE SQL DATABASE
2. CREATE A TABLE WITH ALL THE FIELDS
3. INSERT USER VALUES INTO THAT TABLE WHICCH GETS STORED IN THE DATABASE
4. CREATE A USER ENTRY PORTAL WHERE USER GETS TO ENTER ONLY THE USERNAME AND THE PASSWORD
Also functiom to check whetehr that entery katches with the userentry we did

5.  MAIN FUNCTION WHERE WE EXECUTE ALL REQUROEMENTS, LIKE TAKING INPUT FROM THE USER, AND STORING THAT VALUES IN DATABASE, THRN PROMPT THE USER TO ENTER HIS CRED, AND MATCH THAT DATA WITH THE DATABASE
'''

import mysql.connector
import random

#Function to create a connection for the SQL DATABASE
def connection():
    try:
        global conn
        conn= mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "MySQL@123",
        )
        return conn
    except mysql.connector.Error as err:
        print("Error", err)
        
#WHEN YOU ARE EXECUTING THE PROGRAM FOR THE FIRST TIME, THEN ONLY THIS SQL FUNCTION WILL HAVE TO BE EXECUTED, NOT AFTER THAT, OTHERWISE IT WILL DROP THE DATABASE CREATED BEFORW AND ALL ENTERIES WILL BE DELETED
#WHILE EXECUTING FOR 2ND TIME, WE COMMENT OUT THIS PART    
# def sql(conn):
#     try:
#         global cursor
#         cursor = conn.cursor()
#         cursor.execute("DROP DATABASE IF EXISTS HealthManagement")
#         db1 = "CREATE DATABASE HealthManagement"; cursor.execute(db1)
#         usedb1 = "USE HealthManagement";  cursor.execute(usedb1)
#         table = "CREATE TABLE UserCredentials(ID int(10), NAME varchar(100), Email varchar(100), Username varchar(100), Address varchar(250), Password varchar(16))"
#         cursor.execute(table)

#         conn.commit()
#         cursor.close()
#     except mysql.connector.Error as err:
#         print("error", err)

#THIS FUNCTION IS BEING USED TO ACCESS THE DATABASE, only if executed 2nd time
        
def use_database(conn):
    cursor = conn.cursor()
    use_db = "USE HealthManagement"; cursor.execute(use_db)

    conn.commit()
    cursor.close()


    
def password():

    
    
    str1 = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm12344567890!@#$^&*()"
    
    
    global passw ; passw = ""
    user_input = int(input("Enter how long you want the length of your pasword: "))

    if user_input < 8:
        print("Your password is not strong enough")
        
    else:
        for i in range(0, user_input):
            next_char = random.choice(str1)
            passw = passw + next_char
        

def insert_values(name, email, username, address, Password):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO UserCredentials (NAME, Email, Username, Address, Password) VALUES (%s, %s, %s, %s, %s)",
                       (name, email, username, address, passw))
        
        conn.commit()
        cursor.close()
    
    except mysql.connector.Error as err:
        print("Error", err)
        
def login(conn, username, passw):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UserCredentials WHERE username = %s AND password = %s", (username, passw))  #compares the username and passw variable created with the username and password in the table
        result = cursor.fetchone()

        if result:
            print("Logged in successfully\n")
            print("Hello welcome to the FITNESS MANAGEMENT PORTAL")
            #execute HEALTH()



        else:
            print("Incorrect username or password")
        return True
    except mysql.connector.Error as err:
        print("Error", err)

def main():
    
    conn = connection()
    use_database(conn)
    if conn:
        # sql(conn)
        while True:
            print("1 for Login")
            print(" 2 for Add a new user")
            print(" 3 for Exit ")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                global username
                username = input("Enter your username: ")
                passw = input("Enter your password :")
                
                login(conn, username, passw)

                if login:
                    break
                    
                
            elif choice == 2:
                print("Enter your information to sign up\n")
                
                name = input("Enter your name: ")
                username = input("enter your username: ")
                email = input("enter your email: ")
                address = input("enter your address: ")
                pass_query = input("Do you want to input your password or wanna generate a new one: (INPUT/GENERATE: )")
                if pass_query == "Generate" or pass_query =="generate" or pass_query == "GENERATE":
                    passw = password()
                    print(passw)
                    insert_values(name, email, username, address, passw)

                    if insert_values:
                        print("Your data has been successfully added: ")
                elif pass_query == "Input" or pass_query =="input" or pass_query == "INPUT":
                    while True:
                        input_pass = input("Enter your password: ")
                        if len(input_pass) < 8:
                            print("Please enter a stronger password: ")
                        else:
                            print("Your input password is stored")
                            store_pass = input_pass
                            insert_values(name, email, username, address, store_pass)
                            break
                else:
                    print("INVALID INPUT")
                
                    
            elif choice == 3:
                print("You have successfully exited out of this program: ")
                break
    else:
        print("Connection not established, there is an issue with the portal, please check the host and the user credentials for yur sql connection")
if __name__ == "__main__":
    main()









    

        

   


import mysql.connector
import maskpass
from datetime import datetime as time
import logging

def main():
    #connecting to db
    logging.basicConfig(filename='queryapp.log', filemode='w', encoding='utf-8', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p' ,format=f"%(asctime)s - %(levelname)s - %(filename)s %(funcName)s %(lineno)s - %(message)s")

    cnx = mysql.connector.MySQLConnection(user='root', password='Veyron656!', host='127.0.0.1', database='dispatch_center')

    #logging information (date it occurred, the action, by whom)

    actions_end = ['select', 'describe', 'show']

    while True:

        login = input("Enter Username or type 'exit': ")
        if login == 'exit':
            logging.info('User Exits Program')
            break
        password = maskpass.askpass(mask='*')
        
        with cnx.cursor() as cursor:
            
            #Checks for user login is valid else, requests user to re-enter credentials
            Bool = False 
            while Bool == False:
                result = cursor.execute(f"""select count(*) from login where username = '{login}' && password = SHA('{password}')""")
                rows = cursor.fetchall()
                access = rows[0][0]
                if access > 0:
                    print('Access Granted!')
                    Bool = True
                    logging.info('User Successfully Login')
                else:
                    print("Username or Password invalid")
                    login = input('Enter Username: ')
                    password = maskpass.askpass(mask='*')

        Queue = True
        while Queue == True:
            #Query
            #TODO: BASED ON IF THEY ARE ADMIN OR NOT, WHAT PERMISSION DO THEY HAVE
            #checks if they are admin (they will have letter D as their first letter)
            admin_status = login[0]
            query = input("Enter a query or type 'end' to end session: ")
            query_list = query.split()
            if query == 'end':
                print('Signed out\n')
                t = str(time.now())
                logging.info('User Successfully Logout')
                Queue = False
            else:
                if (query_list[0] not in actions_end and admin_status != 'D'):
                    print('You do not have permissions for that action.\n')
                    logging.error('End-User Accessing Functions Without Permission')
                else:
                    try:
                        with cnx.cursor() as cursor:
                            result = cursor.execute(query)
                            rows = cursor.fetchall()
                            for row in rows:
                                match query_list[0]:
                                    case 'select':
                                        print(row)
                                    case 'describe':
                                        print(row[0])
                                    case 'show':
                                        print(row[0])
                            logging.info('Successful Query')
                    except:
                        logging.error('Invalid Query')
                        print('Invalid Query!\n')

                    match query_list:
                        case 'select':
                            logging.info('Successful Query Search')
                        case 'insert':
                            logging.info('Successful Query Insertion')
                        case 'update':
                            logging.info('Successful Query Update')
                        case 'delete':
                            logging.info('Successful Query Delete')

    #disconnecting to db
    cnx.close()
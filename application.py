import mysql.connector
import maskpass
from datetime import datetime as time
import logging

def main():
    #connecting to db
    logging.basicConfig(filename='app.log', filemode='w', encoding='utf-8', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p' ,format=f"%(asctime)s - %(levelname)s - %(filename)s %(funcName)s %(lineno)s - %(message)s")
    cnx = mysql.connector.MySQLConnection(user='root', password='Veyron656!', host='127.0.0.1', database='dispatch_center')

    #logging information (date it occurred, the action, by whom)

    with cnx.cursor() as cursor:
        result = cursor.execute('show tables')
        tables = cursor.fetchall()

    arr = []
    for table in tables:
        arr.append(table[0])

    def condition_case(cond, carr, table):
        with cnx.cursor() as cursor:
            result = cursor.execute(f"""describe {table}""")
            columns = cursor.fetchall()
            for i in columns:
                print(i[0])
        match cond:
            case 1:
                col = str(input("How would like to filter it (column = 'condtion')? "))
                carr.append(f'where {col}')
            case 2:
                col = str(input("What column would you like to group it by? "))
                carr.append(f'group by {col}')
            case 3:
                while True:
                    col = str(input("How would you like to filter it (column = 'condition')? "))
                    carr.append(f'having {col}')
            case 4:
                while True:
                    ord = str(input("What column(s) would you like it ordered by ('column')? "))
                    desc_or_asc = str(input('Ascending (Y/N)?'))
                    if desc_or_asc == 'Y':
                        carr.append(f'order by {ord} asc')
                        break
                    elif desc_or_asc == 'N':
                        carr.append(f'order by {ord}')
                        break
                    else:
                        print('Not a valid input!')
        return
                        

    def select():
        print('\n')
        for a in arr:
            print(a)
        table = str(input('what table would you like to view? '))
        if table in arr:
            with cnx.cursor() as cursor:
                req = cursor.execute(f"""describe {table}""")
                col = cursor.fetchall()
                print('\n')
                for c in col:
                    print(c[0])
                carr = ['select']
                while True:
                    columns = input("What column(s) would you like to look at (type '0' to finish)? ")
                    if columns == '0':
                        break
                    carr.append(columns)
                carr.append(f'from {table}')
                ord = [-1]
                while True:
                    act = ['1. WHERE', '2. GROUP BY', '3. HAVING', '4. ORDER BY']
                    for i in act:
                        print(i)
                    condition = int(input("Any conditions (type '0' to finish)? "))
                    if condition == 0:
                        break 
                    elif condition > 0 and condition < 5 and condition > ord[-1]:
                        ord.append(condition)
                        condition_case(condition, carr, table)
                    else:
                        print('\nInvalid action!\n')   
                que = ' '.join([str(sent) for sent in carr]) 
                with cnx.cursor() as cursor:
                    print(que)
                    try:
                        result = cursor.execute(que)
                        rows = cursor.fetchall()   
                        for row in rows:
                            print(row)
                        logging.info('Successful Query Search')
                    except:
                        logging.error('Unsuccessful Query Search')
                        print('Invalid query!')
        else:
            print('Not a valid table\n')



    def update():
        print('\n')
        for a in arr:
            print(a)
        table = str(input('what table would you like to update? '))
        if table in arr:
            with cnx.cursor() as cursor:
                req = cursor.execute(f"""describe {table}""")
                col = cursor.fetchall()
                print('\n')
                for c in col:
                    print(c[0])
                carr = [f'update {table} set']
                up = []
                while True:
                    columns = str(input("What column(s) would you like to update (type '0'to finish)? "))
                    if columns == '0':
                        break
                    howso = str(input("What value would you like to update this column with? "))
                    carr.append(f'{columns} = {howso}')
                condition_case(1, carr, table)
                que = ' '.join([str(sent) for sent in carr]) 
                with cnx.cursor() as cursor:
                    try:
                        result = cursor.execute(que)
                        logging.info('Successful Query Update')
                    except:
                        logging.error('Unsuccessful Query Update')
                        print('Invalid query!')

        else:
            print('Not a valid table\n')


    def insert():
        print('\n')
        for a in arr:
            print(a)
        table = str(input('what table would you like to insert new values? '))
        if table in arr:
            with cnx.cursor() as cursor:
                req = cursor.execute(f"""describe {table}""")
                col = cursor.fetchall()
                print('\n')
                carr = [f'insert into {table}(']
                for c in col:
                    print(c[0])
                    if c[0]  == col[-1][0]:
                        carr.append(f'{str(c[0])})')
                    else:
                        carr.append(f'{str(c[0])},')
                carr.append('values')
                i = 0
                while True:
                    columns = str(input("Insert your values ##(value1, value2, etc.)##, type '0' when you are done: "))
                    if columns == '0':
                        carr[-1] = prev
                        break
                    carr.append(f'{columns},')
                    prev = columns
                que = ' '.join([str(sent) for sent in carr]) 
                with cnx.cursor() as cursor:
                    try:
                        result = cursor.execute(que)
                        logging.info('Successful Value Insertion')
                    except:
                        logging.error('Unsuccessful Value Insertion')
                        print('Invalid query!')
        else:
            print('Not a valid table\n')



    def delete():
        print('\n')
        for a in arr:
            print(a)
        table = str(input('what table would you like to delete from? '))
        if table in arr:
            with cnx.cursor() as cursor:
                req = cursor.execute(f"""describe {table}""")
                col = cursor.fetchall()
                print('\n')
                carr = [f'delete from {table}']
                condition_case(1, carr, table) 
                que = ' '.join([str(sent) for sent in carr]) 
                with cnx.cursor() as cursor:
                    try:
                        result = cursor.execute(que)
                        logging.info('Successful Row Deletion')
                    except:
                        logging.error('Unsuccessful Row Deletion')
                        print('Invalid query!')
        else:
            print('Not a valid table\n')

    def admin(admin_status):
        options_user = ['1. Search information', '0. Logout']
        options = ['1. Search information', '2. Update information', '3. Input new information', '4. Delete information', '0. Logout']
        while True:
            if admin_status == "D":
                for i in options:
                    print(i)
                action = int(input('What would you like to do? '))
                if action < 0 or action > 4:
                    print('Not an option!\n')
                else:
                    match action:
                        case 1:
                            select()
                        case 2:
                            update()
                        case 3:
                            insert()
                        case 4:
                            delete()
                        case 0:
                            t = str(time.now())
                            logging.info('User Logout')
                            break
            else:
                for i in options_user:
                    print(i)
                action = int(input('What would you like to do? '))
                if action < 0 or action > 1:
                    print('Not an option!\n')
                else:
                    match action:
                        case 1:
                            select()
                        case 0:
                            t = str(time.now())   
                            logging.info('User Logout')                     
                            break            


    while True:

        login = input("Enter Username or type 'exit': ")
        if login == 'exit':
            logging.info('Exit Program')
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
                    print('Access Granted!\n')
                    Bool = True
                    logging.info('Successful User Login')
                else:
                    logging.error('Invalid Username/Password')
                    print("\nUsername or Password invalid")
                    login = input("Enter Username or type 'exit': ")
                    if login == 'exit':
                        break
                    password = maskpass.askpass(mask='*')
        if login == 'exit':
            logging.info('Exit Program')
            break
        admin_status = login[0]
        admin(admin_status)

    #disconnecting to db
    cnx.close()
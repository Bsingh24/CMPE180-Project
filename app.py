#SJSU CMPE 138 FALL 2023 TEAM12 

import application as a
import applicationquery as b


arr = ['A','B', 'exit']
while True:
    query = input("App A (User-Friendly) or B (Admin-based)? Type 'exit' to leave: ")
    if query not in arr:
        print('Not an option!\n')
    match query:
        case 'A':
            a.main()
        case 'B':
            b.main()
        case 'exit':
            break
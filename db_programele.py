import sqlite3

<<<<<<< HEAD
connector=sqlite3.connect("db/zmone.db")
cursor=connector.cursor()

with connector:
    while True:
        vardas = input("Iveskite varda arba !, kad iseiti, arba . kad ivesti nauja: ")
        if vardas == "!":
            break
        elif vardas ==".":
            print("---NAUJAS draugelis ---")
            naujas_vardas = input("Vardas:  ")
            nauja_pavarde = input("Pavarde  :")
            naujas_email = input("E-mail:  ")
            cursor.execute('INSERT INTO draugai (first_name, last_name, email) VALUES (?,?,?)',
                (naujas_vardas, nauja_pavarde, naujas_email,))
            connector.commit()
        else:
            # f-stringui, naudojame viengubas kabutes, o duombazei, dvigubas
            select_quary = 'SELECT * FROM draugai WHERE first_name LIKE ?'
            cursor.execute(select_quary, (f'%{vardas}%', ))
            rezultatas = cursor.fetchall()
            if rezultatas:
                print(f"Radau tokius draugelius:")
                for draugas in rezultatas:
                    print(f"-{draugas[0]} {draugas[1]} ({draugas[2]})")
            else:
                print("Tokio draugelio nera")
        print("Buy!")
=======
connector = sqlite3.connect("data/zmones.db")
cursor = connector.cursor()

with connector:
    while True:
        vardas = input("Įveskite vardą arba ! kad išeiti, arba . kad įvesti naują: ")
        if vardas == "!":
            break
        elif vardas == ".":
            print("--- NAUJAS draugelis ---")
            naujas_vardas = input("Vardas: ")
            nauja_pavarde = input("Pavardė: ")
            naujas_email = input("E-mail: ")
            cursor.execute('INSERT INTO draugai (first_name, last_name, email) VALUES (?, ?, ?)', 
                (naujas_vardas, nauja_pavarde, naujas_email, ))
            connector.commit()
        else:
            select_query = 'SELECT * FROM draugai WHERE first_name LIKE ?'
            # print(f'... vykdome {select_query} ...')
            cursor.execute(select_query, (f'%{vardas}%', ))
            rezultatas = cursor.fetchall()
            if rezultatas:
                print("Radau tokius draugelius:")
                for draugas in rezultatas:
                    print(f"- {draugas[0]} {draugas[1]} ({draugas[2]})")
            else:
                print("Tokio draugelio nėra")
    print("Bye!")
>>>>>>> 91f25d7504bbd38e8322a9ceb58fcce029f6777e

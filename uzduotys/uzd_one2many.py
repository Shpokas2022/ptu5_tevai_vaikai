from sqlalchemy.orm import sessionmaker
from pprint import pprint
from uzd_12m_modelis import engine, Zmogus, Saskaita, Bankas

session = sessionmaker(bind=engine)()

def create_zmogus(f_name, s_name, kodas, telefonas):
    zmogus = Zmogus(f_name=f_name, s_name=s_name, kodas=kodas, telefonas=telefonas)
    session.add(zmogus)
    session.commit()
    return zmogus

def read_zmones():
    zmones = session.query(Zmogus).all()
    return zmones

def create_account(iban, balansas, zmogus_id):
    account = Saskaita(iban = iban, balansas=balansas, zmogus_id=zmogus_id)
    session.add(account)
    session.commit()
    return account

def read_account():
    accounts = session.query(Saskaita).all()
    return accounts

def create_bank(pavadinimas, adresas, banko_kodas, swift):
    bankas = Bankas(pavadinimas=pavadinimas, adresas=adresas, banko_kodas=banko_kodas, swift=swift)
    session.add(bankas)
    session.commit()
    return bankas

def read_bank():
    bankai = session.query(Bankas).all()
    return bankai

while True:
    pasirinkimas = int(input("1 - įveskite vartotoją\n2 - įveskite banką\n3 - įveskite sąskaitą\n4 - įveskite pajamas/išlaidas\n6 - peržiūrėti vartotojus\n7 - peržiūrėti bankus\n8 - peržiūrėti sąskaitas\n9 - išeiti iš programos"))
    if pasirinkimas == 1:
        f_name = input("Įveskite vardą: ")
        s_name = input("Įveskite pavardę: ")
        kodas = int(input("Įveskite asmens kodą: "))
        telefonas = input("Įveskite telefona: ")
        asmuo = create_zmogus(f_name, s_name, kodas, telefonas)

    if pasirinkimas == 2:
        pavadinimas = input("Įveskite banko pavadinimą: ")
        adresas = input("Įveskite adresą: ")
        banko_kodas = input("Įveskite banko kodą: ")
        swift = input("Įveskite SWIFT kodą: ")
        bankas = create_bank(pavadinimas, adresas, banko_kodas, swift)
    #     session.add(bankas)
    #     session.commit()
    if pasirinkimas == 3:
        iban = input("Įveskite sąskaitos numerį")
        balansas = 0
        vartotojai = session.query(Zmogus).all()
        for vartotojas in vartotojai:
            print(vartotojas)
        zmogus_id = int(input("Pasirinkite vartotojo ID: "))
        bankai = session.query(Bankas).all()
        for vienas in bankai:
            print(vienas)
        bank_id = int(input("Pasirinkite banko ID: "))
        saskaita = create_account(iban, balansas, zmogus_id)
    #     saskaita = Saskaita(numeris=numeris, balansas=balansas, asmuo_id=vartotojo_id, bankas_id=banko_id)
    #     session.add(saskaita)
    #     session.commit()
    if pasirinkimas == 4:
        saskaitos = session.query(Saskaita).all()
        for viena in saskaitos:
            print(viena)
        saskaitos_id = int(input("Pasirinkite sąskaitos ID"))
        pasirinkta_saskaita = session.query(Saskaita).get(saskaitos_id)
        irasas = float(input("Įveskite pajamas/išlaidas (su -)"))
        pasirinkta_saskaita.balansas += irasas
        session.commit()
    if pasirinkimas == 6:
        vartotojai = read_zmones()
        # for vartotojas in vartotojai:
        pprint(vartotojai)
    if pasirinkimas == 7:
        bankai = read_bank()
        # for vienas in bankai:
        pprint(bankai)
    if pasirinkimas == 8:
        saskaitos = read_account()
        # for viena in saskaitos:
        pprint(saskaitos)
    if pasirinkimas == 9:
        print("Programa baigta")
        break

# if __name__ == "__main__":
#     naujas_zmogus = create_zmogus(
#         "Jonas", "Jurgutis",
#         39509140124,
#         "37069800000",
#         )
    
#     naujas_bankas = create_bank(
#         "Swedbank", "Luksio g. 5, Vilnius", "73000", "HABAL"
#     )

#     nauja_saskaita = create_account(
#         "LT7300031213564659", "4500.00", "Swedbank"
#     )
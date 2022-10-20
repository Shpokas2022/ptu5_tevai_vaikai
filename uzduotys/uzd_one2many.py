from sqlalchemy.orm import sessionmaker
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

def create_account(iban, balansas, name):
    account = Saskaita(iban = iban, balansas=balansas, name=name)
    session.add(account)
    session.commit()
    return account

def create_bank(pavadinimas, adresas, banko_kodas, swift):
    bankas = Bankas(pavadinimas=pavadinimas, adresas=adresas, banko_kodas=banko_kodas, swift=swift)
    session.add(bankas)
    session.commit()
    return bankas

if __name__ == "__main__":
    naujas_zmogus = create_zmogus(
        "Petras", "Krasauskas",
        38409040164,
        "37069800000",
        )
from sqlalchemy.orm import sessionmaker
from modelis import engine, Tevas, Vaikas

session = sessionmaker(bind=engine)()

def create_tevas(vardas, pavarde):
    tevas = Tevas(vardas=vardas, pavarde=pavarde)
    session.add(tevas)
    session.commit()
    return tevas

def delete_object(object_class, object_id):
    obj = session.query(object_class).get(object_id)
    if obj:
        session.delete(obj)
        session.commit()
        return True
    else:
        print(f"KLaida: {object_class.__name__} su ID: {object_id} neegzistuoja")

def update_object(object_class, object_id, **kwargs):
    obj = session.query(object_class).get(object_id)
    if obj and kwargs:
        for column_name, value in kwargs.items():
            if hasattr(obj, column_name):
                setattr(obj, column_name, value)
            else:
                print(f"Klaida: {obj} neturi {column_name} atributo")
        else:
            session.commit()
            return obj
    else:
        print(f"Klaida: {object_class.__name__} su ID: {object_id} neegzistuoja") 


# def delete_tevas(tevas_id):
#     tevas = session.query(Tevas).get(tevas_id)
#     if tevas:
#         session.delete(tevas)
#         session.commit()
#         return True
#     else:
#         print(f"Klaida: Tevas su ID:{tevas_id} neegzistuoja")


def read_tevai():
    tevai = session.query(Tevas).all()
    return tevai

def create_vaikas(vardas, pavarde, tevas, mokymo_istaiga=None):
    vaikas = Vaikas(
        vardas=vardas,
        pavarde=pavarde,
        tevas=tevas, 
        mokymo_istaiga=mokymo_istaiga
    )
    session.add(vaikas)
    session.commit()
    return vaikas

def read_vaikai():
    return session.query(Vaikas).all()

# Testuojame
if __name__ == "__main__":


# IVAIKINIMO SCENARIJUS

    vaikas = session.query(Vaikas).filter(Vaikas.pavarde.ilike("Vai%")).first()
    tevas = session.query(Tevas).filter(Tevas.pavarde.ilike("Vas%")).first()
    ivaikintas = update_object(Vaikas, vaikas.id, tevas=tevas, vardas="Ivaikintas")
    print("Python objektas 'ivaikintas':\n", ivaikintas)
    print("perkraunam is DB:\n", read_vaikai())
# ==== SUKURIAME SUPERINE ŠEIMĄ
# Naujas tevas

    # naujas_tevas = create_tevas("Niekam", "Tikes")
    # naujas_vaikas = create_vaikas("Super", "Vaikas", naujas_tevas)
    # delete_object(Tevas, naujas_tevas.id)


    # print(naujas_tevas.id, naujas_tevas.vardas, naujas_tevas.pavarde)
# Atnaujintas Tevas
    # update_tevas(1, vardas = "Darius", pavarde="Vasionis")
    # print(delete_tevas(2))
    # tevas = session.query(Tevas).get(1)
    # naujas_vaikas = create_vaikas("Emilija", "Vainiūtė", 
    # tevas, "Saulės gimnazija")
    # print(read_vaikai())
    # print(read_tevai())

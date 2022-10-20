from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///data/zmones_bankai.db')
Base = declarative_base()

class Zmogus(Base):
    __tablename__ = "zmogus"
    id = Column(Integer, primary_key=True)
    f_name = Column("Vardas", String)
    s_name = Column("Pavarde", String)
    kodas = Column("Asmens_kodas", Integer)
    telefonas = Column("Telefonas", String)
    accounts = relationship("Saskaita", back_populates="zmogus")

    def __repr__(self):
        return f"({self.id}, {self.f_name}, {self.s_name}, {self.kodas}, {self.telefonas})"

class Saskaita(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    iban = Column("Saskaita", String)
    balansas = Column("Balansas", Integer)
    name = Column("Pavadinimas", String)
    # ForeignKey veda į lentelės pavadinimą
    zmogus_id = Column("zmogus_id", Integer, ForeignKey("zmogus.id"))
    bank_id = Column("bank_id", Integer, ForeignKey('bank.id')) 
# Relationship veda į objekto pavadinimą
    zmogus = relationship("Zmogus", back_populates="accounts")
    bank = relationship("Bankas", back_populates="accounts")
    
    def __repr__(self):
        return f"({self.id}, {self.iban}, {self.balansas}, {self.name})"


class Bankas(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    adresas = Column("Adresas", String)
    banko_kodas = Column("Kodas", String, nullable=True)
    swift = Column("SWIFT", String, nullable=True)
    accounts = relationship("Saskaita", back_populates="bank")

    def __repr__(self):
        return f"({self.id}, {self.pavadinimas}, {self.banko_kodas}, {self.swift}, {self.adresas})"

if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
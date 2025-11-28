from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, JSON, ForeignKey, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import json

Base = declarative_base()

# Association tables for many-to-many relationships
pokemon_attacks = Table(
    'pokemon_attacks',
    Base.metadata,
    Column('pokemon_id', Integer, ForeignKey('pokemon.id')),
    Column('attack_id', Integer, ForeignKey('ataque.id'))
)

pokemon_abilities = Table(
    'pokemon_abilities',
    Base.metadata,
    Column('pokemon_id', Integer, ForeignKey('pokemon.id')),
    Column('habilidad_id', Integer, ForeignKey('habilidad.id'))
)

pokemon_species = Table(
    'pokemon_species_rel',
    Base.metadata,
    Column('pokemon_id', Integer, ForeignKey('pokemon.id')),
    Column('especie_id', Integer, ForeignKey('pokemon_especie.id'))
)

class Ataque(Base):
    __tablename__ = 'ataque'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(Text)
    potencia = Column(Integer)
    precision = Column(Integer)
    pp = Column(Integer)
    tipo = Column(String(50))
    
    def __repr__(self):
        return f"<Ataque(nombre='{self.nombre}', potencia={self.potencia}, tipo='{self.tipo}')>"

class Habilidad(Base):
    __tablename__ = 'habilidad'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(Text)
    efecto = Column(String(255))
    
    def __repr__(self):
        return f"<Habilidad(nombre='{self.nombre}')>"

class PokemonEspecie(Base):
    __tablename__ = 'pokemon_especie'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    tipo = Column(String(50))
    rango_genero = Column(Float)
    es_bebe = Column(Boolean, default=False)
    es_legendario = Column(Boolean, default=False)
    es_mitico = Column(Boolean, default=False)
    generacion = Column(Integer)
    habitat = Column(String(100))
    imagen = Column(String(255))
    atributos = Column(JSON)
    fuerte_contra = Column(JSON)
    debil_contra = Column(JSON)
    cadena_evolucion = Column(JSON)
    
    def __repr__(self):
        return f"<PokemonEspecie(nombre='{self.nombre}', tipo='{self.tipo}')>"

class Pokemon(Base):
    __tablename__ = 'pokemon'
    
    id = Column(Integer, primary_key=True)
    id_pokemon = Column(Integer, unique=True)
    altura = Column(Float)
    color = Column(String(50))
    atributos = Column(JSON)
    peso = Column(Float)
    lista_habilidades = Column(JSON)
    lista_ataques = Column(JSON)
    especie = Column(String(100), ForeignKey('pokemon_especie.nombre'))
    
    # Relationships
    ataques = relationship("Ataque", secondary=pokemon_attacks, backref="pokemons")
    habilidades = relationship("Habilidad", secondary=pokemon_abilities, backref="pokemons")
    
    def __repr__(self):
        return f"<Pokemon(id_pokemon={self.id_pokemon}, especie='{self.especie}')>"

class Pokedex(Base):
    __tablename__ = 'pokedex'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    lista_pokemon_especie = Column(JSON)
    
    def __repr__(self):
        return f"<Pokedex(nombre='{self.nombre}')>"

class Entrenador(Base):
    __tablename__ = 'entrenador'
    
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(100), unique=True, nullable=False)
    es_admin = Column(Boolean, default=False)
    es_aprobado = Column(Boolean, default=False)
    fecha_registro = Column(String(50))
    ciudad = Column(String(100))
    nombre = Column(String(100))
    numero = Column(String(20))
    
    def __repr__(self):
        return f"<Entrenador(nombre_usuario='{self.nombre_usuario}', nombre='{self.nombre}')>"

class Equipo(Base):
    __tablename__ = 'equipo'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    lista_pokemon = Column(JSON)
    entrenador_id = Column(Integer, ForeignKey('entrenador.id'))
    fecha_creacion = Column(String(50))
    
    def __repr__(self):
        return f"<Equipo(nombre='{self.nombre}', entrenador_id={self.entrenador_id})>"

# Database connection
def get_database_engine(db_path='pokemon.db'):
    """Create database engine and return it"""
    engine = create_engine(f'sqlite:///{db_path}', echo=False)
    return engine

def create_tables(engine):
    """Create all tables in the database"""
    Base.metadata.create_all(engine)
    print("Database tables created successfully!")

def get_session(engine):
    """Create and return a database session"""
    Session = sessionmaker(bind=engine)
    return Session()

def close_session(session):
    """Close database session"""
    session.close()

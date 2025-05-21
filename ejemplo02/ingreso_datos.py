from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

# se importa la clase(s) del archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se genera enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Cargar datos desde los archivos
data_clubs = pd.read_csv("./data/datos_clubs.txt", delimiter=';', names=["nombre", "deporte", "fundacion"]) #data de los clubs 
data_jugadores = pd.read_csv("./data/datos_jugadores.txt", delimiter=';', names=["nombre_club", "posicion", "dorsal", "nombre"]) #data de los jugadores

# Ingresar los clubs
for index, row in data_clubs.iterrows():
    club = Club()
    club.nombre = row["nombre"]
    club.deporte = row["deporte"]
    club.fundacion = int(row["fundacion"])
    session.add(club)

# Ingresar los jugadores
for index, row in data_jugadores.iterrows():
    jugador = Jugador()
    jugador.nombre = row["nombre"]
    jugador.dorsal = int(row["dorsal"])
    jugador.posicion = row["posicion"]

    club = session.query(Club).filter_by(nombre=row["nombre_club"]).one_or_none()
    if club:
        jugador.club = club
        session.add(jugador)
    else:
        print("No tiene equipo")
        
# Confirmar las transacciones
session.commit()

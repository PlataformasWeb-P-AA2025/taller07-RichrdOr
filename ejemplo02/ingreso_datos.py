from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

data_clubs = pd.read_csv("./data/datos_clubs.txt", delimiter =';', nombres = ["nombre", "deporte", "fundacion"]) #Ruta del csvs que tiene informacion de los clubs

data_jugadores = pd.read_csv("./data/datos_jugadores.txt", delimiter =';', nombres = ["nombre_club", "posicion", "dorsal", "nombre"]) # Ruta del csv que tiene informacion de los jugadores


for e in data_clubs.iterrows():
    club = Club()
    club.nombre 
    club.deporte 
    club.fundacion 
    session.add(club)

for j in data_jugadores.iterrows():
    jugador = Jugador()
    jugador.nombre 
    jugador.dorsal 
    jugador.posicion
    session.add(jugador)

# se confirma las transacciones
session.commit()
    

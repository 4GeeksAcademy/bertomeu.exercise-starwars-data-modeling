import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, primary_key=True)
    userName = Column(String(25), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)

class CharacterFavorite(Base):
    __tablename__ = 'characterFavorite'
    characterFavoriteId = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.userId'))
    user = relationship(User)

class PlanetFavorite(Base):
    __tablename__ = 'planetFavorite'
    planetFavoriteId = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.userId'))
    user = relationship(User)

class VehicleFavorite(Base):
    __tablename__ = 'vehicleFavorite'
    vehicleFavoriteId = Column(Integer, primary_key=True) 
    userId = Column(Integer, ForeignKey('user.userId'))
    user = relationship(User)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    characterId = Column(Integer, primary_key=True)
    name = Column(String(25))
    species = Column(String(25))
    gender = Column(String(25))
    height = Column(Integer)
    weight = Column(Integer)
    age = Column(Integer)
    characterFavoriteId = Column(Integer, ForeignKey('characterFavorite.characterFavoriteId'))
    characterFavorite = relationship(CharacterFavorite)

class Planets(Base):
    __tablename__ = 'planets'
    planetId = Column(Integer, primary_key=True)
    name = Column(String(25))
    population = Column(Integer)
    diameter = Column(Integer)
    rotationPeriod = Column(Integer)
    orbitaPeriod = Column(Integer)
    climate = Column(String(25))   
    planetFavoriteId = Column(Integer, ForeignKey('planetFavorite.planetFavoriteId'))
    planetFavorite = relationship(PlanetFavorite)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    vehicleId = Column(Integer, primary_key=True) 
    name = Column(String(25))
    vehicleClass = Column(String(25))
    model = Column(String(25))
    passengers = Column(Integer)
    loadCapacity = Column(Integer)
    vehicleFavoriteId = Column(Integer, ForeignKey('vehicleFavorite.vehicleFavoriteId'))
    vehicleFavorite = relationship(VehicleFavorite) 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

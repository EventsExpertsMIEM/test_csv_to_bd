from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from numpy import genfromtxt
from time import time

from sqlalchemy import (Column, Integer, String, ForeignKey,
                        DateTime, Boolean, UniqueConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import ENUM, UUID

from datetime import datetime
import uuid

import csv
import pandas as pd


Base = declarative_base()


# таблицы для научных отраслей
# таблицы для научных отраслей
class Scientific_area(Base):
    __tablename__ = 'Scientific_areas'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)


class Scientific_area_additional(Base):
    __tablename__ = 'Scientific_areas_additional'

    area_id = Column(Integer, ForeignKey(
        'Scientific_areas.id'), nullable=False)
    id = Column(String, primary_key=True)
    full_name = Column(String, nullable=False)


# таблицы для специальности высшего образования
class Specialities_of_higher_education(Base):
    __tablename__ = 'Spec_of_h_ed'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)


class SOHE_bakalavriat(Base):
    __tablename__ = 'SOHE_b'

    area_id = Column(Integer, ForeignKey(
        'Spec_of_h_ed.id'), nullable=False)
    id = Column(String, primary_key=True)
    full_name = Column(String, nullable=False)


class SOHE_magistratura(Base):
    __tablename__ = 'SOHE_m'

    area_id = Column(Integer, ForeignKey(
        'Spec_of_h_ed.id'), nullable=False)
    id = Column(String, primary_key=True)
    full_name = Column(String, nullable=False)


class SOHE_aspirantura(Base):
    __tablename__ = 'SOHE_aspir'

    area_id = Column(Integer, ForeignKey(
        'Spec_of_h_ed.id'), nullable=False)
    id = Column(String, primary_key=True)
    full_name = Column(String, nullable=False)


class SOHE_assistentura(Base):
    __tablename__ = 'SOHE_assis'

    area_id = Column(Integer, ForeignKey(
        'Spec_of_h_ed.id'), nullable=False)
    id = Column(String, primary_key=True)
    full_name = Column(String, nullable=False)


engine = create_engine('sqlite:///testbase.db')
Base.metadata.create_all(engine)


list_of_csv_files = ('Scientific_areas.csv',
                     'Specialities_of_higher_education.csv')
list_of_csv_add_files = ('Scientific_areas_add.csv',
                         'SOHE_bakalavriat.csv', 'SOHE_magistratura.csv', 'SOHE_aspirantura.csv', 'SOHE_assistentura.csv')
list_of_tables = ('Scientific_areas', 'Spec_of_h_ed', )
list_of_add_tables = ('Scientific_areas_additional',
                      'SOHE_b', 'SOHE_m', 'SOHE_aspir', 'SOHE_assis')

for csv, table in zip(list_of_csv_files, list_of_tables):
    df = pd.read_csv(csv, sep=';')
    df.to_sql(table, con=engine, index_label='id',
              index=False, if_exists='replace')

for csv, table in zip(list_of_csv_add_files, list_of_add_tables):
    df = pd.read_csv(csv, sep=';')
    df.to_sql(table, index_label='id', index=False,
              con=engine, if_exists='replace')

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


Level = ENUM('b', 'm', 's', 'ap', 'as',
             name='level')


class SOHE_additional(Base):
    __tablename__ = 'SOHE_additional'

    area_id = Column(Integer, ForeignKey(
        'Spec_of_h_ed.id'), nullable=False)
    level = Column(Level, nullable=False)
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)


engine = create_engine('sqlite:///testbase.db')
Base.metadata.create_all(engine)

# main tables
list_of_csv_files = ('Scientific_areas.csv',
                     'Specialities_of_higher_education.csv')
list_of_tables = ('Scientific_areas', 'Spec_of_h_ed', )

for csv, table in zip(list_of_csv_files, list_of_tables):
    df = pd.read_csv(csv, sep=';')
    df.to_sql(table, con=engine, index_label='id',
              index=False, if_exists='replace')

# additional tables
df = pd.read_csv('Scientific_areas_add.csv', sep=';')
df.to_sql('Scientific_areas_additional', con=engine, index_label='id',
          index=False, if_exists='replace')

df = pd.read_csv('SOHE_additional.csv', sep=';')
df.to_sql('SOHE_additional', con=engine, index_label='id',
          index=False, if_exists='replace')

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
class Scientific_area(Base):
    __tablename__ = 'Scientific_areas'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)


engine = create_engine('sqlite:///testbase.db')
Base.metadata.create_all(engine)
file_name = 'Scientific_area.csv'
df = pd.read_csv(file_name, sep=';')
df.to_sql('Scientific_areas', con=engine, index_label='id',
          index=True, if_exists='replace')


import os

from src.Sources.S1 import S1

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DIR  = os.path.join(PROJECT_DIR,'source_data')
TARGET_DIR  = os.path.join(PROJECT_DIR,'target_data')
ETL_DIR  = os.path.join(PROJECT_DIR,'ETL')


SQLITE_DB_FILE = os.path.join(PROJECT_DIR,'DB','outreach.sqlite.db')

TARGET_CLASS_MAP = \
{
    "S1" : S1
    
}

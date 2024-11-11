import os
import pytest

from config import PROJECT_DIR
from src.db import OutreachDB

DB_TEST_SQLS_DIR = os.path.join(PROJECT_DIR, 'tests','db_test_sqls')

@pytest.fixture
def db():
    return OutreachDB()

def test_execute_sql_from_file(db):
    sql_file = os.path.join(DB_TEST_SQLS_DIR,'test_1.sql')
    assert db.execute_sql_from_file(sql_file)
    
# def test_execute_sql_from_file(db):
#     sql_file = os.path.join('ETL','DDLs','create_S1.sql')
#     assert db.execute_sql_from_file(sql_file)
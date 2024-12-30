import sqlalchemy
from sqlalchemy import MetaData, Table
from sqlalchemy.sql.schema import Table, Column
from sqlalchemy.types import Integer, String, Unicode, Float

from teradatasqlalchemy.dialect import TDCreateTablePost

from sqlalchemy.schema import CreateTable

metadata = MetaData()


def create_all(engine):
    metadata.create_all(engine)


def drop_all(engine):
    try:
        metadata.drop_all(engine)
    except e:
        pass


def show_table(engine, table_name):
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text(f"SHOW TABLE {table_name}"))
        return '\n'.join([row[0].replace('\r', '\n') for row in result])


#
# 以下にテーブル定義を追記していく
#

iris = Table(
    "iris", metadata,
    Column("idx", Integer, nullable=False, comment="Unique ID"),
    Column("sepallength", Float, nullable=False, comment='sepal length (cm)'),
    Column("sepalwidth", Float, nullable=False, comment='sepal width (cm)'),
    Column("petallength", Float, nullable=False, comment='petal length (cm)'),
    Column("petalwidth", Float, nullable=False, comment='petal width (cm)'),
    Column("target", Unicode(256), nullable=False, comment='Target'),
    prefixes=['SET'],
    teradatasql_post_create=TDCreateTablePost().primary_index(unique=True, cols=["idx"]),
)

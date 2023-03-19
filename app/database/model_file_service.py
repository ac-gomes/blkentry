import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class FileTableModel(Base):
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_brand = Column(String(100), index=True)
    category = Column(String(100), index=True)
    sub_category= Column(String(100), index=True)
    created_dt = Column(DateTime, default=datetime.datetime.utcnow)




# #chatGPT
# def create_table(table_name, columns):
#     class DynamicTable(Base):
#         __tablename__ = table_name
#         id = Column(Integer, primary_key=True, autoincrement=True)
#         __table_args__ = {'extend_existing': True}

#         def __init__(self, **kwargs):
#             for col in columns:
#                 setattr(self, col, kwargs.get(col))

#     return DynamicTable

# # Cria uma tabela chamada 'my_table' com as colunas 'name' e 'age'
# MyTable = create_table('my_table', ['name', 'age'])
# # Cria uma tabela chamada 'users' com as colunas 'username' e 'email'
# UsersTable = create_table('users', ['username', 'email'])

# # Cria uma tabela chamada 'products' com as colunas 'product_name' e 'price'
# ProductsTable = create_table('products', ['product_name', 'price'])
import os
from m_libls import m_sqlite

sql = m_sqlite.sqlile_db(path="simulator.db")
sql.close_connetion()

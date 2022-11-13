import os
from m_libls import m_sqlite
from pprint import pprint


def generate_data ():
    sql.add_prhase(value_en = 'dog', 
                value_ru = 'собака')
    sql.add_prhase(value_en = 'Hello World', 
                value_ru = 'Привет Мир')
    sql.add_prhase(value_en = 'I suppose', 
                value_ru = 'Я предполагаю')
    sql.add_prhase(value_en = "I'd like to point out that it isn't enough", 
                value_ru = "Я хотел бы заметить, что этого не достаточно")
    sql.add_prhase(value_en = "Let me point out that we can't achieve success without hard work", 
                value_ru = "Позволь мне заметить что, мы не можем достичь успеха без усердной работы")
    sql.add_prhase(value_en = "I would like to point out that it's extremely important", 
                value_ru = "Я бы хотел заметить, что это чрезвычайно важно")    

# sql = m_sqlite.sqlile_db(path="simulator.db")
sql = m_sqlite.sqlile_db(path="test.db")

data = sql.get_all_phrases()
pprint (data)
sql.export_data()

sql.close_connetion()

import os
from m_libls.data import SqlileDb, ImportPhrasesFile
from pprint import pprint

def initial ():
    if not os.path.exists('databases'): os.mkdir('databases')
    sql = SqlileDb(path=f"databases/simulator.db")
    import_phrases_file = ImportPhrasesFile()
    # sql = m_sqlite.SqlileDb(path="test.db")
    
    return (sql,import_phrases_file)

def generate_data (sql):
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

######################################################################################################   

(sql,import_phrases_file) = initial ()

# generate_data(sql=sql)
data = sql.get_all_phrases()
sql.export_data()
import_phrases_file.data()

sql.close_connetion()
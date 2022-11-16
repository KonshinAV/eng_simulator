import os
from m_libls.m_data import SqlileDb, ImportPhrasesFile
import json

class Lesson:
    def __init__(self) -> None:
        if not os.path.exists('modules'): os.mkdir('modules')
        
        # modules = []
        # for module in os.listdir('modules'):
        #     db_module=SqlileDb(path=module)
        #     modules.append ({str(module).split(".")[0]:db_module})
        modules = {}
        for module in os.listdir('modules'):
            db_module = SqlileDb(path=f"modules/{module}")
            modules[str(module.split(".")[0])] = db_module
        self.all_modules_list = modules
    
        self.import_xlsx_file = ImportPhrasesFile()
    
    def all_modules (self):
        
        return self.all_modules_list

    def create_module (self, name):
        db_module = SqlileDb(path=f"modules/{name}.db")
        pass   
    
    def delete_module (self):
        pass
    
    def import_phrases_into_module (self, module_name):
        # print (self.all_modules_list[module_name].get_all_phrases())
        # print (self.import_xlsx_file.data()) 
        for record in self.import_xlsx_file.data():
            self.all_modules_list[module_name].add_prhase(value_en=record['en'],
                                                          value_ru=record['ru'])
        # print(import_xlsx_file.data())
        pass
    
    def export_phrases_from_module (self, module_name):
        pass
    
    

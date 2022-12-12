import os
from m_libls.m_data import SqlileDb, ImportPhrasesFile
import json
from termcolor import colored, cprint
import random
from pprint import pprint
import csv

def clear_screen ():
    print("\033[H\033[J")

class Lesson:
    def __init__(self) -> None:
        if not os.path.exists('modules'): os.mkdir('modules')
    
        self.all_modules_list = self.get_all_modules()
        self.import_xlsx_file = ImportPhrasesFile()
        self.current_module = None
    
    def get_all_modules (self):
        modules = {}
        for module in os.listdir('modules'):
            db_module = SqlileDb(path=f"modules/{module}")
            modules[str(module.split(".")[0])] = db_module
        self.all_modules_list = modules
        return self.all_modules_list
    
    def set_current_module (self, module_name):
        # print (self.all_modules_list)
        try:
            self.current_module = self.all_modules_list[module_name]
        except KeyError:
            cprint(f"[-] Module {module_name}, was not found", color="red")
            

    def create_module (self, module_name):
        db_module = SqlileDb(path=f"modules/{module_name}.db")
        cprint(f"[-] Module {module_name} has been created", color='blue')
        self.set_current_module(module_name=module_name)
        pass   
    
    def check_module_exists (self, module_name):
        if module_name in self.all_modules_list.keys():
            return True
        else:
            cprint(f">>> {module_name}, not found", color="red")
            return False
    
    def delete_module (self):
        pass
    
    def import_phrases_into_module (self, module_name, import_file=None):
        if import_file == None:    
            for record in self.import_xlsx_file.data():
                if record['en'] != None and record['ru'] != None:
                    self.all_modules_list[module_name].add_prhase(value_en=record['en'],
                                                                value_ru=record['ru'])
                else:
                    continue
        else:
            with open(import_file, encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                list_phrases = [row for row in reader]
            for record in list_phrases: 
                self.all_modules_list[module_name].add_prhase(date_create=record['phrases.date_create'],
                                                              date_update=record['phrases.date_update'],
                                                              knowledge_level=int(record['phrases.knowledge_level']),
                                                              attemtps_count=int(record['phrases.appemtps_count']),
                                                              date_last_attempt=None,
                                                              mistakes_count=None,
                                                              value_en=record['en.en_value'],
                                                              value_ru=record['ru.ru_value'])
            pass
        
    
    def export_phrases_from_module (self, 
                                    module_name = None, 
                                    export_file_path='default.csv'):
        if export_file_path == 'default.csv': export_file_path = f"export_data.csv"
        if module_name == None:
            self.current_module.export_data(file_path = export_file_path)
        else:    
            self.all_modules_list[f"{module_name}"].export_data(file_path = export_file_path)
        cprint (f"[-] Data of module {module_name} has been exported to file: {export_file_path}", color='blue')
    
    def practice (self, module_name=None):
        
        try:
            module = self.current_module if module_name is None else self.all_modules_list[f"{module_name}"]
        except KeyError:
            cprint(f">>> {module_name}, not found", color="red")
        # if module_name == None:
        #     module = self.current_module
        # else:
        #     module = self.all_modules_list[f"{module_name}"]
        
               
        phrases = module.get_all_phrases()['data']
        random_phrases = random.sample(phrases, len(phrases))
        
        clear_screen()
        cprint (f'Start module {module_name}', color='yellow')
        mistake = False
        
        for ind, phrase in enumerate (random_phrases):
            ru =  str(phrase['ru.ru_value'])
            en = str(phrase['en.en_value'])
            ind = ind + 1
            len_of_prases = len(phrases)
            
            answer = input(f"{ind} of {len_of_prases}: {ru}\t >>> \n")
            if answer.lower().strip().replace('’', "'").replace(',',"").replace('.',"") == \
                en.lower().strip().replace('’', "'").replace(',',"").replace('.',""):
                cprint (f"Correct", color='green')
                mistake = False
            else:
                cprint (f"{en}", color='red')
                mistake = True
                
            module.update_phrase_because_attempt(phrase['phrases.id'], mistake)
            mistake = False
    
        
           
        
    
    

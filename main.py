import os
from m_libls.m_data import SqlileDb, ImportPhrasesFile
from m_libls.m_lesson import Lesson
from pprint import pprint


######################################################################################################   

lesson = Lesson()
module_name = 'B2'
# print (lesson.all_modules_list)
lesson.create_module(module_name = module_name)
lesson.set_current_module(module_name = module_name)
# lesson.import_phrases_into_module(module_name="B2")
# lesson.practice()
lesson.import_phrases_into_module(module_name = module_name, import_file='export_data.csv')
#pprint(lesson.get_all_modules()['Eng_PP_Phrasal_werbs'].get_all_phrases())



########################################################################################
# lesson.create_module(name='test')
# lesson.set_current_module(module_name='test')
# lesson.import_phrases_into_module('test')
# lesson.practice()

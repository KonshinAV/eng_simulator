import os
from m_libls.m_data import SqlileDb, ImportPhrasesFile
from m_libls.m_lesson import Lesson
from pprint import pprint


######################################################################################################   

lesson = Lesson()
# print (lesson.get_all_modules())
# lesson.import_phrases_into_module(module_name='test_2')
lesson.create_module('test')
# lesson.import_phrases_into_module('test')
lesson.set_current_module(module_name='test')
# print (lesson.all_modules_list.keys())cle
# print(lesson.check_module_exists(module_name='tsdfest'))
lesson.practice()

# print("\033[H\033[J") # Очистка экрана
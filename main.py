import os
from m_libls.m_data import SqlileDb, ImportPhrasesFile
from m_libls.m_lesson import Lesson
from pprint import pprint


######################################################################################################   

lesson = Lesson()
print (lesson.all_modules())
lesson.import_phrases_into_module(module_name='test_2')



# print("\033[H\033[J") # Очистка экрана
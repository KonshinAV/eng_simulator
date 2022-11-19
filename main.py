import os
from m_libls.m_data import SqlileDb, ImportPhrasesFile
from m_libls.m_lesson import Lesson
from pprint import pprint


######################################################################################################   

lesson = Lesson()
# print (lesson.get_all_modules())
lesson.create_module(name='test')
lesson.set_current_module(module_name='test')
lesson.import_phrases_into_module('test')

lesson.practice()

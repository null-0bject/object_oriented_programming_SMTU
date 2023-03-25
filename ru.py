'''
    Вы все делаете на свой страх и риск, при ошибках пишите либо мне - null.object, либо преподавателю, либо решайте сами.
    
    1. пройти по C:\Users\имяпользователя\AppData\Local\Programs\Python\Python(версияпайтона)\Lib\site-packages\rinoh\language
    2. Создать файл ru.py(либо скачать этот файл и вставить его в папку)
    3. скопировать код описанный ниже
    4. в этой же папке найти __init__.py
    5. в импорты вписать строчку
        from .ru import RU
    таким образом вы импротируете язык
    6. в свой config.py в то место, где у вас конфиги rinoh вписывайте
        rinoh.language.RU
    7. Проверяйте созданием PDF документа.



'''
from .cls import Language
from ..structure import SectionTitles, AdmonitionTitles


RU = Language('ru', 'Russian')

SectionTitles(
    contents='Содержание',
    list_of_figures='Список фигур',
    list_of_tables='Список таблиц',
    chapter='Глава',
    index='Индекс',
) in RU

AdmonitionTitles(
    attention='Внимание!',
    caution='Осторожно!',
    danger='!ОПАСНОСТЬ!',
    error='Ошибка',
    hint='Подсказка',
    important='Важно',
    note='Замечание',
    tip='Подсказка',
    warning='Предупреждение',
    seealso='Смотрите так же',
) in RU

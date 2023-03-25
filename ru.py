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

О лингвистической онтологии "Тезаурус РуТез"
============

Тезаурус РуТез представляет собой лингвистический ресурс концептуального типа, то есть представляет собой иерархическую сеть понятий, к которым приписаны текстовые выражения. И в этом смысле РуТез относится к тому же классу, что и тезаурус WordNet. При этом, в отличие от WordNet, который создавался как модель человеческой памяти (раздельное описание частей речи, специальные типы отношений и др.), тезаурус РуТез создавался именно как ресурс для автоматической обработки текстов.

Данный скрипт парсит версию тезауруса русского языка РуТез (далее РуТез-lite) с сайта http://www.labinform.ru/ruthes/index.htm. Версия тезауруса РуТез-lite выложена для бесплатного некоммерческого использования (лицензия типа Attribution-NonCommercial-ShareAlike 3.0 Unported, позволяющая копировать, изменять и некоммерчески использовать данную версию тезауруса). Данный скрипт распространяется по лицензии MIT.

Текущий объем тезауруса РуТез составляет 158 тысяч слов и выражений, уложенных в сеть 55 тысяч понятий, между которыми вручную установлено более 210 тысяч отношений. Особенностью тезауруса является то, что в течение многих лет он тестировался в реальных проектах.

Запуск
===========

Требуется scrapy 0.14, python-sqlite3. Запуск командой:

	scrapy crawl rutez

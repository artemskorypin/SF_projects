# Проблемы
Это файл описание воспроизводимости проекта. Файлы данных проекта большие, а интернет решил проверить меня на прочность. 
Что ж, для ясности картины я решил несколько описать процесс того, что я делал. 
Для воспроизводимости кода я настроил Virtualenv и заготовил файлы с версиями библиотек. Так что я думаю, не должно быть большого труда для его воссоздания.
[Данные](https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting/overview) проекта(все) также нужно будет скачать с сайта соревнования и разместить в папке data.

* $ python3 -m venv total_project
* $ pip install requirements.txt
* $ deactivate

Также отмечу, что в first_var.ipynb происходит основной анализ и работа с моделями, когда в var_2.ipynb рассматривается интересный вариант получения целевой переменной без моделей.

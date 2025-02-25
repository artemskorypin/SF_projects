# Итоговый проект первого года: Corporación Favorita Grocery Sales Forecasting
### Какой кейс решаем?
Поучавствуем в старом, но актуальном соревновании от [Kaggle](https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting/data)

Бизнес-задача: на основе предложенных данных спрогнозировать необходимое количество товара(ов) для магазина(ов).

### Описание данных
В этом конкурсе вам предстоит спрогнозировать продажи за единицу для тысяч товаров, проданных в различных магазинах Favorita, расположенных в Эквадоре. Данные обучения включают даты, информацию о магазине и товаре, продвигался ли этот товар, а также данные о продажах единиц продукции. Дополнительные файлы содержат дополнительную информацию, которая может быть полезна при создании ваших моделей.

### Описания файлов и информация о полях данных:

**train.csv:**
* Обучающие данные, которые включают целевую переменную unit_sales по параметрам date, store_nbr, и item_nbr и уникальную переменную id для маркировки строк.
* Целевое значение unit_sales может быть целым (например, упаковка чипсов) или дробным (например, 1,5 кг сыра).
* Отрицательные значения unit_sales представляют доходность этого конкретного товара.
* В столбце onpromotion указано, было ли item_nbr продвижение по службе для указанного date и store_nbr.
* Примерно 16% значений onpromotion в этом файле являются NaN.
* ПРИМЕЧАНИЕ: Обучающие данные не включают строки для товаров, у которых был нулевой unit_sales для комбинации «магазин/дата». Нет информации о том, был ли товар в наличии в магазине на эту дату, и командам нужно будет решить, как лучше поступить в такой ситуации. Кроме того, в обучающих данных есть небольшое количество товаров, которых нет в тестовых данных.

**test.csv**
* Тестовые данные с комбинациями date, store_nbr, item_nbr для прогнозирования, а также информация onpromotion
* ПРИМЕЧАНИЕ: в тестовых данных есть небольшое количество элементов, которых нет в обучающих данных. Часть упражнения будет заключаться в прогнозировании продаж нового товара на основе аналогичных продуктов.

**sample_submission.csv**
* Образец файла для отправки в правильном формате.

**stores.csv**
* Храните метаданные, включая city, state, type и cluster.
* cluster представляет собой группировку похожих магазинов.

**items.csv**
* Метаданные элемента, включая family, class и perishable.
* ПРИМЕЧАНИЕ: Элементы, отмеченные как perishable, имеют вес 1.25; в противном случае вес равен 1.0.

**transactions.csv**
* Количество транзакций продажи для каждой date, store_nbr комбинации. Учитывается только для периода обучения.

**oil.csv**
* Ежедневная цена на нефть. Включает значения как за период обучения, так и за период тестирования. (Эквадор — страна, зависящая от нефти, и её экономическое положение очень уязвимо к колебаниям цен на нефть.)

**holidays_events.csv**
* Праздники и события с метаданными
* ПРИМЕЧАНИЕ: Обратите особое внимание на колонку transferred. Выходной день, который transferred официально приходится на этот календарный день, но правительство перенесло его на другую дату. transferredДень больше похож на обычный день, чем на праздник. Чтобы найти день, в который он действительно отмечался, найдите соответствующую строку, где type находится Transfer. Например, праздник День независимости Гуаякиля был перенесён с 2012-10-09 на 2012-10-12, то есть он отмечался 12 октября 2012 года. Дополнительные дни Bridge — это дни, которые добавляются к празднику (например, чтобы продлить выходные). Они часто составляются по типу Work Day — это день, который обычно не предназначен для работы (например, суббота) и предназначен для погашения задолженности.
* Additional Праздничные дни — это дни, добавляемые к обычному календарному празднику, например, как это обычно происходит на Рождество (когда Сочельник становится праздником).

**Дополнительные Примечания**
* Заработная плата в государственном секторе выплачивается каждые две недели, 15-го числа и в последний день месяца. Это может повлиять на продажи в супермаркетах.
* 16 апреля 2016 года в Эквадоре произошло землетрясение магнитудой 7,8. Люди объединились для оказания помощи, жертвуя воду и другие товары первой необходимости, что сильно повлияло на продажи в супермаркетах в течение нескольких недель после землетрясения.

**Целевой признак:**
* unit_sales - необходимое колиство товара в магазине


### Файлы для соревнования

* наши данные распологаются [здесь](https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting/data)

**Наш проект включает в себя несколько этапов:**
* Первичная обработка данных
* Разведывательный анализ данных (EDA)
* Отбор и преобразование признаков
* Решение задачи регрессии подходящими моделями
* Решение задачи без моделей

**Что практикуем**     
* Учимся писать хороший код на python
* Учимся работать с IDE
* Учимся работать с GitHub
* Учимся строить и анализировать графики, находить взаимосвязи между признаками
* Учимся работать с данными
* Учимся строить модели
* Отрабатываем Docker и воспроизводимость кода

### Результаты:     
В ходе работы, был произведен анализ данных. На его основе попробовали построить различные модели, от самых простых до сложных. Был получен вполне не плохой результат, на разных моделях, правда нельзя сказать точно, что лучше, тк связь с сайтом подвела и получить значение метрики получилось не везде. Наиболее удачными моделями оказались KNN, логистическая регрессия, "легкая модель"(простые преобразования данных для конечного результата) и банальная вставка среднего значения. Если сосредоточиться на точности, то наиболее интересными будут 1 и 3 модели, последняя явно быстрее, но кто из них точнее сказать сложно. 

Что можно сказать еще? Проведение более глубокого анализа, вполне может натолкнуть на новые идеи. В том числе использование сезонных моделей, поидее должно дать хорошие результаты. Я эту сторону сильно не рассматривал, тк быстро получил переобучение и решил попытать счатье в другом. На мой взгляд оправдано, получились интересные результаты.

*Заметка на будущее: лучше проводить анализ в отдельном ноутбуке, тк большой массив данных снижает производительность. 

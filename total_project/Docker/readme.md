Что ж, здесь задумывался маленький докер для проекта. Так как время поджимало, а проблемы нас не покидали, пришлось сократить полет мысли.
Докер представляет собой контейнер, в котором просто запускается "модель" предсказания целевой переменной по медиане, в силу ее быстроты и "средней" точности.
[Данные](https://www.kaggle.com/competitions/favorita-grocery-sales-forecasting/overview) также нужно скачать с сайта, но уже не все, а только тренировочные и тестовые, и поместить их в папку data.

* $ docker build -t total_project .
* $ docker run -it --rm -v $PWD/src/:/usr/src/app/ --name products total_project
* $ docker run -it --rm --name=products total_project
  

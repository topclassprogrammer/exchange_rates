# Загрузка курсов валют из API в БД PostgreSQL

## Как развернуть проект

- склонировать текущий репозиторий: ```git clone https://github.com/topclassprogrammer/exchange_rates.git```
- перейти в папку проекта: ```cd exchange_rates```
- переименовать файл .env.example в .env: ```mv .env.example .env```
- в файле .env в поле API_KEY необходимо подставить свой API ключ, полученный на [этом сайте](exchangerate-api.com)
- в файле Dockerfile в поле ENTRYPOINT можно изменить аргумент с 60 секунд на любое другое число. Данный аргумент отвечает за периодичность обращения к API и загрузки курсов валют в базу данных 
- запустить контейнеры: ```docker-compose up -d```
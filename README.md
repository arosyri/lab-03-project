# lab-03-project
Цей репозиторій містить три проєкти, зроблені для лабораторної роботи:

## Python App
Папка: `python-app`  
Опис: простий Flask-застосунок  
Запуск:  
```bash
cd python-app
docker build -t python-app .
docker-compose up -d
```
## Go App
Папка: `go-app`
Опис: простий HTTP сервер на Go
Запуск:
```bash
cd go-app
docker build -t go-app .
docker-compose up -d
```
## Books App (Node.js + MongoDB)
Папка: ´books-app´
Опис: REST API для книг
Запуск:
```bash
cd books-app
docker build -t books-app .
docker-compose up -d
```

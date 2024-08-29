**Сервис для скачивания файлов с Яндекс диска при помощи публичных ссылок**</br>
![2024-08-29_14-05-34](https://github.com/user-attachments/assets/44812ba1-fc34-43ae-90d6-72791b16b8ac)

---

Попробовать:</br>
1. Клонировать проект
```
git clone git@github.com:al-ov73/yadisk_download.git && cd yadisk_download
```
2. Заполнить **web/.env** файл с адресом Api.</br>
*По умолчанию - http://127.0.0.1:8000/api/v1/*

3. Установить все зависимости
```
make docker-build
```
4. Запустить сервер с фронтендом на React
```
make docker-run
```
Сервис будет доступен по ссылке</br>
http://localhost:3000/</br>
Проверить можно на ссылках:</br>
Файл:
```
https://disk.yandex.ru/i/_1SvnxCdaE-7Qw
```
Приятная музыка:
```
https://disk.yandex.ru/d/_ZHUo1T9d7WsXg
```

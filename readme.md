# Программа "Заметки"

Данная программа предназначена для создания, просмотра и редактирования заметок. Заметки сохраняются в файл notes.csv.

## Структура notes.csv

Файл notes.csv представляет собой таблицу, каждая строка которой (за исключением первой - она является заголовком)
содержит одну заметку. Заметка состоит из четырех составляющих (выступают как столбцы таблицы): ID, название, текст
заметки, дата создания/изменения. При отсутствии файла функция просмотра заметок сообщит об отсутствии заметок, при
попытке создать новую заметку будет создан новый файл notes.csv.

### ID

Параметр ID генерируется каждый раз при создании новой заметки, является уникальным идентификатором и представляет
собой целочисленное значение типа integer. Создание ID основано на прочитывании всех существующих заметок, нахождении
наибольшего ID. Новый ID присваивается со значением наибольший ID + 1.

### Название и текст заметки

Название и текст заметки - обычные строки типа String.

### Дата изменения

Дата изменения (она же дата создания) - значение типа datetime. Присваивается каждый раз при изменении существующей
заметки, либо при создании новой.

## Просмотр заметок

Функция просмотра заметок доступна при наличии файла notes.csv. Возможен просмотр как всех заметок, так и сортировка их
по дате изменения.

## Создание заметок

При выполнении данной функции пользователю будет предложено ввести название и текст новой заметки. Автоматически будет
присвоен ID и дата создания. При отсутствии файла notes.csv он будет создан.

## Редактирование заметок

Данная функция доступна через меню выбора заметок. При выборе заметки пользователю будет предложено ввести ID
интересующей заметки, после чего при выборе функции редактирования будет предложено ввести новое название и текст. Дата
изменения будет изменена на текущую.

При вводе неверного ID заметки пользователь будет об этом уведомлен.

## Удаление заметок

Функция работает аналогичным образом, как и редактирование заметок, но вместо редактирования заметки удаляет ее.

_Автор: Андрей Александров_


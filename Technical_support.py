from dialog_bot_sdk.bot import DialogBot
from dialog_bot_sdk import interactive_media

import time
import grpc

import os

from dialog_bot_sdk.entities.media.ImageMedia import ImageLocation, ImageMedia
from dialog_bot_sdk.entities.message.TextMessage import MessageMedia




path = "Data/Technical support/Video/Pages/"
ext = ".mp4"
thx = "Через некоторое время будет отправлено видео,\nкоторое содержит ответ на Ваш вопрос.\nНадеюсь, оно будет полезным для Вас"
back = "Вернуться в главное меню?"
feedback = "Обратная связь"
feedbackScore = []

textPageArray = [
    "Формат документов",
    "Левая панель",
    "Правая панель",
    "Как выполнить предпросмотр документа перед печатью",
    "Как вставить изображение",
    "Как вставить изображение из интернета",
    "Как вставить фигуру",
    "Как создать таблицу",
    "Редактировать объекты",
    "Как вставить диаграмму в текст",
    "Как изменить диаграмму",
    "Работа с уравнениями",
    "Как изменить шрифт в тексте",
    "Как поменять межстрочные, межабзацные интервалы, отcтупы",
    "Дополнительные параметры",
    "Как создать маркированный список",
    "Как создать многоуровневый список",
    "Как создать нумерованный список",
    "Выравнивание текста",
    "Как создать новый стиль",
    "Как скопировать стиль",
    "Как вставить textart",
    "Совместная работа",
    "Отслеживание изменений",
    "Как защитить документ",
    "Горячие клавиши",
    "Как вставить гиперссылку на фрагмент в тексте",
    "Как вставить и настроить колонтитулы",
    "Как вставить нумерацию страниц",
    "Как поставить разрыв раздела",
    "Как создать колонки и отредактировать их",
    "Как воспользоваться проверкой на орфографию"]

tablesPageArray = [
    "Удаление строк столбцов",
    "Создать открыть таблицу",
    "Форматы для импорта экспорта",
    "Настройка ширины высоты таблиц",
    "Добавить изображение в ячейку",
    "Доступ только для чтения",
    "Работа с несколькими книгами",
    "Комментарии к ячейкам",
    "Защита таблицы",
    "Отобразить нулевые значения",
    "Работа с ячейками дата время",
    "Копия форматированных ячеек",
    "Выравнивание текста",
    "Формат числовых значений",
    "Разделительная линия",
    "Формат ячеек при помощи валюты",
    "Цвет и граница ячеек",
    "Настройка удобной таблицы",
    "Настройка шрифта",
    "Функция ВПР",
    "Удаление дубликатов",
    "Авто-скрытие пустых ячеек",
    "Условное форматирование",
    "Автозаполнение ячеек",
    "Расчет среднего значения",
    "Расширенные свойства ячейки",
    "Запуск макроса",
    "Выпадающий список",
    "Поиск и замена текста",
    "Форматирование сводной таблицы",
    "График на основе данных",
    "Смарт таблица"]



def exit_func(params):
    time.sleep(7)
    bot.messaging.send_message(params.peer, thx,
                               [interactive_media.InteractiveMediaGroup(
                                   [
                                       interactive_media.InteractiveMedia(
                                           str(79),
                                           interactive_media.InteractiveMediaButton("btn_79", back)
                                       ),
                                       interactive_media.InteractiveMedia(
                                           str(80),
                                           interactive_media.InteractiveMediaButton("btn_80", feedback)
                                       ),
                                   ]
                               )]
                               )

def start_func(params):

    bot.messaging.send_message(params.peer, "Добро пожаловать!\nЗдесь Вы найдете подробные ответы на все Ваши вопросы о Российском стеке ИТ-решений.\nЧтобы я смог точнее ответить на интересующий вас вопрос, \nподскажите, с каким продуктом он связан?",
                               [interactive_media.InteractiveMediaGroup(
                                   [
                                       interactive_media.InteractiveMedia(
                                           str(1),
                                           interactive_media.InteractiveMediaButton("btn_01", "Р7-Офис")
                                       ),
                                       interactive_media.InteractiveMedia(
                                           str(2),
                                           interactive_media.InteractiveMediaButton("btn_02", "Astra Linux")
                                       ),
                                       interactive_media.InteractiveMedia(
                                           str(3),
                                           interactive_media.InteractiveMediaButton("btn_03", "True Conf")
                                       )
                                   ]
                               )]
                               )
def question(params):
    bot.messaging.send_message(params.peer,
                               "Оцените, насколько вы удовлетворены удобством использования чат-ботом\n(где 1 – точно не удовлетворен, 6 – полностью удовлетворен)",
                               [interactive_media.InteractiveMediaGroup(
                                   [
                                       interactive_media.InteractiveMedia(
                                           str(103),
                                           interactive_media.InteractiveMediaButton("btn_103",
                                                                                    "1")
                                       ),
                                       interactive_media.InteractiveMedia(
                                           str(104),
                                           interactive_media.InteractiveMediaButton("btn_104",
                                                                                    "2")
                                       ),
                                       interactive_media.InteractiveMedia(
                                           str(105),
                                           interactive_media.InteractiveMediaButton("btn_105",
                                                                                    "3")
                                       ),
                                       interactive_media.InteractiveMedia(
                                           str(106),
                                           interactive_media.InteractiveMediaButton("btn_106",
                                                                                    "4")
                                       ),
                                       interactive_media.InteractiveMedia(
                                           str(107),
                                           interactive_media.InteractiveMediaButton("btn_107",
                                                                                    "5")
                                       ),
                                       interactive_media.InteractiveMedia(
                                           str(108),
                                           interactive_media.InteractiveMediaButton("btn_108",
                                                                                    "6")
                                       )
                                   ]
                               )]
                               )

def on_msg(params):
    mes = str(params.message.text_message.text)
    # if mes == "/start":
    if mes == "/start":
       start_func(params)

def on_click(params):
    peer = params.peer
    which_button = str(params.value)
    if which_button == "btn_01":
        bot.messaging.send_message(peer, "По какому конкретно продукту возник вопрос?",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(4),
                                               interactive_media.InteractiveMediaButton("btn_04",
                                                                                        "Текстовый редактор")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(5),
                                               interactive_media.InteractiveMediaButton("btn_05",
                                                                                        "Табличный редактор")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(6),
                                               interactive_media.InteractiveMediaButton("btn_6", "Редактор презентаций")
                                           )
                                       ]
                                   )]
                                   )
    elif which_button == "btn_02":
        bot.messaging.send_message(peer, "Раздел в разработке")
    elif which_button == "btn_03":
        bot.messaging.send_message(peer, "Раздел в разработке")
    elif which_button == "btn_04":
        bot.messaging.send_message(peer, "Выберите подраздел",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(7),
                                               interactive_media.InteractiveMediaButton("btn_07", "Основы")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(8),
                                               interactive_media.InteractiveMediaButton("btn_08", "Работа с объектами")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(9),
                                               interactive_media.InteractiveMediaButton("btn_09", "Работа с текстом")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(10),
                                               interactive_media.InteractiveMediaButton("btn_10", "Встроенный функционал")
                                           )
                                       ]
                                   )]
                                   )
    elif which_button == "btn_05":
        bot.messaging.send_message(peer, "Выберите подраздел",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(11),
                                               interactive_media.InteractiveMediaButton("btn_11", "Основные понятия")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(12),
                                               interactive_media.InteractiveMediaButton("btn_12", "Пользовательские форматы")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(13),
                                               interactive_media.InteractiveMediaButton("btn_13", "Встроенные функции")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(14),
                                               interactive_media.InteractiveMediaButton("btn_14", "Анализ данных")
                                           )
                                       ]
                                   )]
                                   )

    elif which_button == "btn_06":
        bot.messaging.send_message(peer, "Раздел в разработке")


    elif which_button == "btn_07":
        bot.messaging.send_message(peer, "Выберите интересующую тему",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(15),
                                               interactive_media.InteractiveMediaButton("btn_15", "Формат документов")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(16),
                                               interactive_media.InteractiveMediaButton("btn_16",
                                                                                        "Левая панель")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(17),
                                               interactive_media.InteractiveMediaButton("btn_17", "Правая панель")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(18),
                                               interactive_media.InteractiveMediaButton("btn_18", "Просмотр перед печатью")
                                           )
                                       ]
                                   )]
                                   )

    elif which_button == "btn_08":
        bot.messaging.send_message(peer, "Выберите интересующую тему",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(19),
                                               interactive_media.InteractiveMediaButton("btn_19", "Вставка изображения")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(20),
                                               interactive_media.InteractiveMediaButton("btn_20",
                                                                                        "Изображение из интернета")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(21),
                                               interactive_media.InteractiveMediaButton("btn_21", "Вставка фигуры")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(22),
                                               interactive_media.InteractiveMediaButton("btn_22",
                                                                                        "Создать таблицу")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(23),
                                               interactive_media.InteractiveMediaButton("btn_23", "Редактировать объекты")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(24),
                                               interactive_media.InteractiveMediaButton("btn_24",
                                                                                        "Вставить диаграмму")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(25),
                                               interactive_media.InteractiveMediaButton("btn_25", "Изменить диаграмму")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(26),
                                               interactive_media.InteractiveMediaButton("btn_26",
                                                                                        "Работа с уравнениями")
                                           )
                                       ]
                                   )]
                                   )

    elif which_button == "btn_09":
        bot.messaging.send_message(peer, "Выберите интересующую тему",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(27),
                                               interactive_media.InteractiveMediaButton("btn_27", "Изменить шрифт")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(28),
                                               interactive_media.InteractiveMediaButton("btn_28",
                                                                                        "Поменять интервалы/отступы")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(29),
                                               interactive_media.InteractiveMediaButton("btn_29", "Дополнительные параметры")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(30),
                                               interactive_media.InteractiveMediaButton("btn_30",
                                                                                        "Создать маркированный список")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(31),
                                               interactive_media.InteractiveMediaButton("btn_31",
                                                                                        "Создать многоуровневый список")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(32),
                                               interactive_media.InteractiveMediaButton("btn_32",
                                                                                        "Создать нумерованный список")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(33),
                                               interactive_media.InteractiveMediaButton("btn_33", "Выравнивание текста")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(34),
                                               interactive_media.InteractiveMediaButton("btn_34",
                                                                                        "Создать новый стиль")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(35),
                                               interactive_media.InteractiveMediaButton("btn_35",
                                                                                        "Скопировать стиль")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(36),
                                               interactive_media.InteractiveMediaButton("btn_36",
                                                                                        "Настройка с TextArt")
                                           )
                                       ]
                                   )]
                                   )

    elif which_button == "btn_10":
        bot.messaging.send_message(peer, "Выберите интересующую тему",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(37),
                                               interactive_media.InteractiveMediaButton("btn_37", "Совместная работа")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(38),
                                               interactive_media.InteractiveMediaButton("btn_38",
                                                                                        "Отслеживание изменений")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(39),
                                               interactive_media.InteractiveMediaButton("btn_39",
                                                                                        "Защита документа")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(40),
                                               interactive_media.InteractiveMediaButton("btn_40",
                                                                                        "Горячие клавиши")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(41),
                                               interactive_media.InteractiveMediaButton("btn_41",
                                                                                        "Гиперссылка на фрагмент текста")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(42),
                                               interactive_media.InteractiveMediaButton("btn_42",
                                                                                        "Настроить колонтитулы")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(43),
                                               interactive_media.InteractiveMediaButton("btn_43", "Нумерация страниц")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(44),
                                               interactive_media.InteractiveMediaButton("btn_44",
                                                                                        "Разрыв раздела")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(45),
                                               interactive_media.InteractiveMediaButton("btn_45",
                                                                                        "Создать колонки")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(46),
                                               interactive_media.InteractiveMediaButton("btn_46",
                                                                                        "Проверить орфографию")
                                           )
                                       ]
                                   )]
                                   )

    elif which_button == "btn_11":
        bot.messaging.send_message(peer, "Выберите интересующую тему",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(47),
                                               interactive_media.InteractiveMediaButton("btn_47", "Удаление строк/столбцов")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(48),
                                               interactive_media.InteractiveMediaButton("btn_48",
                                                                                        "Создать/открыть таблицу")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(49),
                                               interactive_media.InteractiveMediaButton("btn_49",
                                                                                        "Форматы для импорта/экспорта")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(50),
                                               interactive_media.InteractiveMediaButton("btn_50",
                                                                                        "Настройка ширины/высоты таблиц")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(51),
                                               interactive_media.InteractiveMediaButton("btn_51",
                                                                                        "Добавить изображение в ячейку")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(52),
                                               interactive_media.InteractiveMediaButton("btn_52",
                                                                                        "Доступ только для чтения")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(53),
                                               interactive_media.InteractiveMediaButton("btn_53", "Работа с несколькими книгами")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(54),
                                               interactive_media.InteractiveMediaButton("btn_54",
                                                                                        "Комментарии к ячейкам")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(55),
                                               interactive_media.InteractiveMediaButton("btn_55",
                                                                                        "Защита таблицы")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(56),
                                               interactive_media.InteractiveMediaButton("btn_56",
                                                                                        "Отобразить нулевые значения")
                                           )
                                       ]
                                   )]
                                   )

    elif which_button == "btn_12":
        bot.messaging.send_message(peer, "Выберите интересующую тему",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(57),
                                               interactive_media.InteractiveMediaButton("btn_57",
                                                                                        "Работа с ячейками дата/время")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(58),
                                               interactive_media.InteractiveMediaButton("btn_58",
                                                                                        "Копия форматированных ячеек")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(59),
                                               interactive_media.InteractiveMediaButton("btn_59",
                                                                                        "Выравнивание текста")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(60),
                                               interactive_media.InteractiveMediaButton("btn_60",
                                                                                        "Формат числовых значений")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(61),
                                               interactive_media.InteractiveMediaButton("btn_61",
                                                                                        "Разделительная линия")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(62),
                                               interactive_media.InteractiveMediaButton("btn_62",
                                                                                        "Доступ только для чтения")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(63),
                                               interactive_media.InteractiveMediaButton("btn_63",
                                                                                        "Формат ячеек при помощи валюты")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(64),
                                               interactive_media.InteractiveMediaButton("btn_64",
                                                                                        "Цвет и граница ячеек")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(65),
                                               interactive_media.InteractiveMediaButton("btn_65",
                                                                                        "Настройка удобной таблицы")
                                           )
                                       ]
                                   )]
                                   )
    elif which_button == "btn_13":
        bot.messaging.send_message(peer, "Выберите интересующую тему",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(66),
                                               interactive_media.InteractiveMediaButton("btn_66",
                                                                                        "Функция ВПР")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(67),
                                               interactive_media.InteractiveMediaButton("btn_67",
                                                                                        "Удаление дубликатов")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(68),
                                               interactive_media.InteractiveMediaButton("btn_68",
                                                                                        "Авто-скрытие пустых ячеек")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(69),
                                               interactive_media.InteractiveMediaButton("btn_69",
                                                                                        "Условное форматирование")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(70),
                                               interactive_media.InteractiveMediaButton("btn_70",
                                                                                        "Автозаполнение ячеек")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(71),
                                               interactive_media.InteractiveMediaButton("btn_71",
                                                                                        "Расчет среднего значения")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(72),
                                               interactive_media.InteractiveMediaButton("btn_72",
                                                                                        "Расширенные свойства ячейки")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(73),
                                               interactive_media.InteractiveMediaButton("btn_73",
                                                                                        "Запуск макроса")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(74),
                                               interactive_media.InteractiveMediaButton("btn_74",
                                                                                        "Выпадающий список")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(75),
                                               interactive_media.InteractiveMediaButton("btn_75",
                                                                                        "Поиск и замена текста")
                                           )
                                       ]
                                   )]
                                   )

    elif which_button == "btn_14":
        bot.messaging.send_message(peer, "Выберите интересующую тему",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(76),
                                               interactive_media.InteractiveMediaButton("btn_76",
                                                                                        "Форматирование сводной таблицы")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(77),
                                               interactive_media.InteractiveMediaButton("btn_77",
                                                                                        "График на основе данных")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(78),
                                               interactive_media.InteractiveMediaButton("btn_78",
                                                                                        "Смарт таблица")
                                           )
                                       ]
                                   )]
                                   )

    elif which_button == "btn_15":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[0] + ext)
        exit_func(params)

    elif which_button == "btn_16":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[1] + ext)
        exit_func(params)

    elif which_button == "btn_17":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[2] + ext)
        exit_func(params)

    elif which_button == "btn_18":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[3] + ext)
        exit_func(params)

    elif which_button == "btn_19":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[4] + ext)
        exit_func(params)

    elif which_button == "btn_20":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[5] + ext)
        exit_func(params)

    elif which_button == "btn_21":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[6] + ext)
        exit_func(params)

    elif which_button == "btn_22":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[7] + ext)
        exit_func(params)

    elif which_button == "btn_23":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[8] + ext)
        exit_func(params)

    elif which_button == "btn_24":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[9] + ext)
        exit_func(params)

    elif which_button == "btn_25":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[10] + ext)
        exit_func(params)

    elif which_button == "btn_26":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[11] + ext)
        exit_func(params)

    elif which_button == "btn_27":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[12] + ext)
        exit_func(params)

    elif which_button == "btn_28":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[13] + ext)
        exit_func(params)

    elif which_button == "btn_29":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[14] + ext)
        exit_func(params)

    elif which_button == "btn_30":
        bot.messaging.send_file(params.peer, path + 'Text' + textPageArray[15] + ext)
        exit_func(params)

    elif which_button == "btn_31":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[16] + ext)
        exit_func(params)

    elif which_button == "btn_32":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[17] + ext)
        exit_func(params)

    elif which_button == "btn_33":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[18] + ext)
        exit_func(params)

    elif which_button == "btn_34":
        bot.messaging.send_file(params.peer, path + 'Text' + textPageArray[19] + ext)
        exit_func(params)

    elif which_button == "btn_35":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[20] + ext)
        exit_func(params)

    elif which_button == "btn_36":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[21] + ext)
        exit_func(params)

    elif which_button == "btn_37":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[22] + ext)
        exit_func(params)

    elif which_button == "btn_38":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[23] + ext)
        exit_func(params)

    elif which_button == "btn_39":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[24] + ext)
        exit_func(params)

    elif which_button == "btn_40":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[25] + ext)
        exit_func(params)

    elif which_button == "btn_41":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[26] + ext)
        exit_func(params)

    elif which_button == "btn_42":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[27] + ext)
        exit_func(params)

    elif which_button == "btn_43":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[28] + ext)
        exit_func(params)

    elif which_button == "btn_44":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[29] + ext)
        exit_func(params)

    elif which_button == "btn_45":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[30] + ext)
        exit_func(params)

    elif which_button == "btn_46":
        bot.messaging.send_file(params.peer, path + 'Text/' + textPageArray[31] + ext)
        exit_func(params)



    elif which_button == "btn_47":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[0] + ext)
        exit_func(params)

    elif which_button == "btn_48":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[1] + ext)
        exit_func(params)

    elif which_button == "btn_49":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[2] + ext)
        exit_func(params)

    elif which_button == "btn_50":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[3] + ext)
        exit_func(params)

    elif which_button == "btn_51":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[4] + ext)
        exit_func(params)

    elif which_button == "btn_52":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[5] + ext)
        exit_func(params)

    elif which_button == "btn_53":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[6] + ext)
        exit_func(params)

    elif which_button == "btn_54":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[7] + ext)
        exit_func(params)

    elif which_button == "btn_55":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[8] + ext)
        exit_func(params)

    elif which_button == "btn_56":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[9] + ext)
        exit_func(params)

    elif which_button == "btn_57":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[10] + ext)
        exit_func(params)

    elif which_button == "btn_58":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[11] + ext)
        exit_func(params)

    elif which_button == "btn_59":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[12] + ext)
        exit_func(params)

    elif which_button == "btn_60":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[13] + ext)
        exit_func(params)

    elif which_button == "btn_61":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[14] + ext)
        exit_func(params)

    elif which_button == "btn_62":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[15] + ext)
        exit_func(params)

    elif which_button == "btn_63":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[16] + ext)
        exit_func(params)

    elif which_button == "btn_64":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[17] + ext)
        exit_func(params)

    elif which_button == "btn_65":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[18] + ext)
        exit_func(params)

    elif which_button == "btn_66":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[19] + ext)
        exit_func(params)

    elif which_button == "btn_67":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[20] + ext)
        exit_func(params)

    elif which_button == "btn_68":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[21] + ext)
        exit_func(params)

    elif which_button == "btn_69":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[22] + ext)
        exit_func(params)

    elif which_button == "btn_70":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[23] + ext)
        exit_func(params)

    elif which_button == "btn_71":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[24] + ext)
        exit_func(params)

    elif which_button == "btn_72":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[25] + ext)
        exit_func(params)

    elif which_button == "btn_73":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[26] + ext)
        exit_func(params)

    elif which_button == "btn_74":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[27] + ext)
        exit_func(params)

    elif which_button == "btn_75":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[28] + ext)
        exit_func(params)

    elif which_button == "btn_76":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[29] + ext)
        exit_func(params)

    elif which_button == "btn_77":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[30] + ext)
        exit_func(params)

    elif which_button == "btn_78":
        bot.messaging.send_file(params.peer, path + 'Tables/' + tablesPageArray[31] + ext)
        exit_func(params)


    elif which_button == "btn_79":
        start_func(params)

    elif which_button == "btn_80":
        feedbackScore.clear()
        bot.messaging.send_message(peer, "Оцените, какова вероятность,что вы порекомендуете чат бот коллеге\n(где 1 – точно не порекомендую, 10 – точно порекомендую)",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(81),
                                               interactive_media.InteractiveMediaButton("btn_81",
                                                                                        "1")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(82),
                                               interactive_media.InteractiveMediaButton("btn_82",
                                                                                        "2")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(83),
                                               interactive_media.InteractiveMediaButton("btn_83",
                                                                                        "3")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(84),
                                               interactive_media.InteractiveMediaButton("btn_84",
                                                                                        "4")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(85),
                                               interactive_media.InteractiveMediaButton("btn_85",
                                                                                        "5")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(86),
                                               interactive_media.InteractiveMediaButton("btn_86",
                                                                                        "6")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(87),
                                               interactive_media.InteractiveMediaButton("btn_87",
                                                                                        "7")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(88),
                                               interactive_media.InteractiveMediaButton("btn_88",
                                                                                        "8")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(89),
                                               interactive_media.InteractiveMediaButton("btn_89",
                                                                                        "9")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(90),
                                               interactive_media.InteractiveMediaButton("btn_90",
                                                                                        "10")
                                           )
                                       ]
                                   )]
                                   )
    elif which_button == "btn_81" or which_button == "btn_82" or which_button == "btn_83" or which_button == "btn_84" or which_button == "btn_85" or which_button == "btn_86" or which_button == "btn_87" or which_button == "btn_88" or which_button == "btn_89" or which_button == "btn_90":
        feedbackScore.append(int((which_button[4:6]))-80)
        bot.messaging.send_message(peer,
                                   "Оцените, насколько вы удовлетворены скоростью обработки чат-бота\n(где 1 – точно не удовлетворен, 6 – полностью удовлетворен)",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(91),
                                               interactive_media.InteractiveMediaButton("btn_91",
                                                                                        "1")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(92),
                                               interactive_media.InteractiveMediaButton("btn_92",
                                                                                        "2")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(93),
                                               interactive_media.InteractiveMediaButton("btn_93",
                                                                                        "3")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(94),
                                               interactive_media.InteractiveMediaButton("btn_94",
                                                                                        "4")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(95),
                                               interactive_media.InteractiveMediaButton("btn_95",
                                                                                        "5")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(96),
                                               interactive_media.InteractiveMediaButton("btn_96",
                                                                                        "6")
                                           )
                                       ]
                                   )]
                                   )
    elif which_button == "btn_91" or which_button == "btn_92" or which_button == "btn_93" or which_button == "btn_94" or which_button == "btn_95" or which_button == "btn_96":
        feedbackScore.append(int((which_button[4:6])) - 90)
        bot.messaging.send_message(peer,
                                   "Оцените, насколько база знаний чат-бота помогает в решении рабочих задач?\n(где 1 – совсем не помогает, 6 – является помогает)",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(97),
                                               interactive_media.InteractiveMediaButton("btn_97",
                                                                                        "1")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(98),
                                               interactive_media.InteractiveMediaButton("btn_98",
                                                                                        "2")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(99),
                                               interactive_media.InteractiveMediaButton("btn_99",
                                                                                        "3")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(100),
                                               interactive_media.InteractiveMediaButton("btn_100",
                                                                                        "4")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(101),
                                               interactive_media.InteractiveMediaButton("btn_101",
                                                                                        "5")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(102),
                                               interactive_media.InteractiveMediaButton("btn_102",
                                                                                        "6")
                                           )
                                       ]
                                   )]
                                   )
    elif which_button == "btn_97" or which_button == "btn_98" or which_button == "btn_99":
        feedbackScore.append(int((which_button[4:6])) - 96)
        question(params)

    elif which_button == "btn_100" or which_button == "btn_101" or which_button == "btn_102":
        feedbackScore.append(int((which_button[4:7])) - 96)
        question(params)

    elif which_button == "btn_103" or which_button == "btn_104" or which_button == "btn_105" or which_button == "btn_106" or which_button == "btn_107" or which_button == "btn_108":
        feedbackScore.append(int((which_button[4:7])) - 102)
        bot.messaging.send_message(peer,
                                   "Оцените как часто вы пользуетесь чат-ботом",
                                   [interactive_media.InteractiveMediaGroup(
                                       [
                                           interactive_media.InteractiveMedia(
                                               str(109),
                                               interactive_media.InteractiveMediaButton("btn_109",
                                                                                        "От 1 до 3 раз в неделю")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(110),
                                               interactive_media.InteractiveMediaButton("btn_110",
                                                                                        "От 3 до 7 раз в неделю")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(111),
                                               interactive_media.InteractiveMediaButton("btn_111",
                                                                                        "От 7 до 15 раз в неделю")
                                           ),
                                           interactive_media.InteractiveMedia(
                                               str(112),
                                               interactive_media.InteractiveMediaButton("btn_112",
                                                                                        "Более 15 раз")
                                           )
                                       ]
                                   )]
                                   )
    elif which_button == "btn_109" or which_button == "btn_110" or which_button == "btn_111" or which_button == "btn_112":
        feedbackScore.append(int((which_button[4:7])) - 108)
        bot.messaging.send_message(peer, "Какой продукт Вы бы хотели видеть в пуле чат- бота?\nНапишите ваше мнение, как я могу стать лучше")
        # for i in feedbackScore:
        #     bot.messaging.send_message(peer, str(feedbackScore[i]))
        time.sleep(7)
        bot.messaging.send_message(peer, "Спасибо за вашу обратную связь!")
        exit_func(params)


    # bot.messaging.send_message(peer, which_button)


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        'm.vocamate.ru',
        grpc.ssl_channel_credentials(),
        'd6eec0c32e37d1ddbe6f701147b0317fe59ee62d',
        verbose=True
    )

bot.messaging.on_message_async(on_msg, on_click)



# bot.messaging.on_message(on_msg, on_click)
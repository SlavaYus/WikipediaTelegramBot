import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import wikipedia, re
from datetime import datetime

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5809083420:AAE75j5pg9hcplDbgTBbBU_KeSIDCGELnhk")
# Диспетчер
dp = Dispatcher(bot)

wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def start(m, res=False):
    await bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia \n Чтобы сменить язык на английский введите En, \n Чтобы сменит язык на русский введите Ru, \n Чтобы сменить язык на французский - Fr, \n Чтобы сменить яхык на испанский - Es \n Чтобы узнать время - Time \n Чтобы открыть Яндекс - Yandex, \n Чтобы открыть StackOverflow - Stack. ')

@dp.message_handler(content_types=["text"])
async def handle_text(message):
    if message.text == 'En':
        wikipedia.set_lang("en")
        await bot.send_message(message.chat.id, "Язык выбран: English")
    elif message.text == "Ru":
        wikipedia.set_lang("ru")
        await bot.send_message(message.chat.id, "Язык выбран: Russian")     
    elif message.text == "Fr":
        wikipedia.set_lang("fr")
        await bot.send_message(message.chat.id, "Язык выбран: French")
    elif message.text == "Es":
        wikipedia.set_lang("es")
        await bot.send_message(message.chat.id, "Язык выбран: Spanish")
    elif message.text == "Time":
        
        await bot.send_message(message.chat.id, datetime.now())  
    elif message.text == "Yandex":
        
        await bot.send_message(message.chat.id, "https://dzen.ru/?yredirect=true")  
    elif message.text == "Stack":
        
        await bot.send_message(message.chat.id, "https://stackoverflow.com/")      
    else:
        await bot.send_message(message.chat.id, getwiki(message.text))
        
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
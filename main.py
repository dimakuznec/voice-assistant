import speech_recognition as sr 
import pyttsx3
import os
import webbrowser
import datetime
import random

# Настройка голосового синтезатора
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Функция для распознавания речи
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Вы сказали: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Я не понял вашу команду.")
        return ""
    except sr.RequestError:
        speak("Произошла ошибка при распознавании.")
        return ""

# Функция для рассказа шуток
def tell_joke():
    jokes = [
        "Почему программисты не ходят в лес? Потому что там много багов.",
        "Какой язык программирования предпочитают океаны? Си.",
        "Почему питоны никогда не устают? Потому что они всегда остаются гибкими.",
        "Почему Java-программисты всегда носят очки? Потому что они не могут C#.",
        "Что говорят разработчики, когда их код работает? Это магия!"
    ]
    joke = random.choice(jokes)
    speak(joke)

# Обработка команд
def process_command(command):
    twitch_url = 'https://www.twitch.tv'  # Обычный Twitch
    twitch_channel_url = 'https://m.twitch.tv/michal_ivanich/home'  # URL твоего Twitch-канала

    if 'привет' in command:
        speak("Привет! Как я могу помочь?")
    elif 'что ты можешь' in command or 'что ты умеешь' in command:
        speak("Я могу выполнять различные команды, например, открывать браузер, искать информацию в интернете, проверять время, закрывать приложения, открывать Twitch и ваш Twitch канал, а также рассказывать шутки.")
    elif 'окей google' in command or 'открой google' in command or 'открой гугл' in command:
        webbrowser.open('https://www.google.com')
        speak("Открываю Google.")
    elif 'открой яндекс' in command or 'открой yandex' in command:
        webbrowser.open('https://www.yandex.ru')
        speak("Открываю Яндекс.")
    elif 'открой youtube' in command:
        webbrowser.open('https://www.youtube.com')
        speak("Открываю YouTube.")
    elif 'открой twitch' in command and 'канал' not in command:
        webbrowser.open(twitch_url)
        speak("Открываю Twitch.")
    elif any(phrase in command for phrase in ['открой твич канал', 'открой мой твич канал', 'перейди на мой twitch канал', 'запусти мой twitch', 'мой твич']):
        webbrowser.open(twitch_channel_url)
        speak("Открываю ваш Twitch канал.")
    elif 'поиск' in command:
        query = command.replace('поиск', '').strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Ищу {query} в интернете.")
    elif 'время' in command or 'сколько времени' in command:
        now = datetime.datetime.now().strftime('%H:%M')
        speak(f"Сейчас {now}.")
    elif 'закрой' in command:
        if 'блокнот' in command:
            os.system('taskkill /f /im notepad.exe')
            speak("Закрываю блокнот.")
        elif 'браузер' in command:
            os.system('taskkill /f /im chrome.exe')
            speak("Закрываю браузер.")
        else:
            speak("Не могу найти указанное приложение.")
    elif 'расскажи шутку' in command or 'пошути' in command or 'шутка' in command:
        tell_joke()
    else:
        speak("Я не знаю, как выполнить эту команду.")

if __name__ == "__main__":
    speak("Привет! Я ваш голосовой помощник. Как я могу помочь?")
    while True:
        command = listen_command()
        if command:
            process_command(command)

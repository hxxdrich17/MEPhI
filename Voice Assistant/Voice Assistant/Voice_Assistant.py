# ПЕРЕД ЗАПУСКОМ ОБЯЗАТЕЛЬНО УСТАНОВИТЬ МОДУЛИ (В том порядке, в котором они даны(ВАЖНО!)):
# если вы используете PyCharm, то py -m писать не обязательно
# py -m pip install pywin32
# py -m pip install pypiwin32
# py -m pip install pyttsx3
# py -m pip install SpeechRecognition
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio (Модуль PyAudio скачивать по этой ссылке в соответсвии
# с вашей версией Python) зайдите в cmd и укажите папку в которой находится модуль PyAudio.whl, после чего
# вводите комманду py -m pip install (полное название файла.whl)
# py -m pip install fuzzywuzzy

import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import requests
import sys
 
# настройки
opts = {
    "alias": ('саня','саша','александр','сашок','сашка','сашик',
              'санёк','санек','санчо','сань','саш'),
    "tbr": ('скажи','расскажи','покажи','сколько','произнеси'),
    "cmds": {
        "ctime": ('текущее время','сейчас времени','который час'),
        "radio": ('включи музыку','воспроизведи радио','включи радио'),
        "stupid1": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты')
    }
}
 
# функции
def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
 
    
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)
    
        if voice.startswith(opts["alias"]):
            # обращаются к Сане
            cmd = voice
 
            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()
            
            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            
            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])
 
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")
 
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC
 
def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    
    elif cmd == 'radio':
        # воспроизвести радио
        os.system("Тут ссылка на программу радио в проводнике")
    
    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
    else:
        print('Команда не распознана, повторите!')
 
# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index = 0)
 
with m as source:
    r.adjust_for_ambient_noise(source)
 
speak_engine = pyttsx3.init()

# voices = speak_engine.getProperty('voices')

# # Задать голос по умолчанию
# speak_engine.setProperty('voice', 'ru') 
 
#Только если у вас установлены голоса для синтеза речи!
#voices = speak_engine.getProperty('voices')
#speak_engine.setProperty('voice', voices[4].id)
 
# тест на работоспособность
#speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
 
speak("Добрый день, повелитель")
speak("Саня слушает")
 
stop_listening = r.listen_in_background(m, callback)
while True: 
    time.sleep(0.1)

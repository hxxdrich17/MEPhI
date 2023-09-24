# ОБЯЗАТЕЛЬНО К ВЫПОЛНЕНИЮ ПОСЛЕ УСТАНОВКИ ВСЕХ МОДУЛЕЙ ИЗ Voice Assistant.py
# найдите в списке свой микрофон и запомните его Index номер
# если микрофон не работает, можете попробовать другой индекс

import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
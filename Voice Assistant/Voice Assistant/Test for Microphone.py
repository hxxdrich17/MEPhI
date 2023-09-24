import speech_recognition as sr

r = sr.Recognizer()
while True:
    while (True):
        with sr.Microphone(device_index=0) as source:
            print('Скажите что-нибудь...')
            audio = r.listen(source)

        query = r.recognize_google(audio, language='ru-RU')
        print('Вы сказали: ' + query.lower())
        break
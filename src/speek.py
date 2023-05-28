import speech_recognition as sr
import pyttsx3 #convierte texto en voz
import json
from time import time

start_time = time()
engine = pyttsx3.init()

# name of the virtual assistant
name = 'amor'
attemts = 0

# keys
#with open('src/keys.json') as json_file:
#    keys = json.load(json_file)

# colors
green_color = "\033[1;32;40m"
red_color = "\033[1;31;40m"
normal_color = "\033[0;37;40m"

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    status = False


    print ('paso 1')

    with sr.AudioFile('audio.wav') as source:
        print ('paso 2')

        audio = r.record(source)
        print ('paso 3')
        texto1= r.recognize_google(audio, language='es-ES').lower()
        print ('paso 4')
        print (texto1)

    with sr.Microphone(

    ) as source:
        print(f"{green_color}({attemts}) Escuchando...{normal_color}")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        rec = ""

        try:
            rec = r.recognize_google(audio, language='es-ES').lower()
            
            if name in rec:
                rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                status = True
            else:
                print(f"Vuelve a intentarlo, no reconozco: {rec}")
        except:
            pass
    return {'text':rec, 'status':status}

while True:
    rec_json = get_audio()

    rec = rec_json['text']
    status = rec_json['status']

    if status:
       #campo de la vista donde debe mostrar en texto el audio 

        
        attemts = 0
    else:
        attemts += 1

print(f"{red_color} PROGRAMA FINALIZADO CON UNA DURACIÓN DE: { int(time() - start_time) } SEGUNDOS {normal_color}")
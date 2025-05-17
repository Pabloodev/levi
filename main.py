# main.py

import speech_recognition as sr
import pyttsx3
from intencao import classificar_intencao
import plugins.hora
import plugins.piada

plugin_map = {
    "hora": plugins.hora,
    "piada": plugins.piada,
}

r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:

    engine.say("Olá Pablo, estou ouvindo...")
    engine.runAndWait()

    print("Fale algo:")
    audio = r.listen(source)
    texto = r.recognize_google(audio, language='pt-BR')

    print(f"Você disse: {texto}")

    # Entender intenção
    intencao = classificar_intencao(texto)
    print(f"Intenção detectada: {intencao}")

    if intencao in plugin_map:
        resposta = plugin_map[intencao].executa(texto)
        engine.say(resposta)
        engine.runAndWait()
    else:
        engine.say("Desculpe, não entendi o que você quer.")
        engine.runAndWait()
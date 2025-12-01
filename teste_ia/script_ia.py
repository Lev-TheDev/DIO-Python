print ("testando...")

import speech_recognition as sr
import os

def ouvir_microfone():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)

    try:
        # Reconhece a fala
        frase = microfone.recognize_google(audio, language='pt-BR')
        
        # DICA DE OURO: Transforma tudo em minúsculas para facilitar a comparação
        frase = frase.lower()
        
        # Mostra o que foi ouvido (ajuda muito a encontrar erros!)
        print("Você disse: " + frase)

        if "navegador" in frase:
            os.system("firefox &")
            return False
        
        elif "excel" in frase:  # Note que agora escrevemos 'excel' em minúsculo
            os.system("libreoffice --calc &")
            return False
        
        elif "powerpoint" in frase: # 'powerpoint' minúsculo
            os.system("libreoffice --impress &")
            return False
        
        elif "edge" in frase:
            os.system("microsoft-edge-stable &")
            return False
        
        # Agora vai funcionar mesmo se disser "fechar", "FECHAR", etc.
        elif "fechar" in frase:
            print("Encerrando assistente.")
            return True  # Isso faz o loop lá embaixo parar
    
    except sr.UnknownValueError:
        print("Não entendi")
    
    return False
    
while True:
    if ouvir_microfone():
        break
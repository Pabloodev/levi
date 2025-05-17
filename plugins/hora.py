from datetime import datetime

def executa(frase):
  agora = datetime.now()
  return agora.strftime("Agora são %H horas e %M minutos.")
# Plugin para caso usario questione sobre horas

from datetime import datetime

def executa(frase):
  agora = datetime.now()
  return agora.strftime("Olá! Agora são %H horas e %M minutos.")
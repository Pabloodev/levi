import asyncio
from jokeapi import Jokes

async def obter_piada():
    j = await Jokes()
    joke = await j.get_joke(lang='pt')
    if joke["type"] == "single":
        return joke["joke"]
    else:
        return f"{joke['setup']} ... {joke['delivery']}"

def executa(frase):
    try:
        return asyncio.run(obter_piada())
    except Exception as e:
        return "Desculpe, não consegui pensar em uma piada agora."

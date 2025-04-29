import spacy

# Carregar o modelo de língua portuguesa
nlp = spacy.load("pt_core_news_sm")

def classificar_intencao(frase):
    doc = nlp(frase.lower())

    if any(token.lemma_ in ["hora", "horário", "tempo"] for token in doc):
        return "hora"
    
    if any(token.lemma_ in ["tocar", "música", "cantar"] for token in doc):
        return "musica"
    
    if any(token.lemma_ in ["clima", "tempo", "chuva", "sol"] for token in doc):
        return "clima"

    return "desconhecido"
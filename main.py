from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def homepage():
    return "Hello World!"


@app.get('/stampa')
def stampa(testo):
    return "Hai scritto: " + testo


@app.get('/greet')
def greet(nome : str, cognome : str):
    return f"Ciao  {nome} {cognome}!"


@app.get('/linguaggio')
def lingua(testo):
    from langdetect import detect

    #testo = "Ciao, sto parlando in italiano" 
    lingua = detect(testo)

    print(f"La lingua rilevata è: {lingua}")

    return f"La lingua rilevata è: {lingua}"


@app.get('/sentiment')
def sentiment(frase):
    from textblob import TextBlob

    #frase = "I'm happy!"
    blob = TextBlob(frase)

    # Se sentiment > 0 allora -> positivo
    # Se sentiment < 0 allora -> negativo
    # Se sentiment = 0 allora -> neutro
    sentiment = blob.sentiment.polarity
    print(sentiment)
    if sentiment > 0:
        sentiment = "positivo"
    elif sentiment < 0: 
        sentiment = "negativo"
    else:           
        sentiment = "neutro"

    return f"sentimento: {sentiment}"

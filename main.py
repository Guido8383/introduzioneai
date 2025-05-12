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
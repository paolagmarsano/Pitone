"""
ESERCIZIO 2 - Che tempo fa? 🌤
Scrivi una funzione che abbia 
come input da parte dell'utente una "città",
che ti mostri tutte le informazioni climatiche di quella città.
Le informazioni meteorologiche vengono servite tramite API 
dal sito "openweathermap.org".
Si richiede di mostrare: 
- descrizione climatica, 
- temperatura(base, minima e massima in C°),
- umidità(%), velocità del vento(in km/h), 
- considerando come lingua L'ITALIANO. 
Di seguito i dati per lo svolgimento:

import requests
API_KEY = '0e7d546659d27f37015346a62a3addb7'
DOCUMENTAZIONE API: https://openweathermap.org/current """
#---------------------------------------------------------------------------------
#Cosa DEVO fare:
#All-inizio mettere il codice del prof
#ricercare documentazione
# https://docs.python-requests.org/en/latest/
#r = requests.get('https://www.python.org')
#https://openweathermap.org/current#geo
#da input nome citta deve darmi una request 
#il nome della citta dovrebbe corrispondere a dopo ?q 
#API_KEY cercare dove porla
#cercare su google traduzione to italian language
#-----------------------------s----------------------------------------------------


import requests

API_KEY = '0e7d546659d27f37015346a62a3addb7'
tradurre_italiano= {'lang':'it','units':'metric'} 
nome_citta = input("inserisci nome città: \n")

def meteo(citta):
    risposta = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={nome_citta}&appid={API_KEY}",params= tradurre_italiano )
  
    print(risposta.json())
    if risposta.status_code == 200:
        print("successo")
        dati_meteo = risposta.json()
        print(dati_meteo)
        print(f"Descrizione climatica: {dati_meteo['weather'][0]['description']}\n")
        print(f"temperatura base: {dati_meteo['main']['temp']} °C")
        print(f"temperatura minima: {dati_meteo['main']['temp_min']} °C ")
        print(f"temperatura massima: {dati_meteo['main']['temp_max']} °C ")
        #print(f"temperatura percepita: {dati_meteo['main']['feels_like']}°C\n")
        print(f"umidità: {dati_meteo['main']['humidity']}%")
        print(f"velocità del vento: {dati_meteo['wind']['speed']} km/h")    
    elif  risposta.status_code == 404:
         print("Città non trovata")
meteo(nome_citta)



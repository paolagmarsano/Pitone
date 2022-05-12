"""
ESERCIZIO 1 - Indovina il numero 🕵️🕵️‍♂️
Crea una funziona che permetta all'utente di indovinare
un numero generato random tra 0 e 100,
con un massimo di 10 tentativi da parte dell'utente.  """
import random 
i= 0
numero= random.randint(0,100)
print(numero)
def indovina(numero, i):
    for i in range(10):
        dammi= int(input("Scrivi un numero da 0 a 100: "))
        if dammi == numero:
            print('Hai indovinato')
            break
        elif i<=10:
            print(f"Non hai indovinato, ritenta, hai usato {i+1} possibilità")
        else:
            print('Hai finito le possibilità')
indovina(numero, i)

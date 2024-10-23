import serial
import time
import random

ser = serial.Serial('COM11', 9600)
ser.flush()

bases_de_donnees = [
    "actions_verites.txt",
    "dinosaures_descriptions.txt",
    "citations_celebres.txt",
    "dinosaures_noms.txt",
    "rap.txt",
    "aleatoire.txt"
]

def charger_donnees(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        texte = f.read()
    return texte

def envoyer_phrase(base_index):
    base_choisie = bases_de_donnees[base_index]
    texte = charger_donnees(base_choisie)

    import markovify
    modele = markovify.Text(texte)
    
    phrase = modele.make_sentence()
    phrase = ' '.join(phrase.split())
    ser.write((phrase + ' ').encode('utf-8'))
    time.sleep(1)
    
while True:
    if ser.in_waiting > 0:
        base_index = int(ser.read().decode('utf-8'))
        envoyer_phrase(base_index)
        time.sleep(10)

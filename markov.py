import serial
import time
import random
import markovify

# Configuration de la communication série
try:
    ser = serial.Serial('COM3', 9600)
    ser.flush()
    print("Connexion série établie avec succès.---------------------------------------------------")
except serial.SerialException as e:
    print(f"Erreur de connexion série : {e}")
    exit(1)

# Liste des bases de données
bases_de_donnees = [
    "actions_verites.txt",
    "dinosaures_descriptions.txt",
    "citations_celebres.txt",
    "dinosaures_noms.txt",
    "rap.txt",
    "aleatoire.txt"
]

# Fonction pour charger les données d'un fichier
def charger_donnees(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            texte = f.read()
        print(f"Fichier {chemin} chargé avec succès.")
        return texte
    except Exception as e:
        print(f"Erreur lors du chargement du fichier {chemin}: {e}")
        return ""

# Fonction pour envoyer une phrase générée par Markov
def envoyer_phrase(base_index):
    try:
        base_choisie = bases_de_donnees[base_index]
        print(f"Base choisie: {base_choisie}-------------------------------------------------------")
        texte = charger_donnees(base_choisie)

        if texte == "":
            print("Le fichier est vide ou il y a eu une erreur lors de son chargement. Impossible de générer une phrase.")
            return

        modele = markovify.Text(texte)
        phrase = modele.make_sentence()
        if phrase:
            phrase = ' '.join(phrase.split())
            print(f"Phrase générée: {phrase}")
            ser.write((phrase + ' ').encode('utf-8'))
            time.sleep(1)
        else:
            print("Impossible de générer une phrase avec le modèle Markov.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de la phrase : {e}")

# Boucle principale
while True:
    try:
        if ser.in_waiting > 0:
            base_index = int(ser.read().decode('utf-8'))
            if base_index < 0 or base_index >= len(bases_de_donnees):
                print(f"Indice de base invalide: {base_index}")
                continue
            envoyer_phrase(base_index)
            time.sleep(10)
    except Exception as e:
        print(f"Erreur dans la boucle principale : {e}")
        time.sleep(5)  # Attente avant de réessayer

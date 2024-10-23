import markovify
import serial
import time
import random

# Connexion au Arduino
ser = serial.Serial('COM11', 9600)  # Remplacer COM8 par votre port série

# Confirmer l'envoi de toutes les données
ser.flush()

# Fonction pour ouvrir la base de données
def charger_donnees(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        texte = f.read()
    return texte

# Fonction pour couper les phrases en groupe de 4
def splitTextToQuadruplet(phrase):
    mots = phrase.split()
    mots_groupes = [' '.join(mots[i: i + 4]) for i in range(0, len(mots), 4)]
    return mots_groupes

# Charger le fichier "aleatoire.txt"
texte_aleatoire = charger_donnees("aleatoire.txt")
modele_aleatoire = markovify.Text(texte_aleatoire)

# Début de la boucle infinie pour générer des phrases en continu
while True:
    # Générer une phrase aléatoire avec Markov
    phrase = modele_aleatoire.make_sentence()

    # Envoyer un entête sur le port série de l'Arduino
    ser.write(("----------").encode("utf-8"))
    time.sleep(3)  # Attendre un court instant avant d'envoyer la phrase

    # Envoyer la phrase par groupe de 4 mots
    for groupe in splitTextToQuadruplet(str(phrase)):
        ser.write((groupe).encode("utf-8"))
        time.sleep(5)

    # Envoyer un espace pour la séparation
    ser.write((' ').encode())
    time.sleep(3)

    # Afficher la phrase générée pour vérification
    print(f"La phrase à imprimer est: {phrase}")
    print("Fin d'impression\n")

    # Attendre un moment avant de générer une nouvelle phrase
    time.sleep(10)

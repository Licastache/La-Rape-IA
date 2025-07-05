import serial
import time
import markovify
import sys
import unicodedata
import re

PORT_SERIE = 'COM4'  # Adapte selon ton système (ex: /dev/ttyUSB0 sous Linux)
BAUD_RATE = 9600
TIMEOUT = 60  # Timeout de lecture série en secondes

bases_de_donnees = [
    "actions_verites.txt",
    "dinosaures_descriptions.txt",
    "citations_celebres.txt",
    "dinosaures_noms.txt",
    "rap.txt",
    "aleatoire.txt"
]


def retirer_accents(texte):
    # Normalize la chaîne en décomposant les caractères accentués
    texte_normalise = unicodedata.normalize('NFD', texte)
    # Filtrer les caractères qui ne sont pas des marques diacritiques (accents)
    texte_sans_accents = ''.join(
        c for c in texte_normalise
        if unicodedata.category(c) != 'Mn'
    )
    return texte_sans_accents

def charger_donnees(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"[ERREUR] Lecture fichier {chemin} : {e}")
        return ""

def generer_phrase(texte):
    if not texte.strip():
        return None
    try:
        modele = markovify.Text(texte)
        for _ in range(5):
            phrase = modele.make_sentence()
            if phrase:
                return ' '.join(phrase.split())
    except Exception as e:
        print(f"[ERREUR] Génération Markov : {e}")
    return None

def attendre_message(ser, attendu, timeout=TIMEOUT):
    print(f"[INFO] Attente de '{attendu}'")
    t0 = time.time()
    while time.time() - t0 < timeout:
        if ser.in_waiting > 0:
            ligne = ser.readline().decode('utf-8').strip()
            print(f"[←] {ligne}")
            if ligne == attendu:
                return True
        time.sleep(0.05)
    print(f"[ERREUR] Timeout : pas de '{attendu}' reçu.")
    return False

def main():
    try:
        ser = serial.Serial(PORT_SERIE, BAUD_RATE, timeout=1)
        ser.flush()
        print("[OK] Connexion série établie.")
    except serial.SerialException as e:
        print(f"[ERREUR] Port série : {e}")
        sys.exit(1)

    try:
        while True:
            if ser.in_waiting > 0:
                ligne = ser.readline().decode('utf-8').strip()
                if ligne.isdigit():
                    base_index = int(ligne)
                    if base_index < 0 or base_index >= len(bases_de_donnees):
                        print(f"[ERREUR] Index {base_index} invalide.")
                        continue

                    print(f"[→] Index reçu : {base_index}")

                    # On attend le READY de l'Arduino avant d'envoyer la phrase
                    if attendre_message(ser, "READY"):
                        texte = charger_donnees(bases_de_donnees[base_index])
                        phrase = generer_phrase(texte)
                        
                        if phrase:
                            phrase = retirer_accents(phrase)
                            print(f"[→] Phrase envoyée : {phrase}")
                            ser.write((phrase + "\n").encode('utf-8'))

                            # On attend que l'Arduino confirme la réception avec DONE
                            if attendre_message(ser, "DONE"):
                                print("[✓] Phrase affichée.")
                        else:
                            print("[ERREUR] Aucune phrase générée.")
                    else:
                        print("[ERREUR] Pas de READY reçu, on ignore cette demande.")
                else:
                    print(f"[WARN] Donnée inattendue : {ligne}")
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n[INFO] Arrêté par l'utilisateur.")
    finally:
        ser.close()
        print("[INFO] Port série fermé.")

if __name__ == "__main__":
    main()

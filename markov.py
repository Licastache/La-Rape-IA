import serial
import time
import markovify
import sys
import unicodedata
import re
import glob

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
    texte_normalise = unicodedata.normalize('NFD', texte)
    return ''.join(c for c in texte_normalise if unicodedata.category(c) != 'Mn')

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

def detecter_port_serie():
    ports_possibles = glob.glob("/dev/ttyACM*") + glob.glob("/dev/ttyUSB*")
    if not ports_possibles:
        print("[ERREUR] Aucun port série détecté (ttyACM* ou ttyUSB*).")
        return None
    print(f"[INFO] Port série détecté : {ports_possibles[0]}")
    return ports_possibles[0]

def main():
    port_serie = detecter_port_serie()
    if port_serie is None:
        sys.exit(1)

    try:
        ser = serial.Serial(port_serie, BAUD_RATE, timeout=1)
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

                    if attendre_message(ser, "READY"):
                        texte = charger_donnees(bases_de_donnees[base_index])
                        phrase = generer_phrase(texte)
                        
                        if phrase:
                            phrase = retirer_accents(phrase)
                            print(f"[→] Phrase envoyée : {phrase}")
                            ser.write((phrase + "\n").encode('utf-8'))

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

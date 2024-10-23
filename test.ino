#include <LiquidCrystal.h>

// Initialisation de l'écran LCD en mode 4 bits
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// Variable pour stocker la phrase reçue
String receivedText = "";

void setup() {
  // Initialiser la communication série à 9600 bauds
  Serial.begin(9600);
  
  // Initialiser l'écran LCD avec 16 colonnes et 2 lignes
  lcd.begin(16, 2);
  
  // Afficher un message de démarrage
  lcd.print("Ready...");
}

void loop() {
  // Vérifier si des données sont disponibles sur le port série
  if (Serial.available() > 0) {
    char c = Serial.read();  // Lire un caractère depuis le port série
    
    // Vérifier la fin de la transmission d'une phrase
    if (c == ' ') {
      // Afficher la phrase reçue sur l'écran LCD
      scrollText(receivedText);
      
      // Effacer le texte reçu après l'affichage
      receivedText = "";
    } else {
      // Ajouter le caractère à la phrase reçue
      receivedText += c;
    }
  }
}

// Fonction pour faire défiler le texte sur la deuxième ligne de l'écran LCD
void scrollText(String text) {
  // Ajouter des espaces au début et à la fin du texte pour le défilement
  String scrollingText = "                " + text + "                ";
  
  // Calculer la longueur du texte total avec les espaces
  int textLength = scrollingText.length();
  
  // Faire défiler le texte de droite à gauche
  for (int i = 0; i <= textLength - 16; i++) {
    lcd.setCursor(0, 1);  // Positionner le curseur sur la deuxième ligne
    lcd.print(scrollingText.substring(i, i + 16));  // Afficher 16 caractères à la fois
    
    delay(300);  // Attendre un moment avant de faire défiler le texte
  }
  
  // Attendre 2 secondes après le défilement
  delay(2000);
}

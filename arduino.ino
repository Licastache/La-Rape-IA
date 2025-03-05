#include <LiquidCrystal.h>

// Initialisation de l'écran LCD (broches en fonction de votre configuration)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// Broches utilisées pour le potentiomètre et le bouton
const int potentiometerPin = A0;
const int buttonPin = 8;

int currentBase = 0;
bool selectionValidee = false;

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);  // Initialisation de l'écran avec 16 colonnes et 2 lignes
  pinMode(buttonPin, INPUT_PULLUP);  // Bouton configuré en mode pull-up
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
}

void loop() {
  // Lire la valeur du potentiomètre
  digitalWrite(9, HIGH); // Allumage led ROUGE
  
  int sensorValue = analogRead(potentiometerPin);

  // Sélectionner la base de données en fonction de la valeur du potentiomètre
  if (!selectionValidee) {
    currentBase = map(sensorValue, 0, 1023, 0, 6); // 7 bases, donc de 0 à 6
    delay(10); // Petit delai pour éviter que l'écran ne sature
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Mode de jeu : ");
    lcd.print(currentBase + 1);  // Affiche la base sélectionnée
  }

  // Vérifier si le bouton est pressé pour valider la sélection
  if (digitalRead(buttonPin) == LOW) {
    selectionValidee = true;
    lcd.setCursor(0, 1);
    lcd.print("Base validee!");
    digitalWrite(9, LOW); // LED ROUGE
    digitalWrite(7, HIGH); // Allumer la led verte
    delay(500);  // Petit délai pour éviter les rebonds

    // Envoyer la sélection au script Python
    Serial.print(currentBase);
    delay(2000);  // Attendre avant de commencer à lire les phrases
    digitalWrite(7, LOW); // Eteindre la led verte
    digitalWrite(9, HIGH); // LED ROUGE
  }

  // Lire et afficher la phrase reçue sur le LCD
  if (selectionValidee && Serial.available() > 0) {
    lcd.clear();
    digitalWrite(9, LOW); // LED ROUGE
    digitalWrite(6, HIGH); // Allumage led orange processing
    String receivedText = "";
    while (Serial.available() > 0) {
      char c = Serial.read();
      receivedText += c;
      delay(10);  // Petit délai pour assurer la réception complète
    }
    scrollText(receivedText);

    // Réinitialiser la sélection après avoir affiché la phrase
    selectionValidee = false;
    delay(1000);  // Attendre un peu avant de permettre une nouvelle sélection
    digitalWrite(6, LOW); // fin led orange
    digitalWrite(9, HIGH); // LED ROUGE
  }
}

void scrollText(String text) {
  String scrollingText = "                " + text + "                ";
  int textLength = scrollingText.length();

  for (int i = 0; i <= textLength - 16; i++) {
    lcd.setCursor(0, 1);
    lcd.print(scrollingText.substring(i, i + 16));
    delay(300);
  }
}

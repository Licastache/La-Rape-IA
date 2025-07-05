#include <LiquidCrystal.h>
#include <Bounce2.h>

// Initialisation de l'écran LCD
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// Broches
const int potentiometerPin = A0;
const int buttonPin = 8;
const int ledRouge = 9;
const int ledVerte = 7;
const int ledOrange = 6;

Bounce debouncer = Bounce();

int currentBase = 0;
int lastBase = -1;
bool selectionValidee = false;

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);

  pinMode(ledRouge, OUTPUT);
  pinMode(ledVerte, OUTPUT);
  pinMode(ledOrange, OUTPUT);
  digitalWrite(ledRouge, HIGH);
  digitalWrite(ledOrange, LOW);
  digitalWrite(ledVerte, LOW);

  debouncer.attach(buttonPin, INPUT_PULLUP);
  debouncer.interval(25);
}

void loop() {
  debouncer.update();

  int sensorValue = analogRead(potentiometerPin);
  sensorValue = constrain(sensorValue, 0, 1022);
  currentBase = map(sensorValue, 0, 1023, 0, 6);

  if (!selectionValidee) {
    if (currentBase != lastBase) {
      lcd.setCursor(0, 0);
      lcd.print("Mode de jeu :    ");
      lcd.setCursor(13, 0);
      lcd.print(currentBase + 1);
      lastBase = currentBase;
    }

    if (debouncer.fell()) {
      selectionValidee = true;
      lcd.setCursor(0, 1);
      lcd.print("                ");  // Effacer la ligne avant affichage
      lcd.setCursor(0, 1);
      lcd.print("Base validee!");

      digitalWrite(ledRouge, LOW);
      digitalWrite(ledVerte, HIGH);
      delay(300);
      digitalWrite(ledVerte, LOW);
      digitalWrite(ledRouge, HIGH);

      Serial.println(currentBase);
      Serial.println("READY");
    }
  }

  if (selectionValidee && Serial.available() > 0) {
    String receivedText = "";
    digitalWrite(ledRouge, LOW);
    digitalWrite(ledOrange, HIGH);  // LED orange allumée pendant traitement

    while (Serial.available() > 0) {
      char c = Serial.read();
      // Ne garder que les caractères imprimables ASCII (32 à 126)
      if (c >= 32 && c <= 126) {
        receivedText += c;
      }
      delay(2);
    }

    Serial.print("DEBUG RX: [");
    Serial.print(receivedText);
    Serial.println("]");

    lcd.clear();
    scrollText(receivedText);

    Serial.println("DONE");
    selectionValidee = false;
    digitalWrite(ledOrange, LOW);  // Extinction LED orange
    digitalWrite(ledRouge, HIGH);
    lastBase = -1;
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

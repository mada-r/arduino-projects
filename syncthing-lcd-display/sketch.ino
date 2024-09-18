#include <LiquidCrystal.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

const int maxLineLength = 16;
String buffer = "";

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600); // Set baud rate to match the Python script
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      if (buffer.length() > 0) {
        displayText(buffer);
        buffer = "";
        delay(100);
      }
    } else {
      buffer += c;
    }
  }
}

void displayText(String text) {
  int length = text.length();
  int line = 0;
  for (int i = 0; i < length; i += maxLineLength) {
    if (line >= 2) break;
    lcd.setCursor(0, line);
    lcd.print(text.substring(i, i + maxLineLength));
    line++;
  }
}

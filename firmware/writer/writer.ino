#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 5  // Configurable, see typical pin layout above
#define SS_PIN 4   // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key;

String readerId = "DSJ001";

void setup() {
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();
}

void loop() {
  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;
  if (!mfrc522.PICC_IsNewCardPresent() || !mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  Serial.print(F("Card UID:"));
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.println();

  Serial.print(F("PICC type: "));
  MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
  Serial.println(mfrc522.PICC_GetTypeName(piccType));
  Serial.println();

  Serial.setTimeout(20000L);  // because unsigned long integer type is used, its best practice to write L

  byte messageLength = 32;  // in bytes
  byte buffer[messageLength];
  byte inputLength;

  Serial.println("Input Product ID...");
  inputLength = Serial.readBytesUntil('\n', (char *)buffer, messageLength);  // size_t is unsigned long long type which is the largest number possible
  for (byte i = inputLength; i < messageLength; i++) buffer[i] = ' ';
  Serial.print("Input: ");
  for (byte i = 0; i < messageLength; i++) {
    Serial.write(buffer[i]);
  };
  Serial.println();
  // Each block 16 bytes max
  WriteToBlock(1, buffer);
  WriteToBlock(2, &buffer[16]);

  Serial.println("Input Current Date...");
  inputLength = Serial.readBytesUntil('\n', (char *)buffer, messageLength);  // size_t is unsigned long long type which is the largest number possible
  for (byte i = inputLength; i < messageLength; i++) buffer[i] = ' ';
  Serial.print("Input: ");
  for (byte i = 0; i < messageLength; i++) {
    Serial.write(buffer[i]);
  };
  Serial.println();
  WriteToBlock(4, buffer);
  WriteToBlock(5, &buffer[16]);

  Serial.println("Input Product Name...");
  inputLength = Serial.readBytesUntil('\n', (char *)buffer, messageLength);  // size_t is unsigned long long type which is the largest number possible
  for (byte i = inputLength; i < messageLength; i++) buffer[i] = ' ';
  Serial.print("Input: ");
  for (byte i = 0; i < messageLength; i++) {
    Serial.write(buffer[i]);
  };
  Serial.println();
  WriteToBlock(8, buffer);
  WriteToBlock(9, &buffer[16]);

  delay(1000);
  mfrc522.PICC_HaltA();       // Halt PICC
  mfrc522.PCD_StopCrypto1();  // Stop encryption on PCD
  Serial.println();
  Serial.println();
  Serial.println();
}

void WriteToBlock(int blockNum, byte buffer[]) {
  MFRC522::StatusCode status;
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, blockNum, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("PCD_Authenticate() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }

  status = mfrc522.MIFARE_Write(blockNum, buffer, 16);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("MIFARE_Write() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  } else Serial.println(F("MIFARE_Write() success: "));
}

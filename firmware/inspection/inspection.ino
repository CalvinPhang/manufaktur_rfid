#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 5  // Configurable, see typical pin layout above
#define SS_PIN 4   // Configurable, see typical pin layout above

const char* ssid = "CALVIN-Student";
const char* password = "CITStudentsOnly";

String serverName = "http://10.252.240.21:8000";

MFRC522 mfrc522(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key;

String readerId = "DSJ001";

void setup() {
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (WiFi.status() != WL_CONNECTED){
    delay(1000);
    return;
  }

  for (byte i = 0; i < 6; i++) key.keyByte[i] = 0xFF;

  if (!mfrc522.PICC_IsNewCardPresent() || !mfrc522.PICC_ReadCardSerial()) return;

  Serial.print(F("Card UID:"));
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.println();

  Serial.print(F("PICC type: "));
  MFRC522::PICC_Type piccType = mfrc522.PICC_GetType(mfrc522.uid.sak);
  Serial.println(mfrc522.PICC_GetTypeName(piccType));

  byte messageLength = 36;
  byte readId[messageLength];
  byte readDate[messageLength];
  byte readName[messageLength];
  ReadFromBlock(1, readId);
  ReadFromBlock(2, &readId[18]);
  ReadFromBlock(4, readDate);
  ReadFromBlock(5, &readDate[18]);
  ReadFromBlock(8, readName);
  ReadFromBlock(9, &readName[18]);

  String stringId;
  String stringDate;
  String stringName;

  for (byte i = 0; i < messageLength; i++) {
    if (i == 16 || i == 17 || i == 34 || i == 35) continue;
    stringId += (char)readId[i];
  }
  for (byte i = 0; i < messageLength; i++) {
    if (i == 16 || i == 17 || i == 34 || i == 35) continue;
    stringDate += (char)readDate[i];
  }
  for (byte i = 0; i < messageLength; i++) {
    if (i == 16 || i == 17 || i == 34 || i == 35) continue;
    stringName += (char)readName[i];
  }
  stringId.trim();
  stringDate.trim();
  stringName.trim();
  Serial.print("ID: ");
  Serial.println(stringId);

  PostToAPI(stringId, stringDate, stringName);

  delay(500);  //change value if you want to read cards faster

  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();

  Serial.println();
  Serial.println();
  Serial.println();
}

void PostToAPI(String stringId, String stringDate, String stringName) {
  WiFiClient client;
  HTTPClient http;

  http.begin(client, serverName + "/kanban/bom");
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  String payloadString = "product_code=" + stringId ;
  int responseCode = http.POST(payloadString);
  Serial.println(responseCode);
  http.end();
}

void ReadFromBlock(int blockNum, byte readData[]) {
  MFRC522::StatusCode status;
  status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, blockNum, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("PCD_Authenticate() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }

  byte READLEN = 18;

  status = mfrc522.MIFARE_Read(blockNum, readData, &READLEN);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("MIFARE_Read() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  readData[16] = ' ';
  readData[17] = ' ';
}

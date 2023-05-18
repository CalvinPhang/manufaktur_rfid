#include <TM1637.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// Wifi
const char* ssid = "CALVIN-Student";
const char* password = "CITStudentsOnly";

const char* serverName = "http://10.252.240.21:8000/kanban/bom/display";

String sensorReadings;

StaticJsonDocument<256> doc;

TM1637 TM1;
TM1637 TM2;
TM1637 TM3;
TM1637 TM4;
TM1637 TM5;
// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastTime = 0;
// Timer set to 10 minutes (600000)
//unsigned long timerDelay = 600000;
// Set timer to 5 seconds (5000)
unsigned long timerDelay = 1000;

void setup() {
   // Wifi Setup
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
   // Serial Monitor
  Serial.begin(115200);
  TM1.begin(2, 4, 4); // clk, dio, jumlah angka
  TM2.begin(16, 17, 4);
  TM3.begin(5, 18, 4);
  TM4.begin(19, 21, 4);
  TM5.begin(22, 23, 4);

  TM1.displayClear();
  TM2.displayClear();
  TM3.displayClear();
  TM4.displayClear();
  TM5.displayClear();
}

void loop() {
  //Send an HTTP POST request every 10 minutes
  if(WiFi.status()== WL_CONNECTED){
    HTTPClient http;

    String serverPath = serverName;
        http.begin(serverPath.c_str());
      
      int httpResponseCode = http.GET();
      
      if (httpResponseCode>0) {
        Serial.print("HTTP Response code: ");
        Serial.println(httpResponseCode);
        String payload = http.getString();
        DeserializationError error = deserializeJson(doc, payload);
      
        int bolt = doc["Bolt"];
        int blacknut = doc["Black Nut"];
        int blackwasher = doc["Black Washer"];
        int silvernut = doc["Silver Nut"];
        int silverwasher = doc["Silver Washer"];

        TM1.displayInt(bolt);
        TM2.displayInt(blacknut);
        TM3.displayInt(blackwasher);
        TM4.displayInt(silvernut);
        TM5.displayInt(silverwasher);
      
        Serial.println(blacknut);
        Serial.println(blackwasher);
        Serial.println(silvernut);
        Serial.println(silverwasher);
        Serial.println(bolt);
      }
      else {
        Serial.print("Error code: ");
        Serial.println(httpResponseCode);
      }
      // Free resources
      http.end();
    }
    else {
      Serial.println("WiFi Disconnected");
    }
    delay(1000);
}
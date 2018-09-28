#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 7 //I'm defining what pin to use

#define DHTTYPE DHT11 //We're using the DHT11

DHT dht(DHTPIN, DHTTYPE);  
int smokeDetectorA0 = A1; //Defines the pin used by the smoke detector
const int sensorMin = 0;

void setup() {
  Serial.begin(9600);
  pinMode(smokeDetectorA0, INPUT);
  dht.begin();
}

void loop() {
  delay(2000);
  int analogSensor = analogRead(smokeDetectorA0);

  float humidity = dht.readHumidity();
  float temp = dht.readTemperature();
  float fahrenheit = dht.readTemperature(true);
  
  if (isnan(humidity) || isnan(temp) || isnan(fahrenheit)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  Serial.print("Humidity: ");
  Serial.print(humidity);
  delay(1000);
  Serial.print("fahrenheit: ");
  Serial.print(temp);
  delay(1000);
  Serial.print("Gas Detector: ");
  Serial.print(analogSensor);
}

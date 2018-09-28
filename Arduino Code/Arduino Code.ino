#include <DHT.h>
#include <DHT_U.h>
#include <SPI.h>
#include <Ethernet.h>

#define DHTPIN 7 //I'm defining what pin to use

#define DHTTYPE DHT11 //We're using the DHT11

DHT dht(DHTPIN, DHTTYPE);  
int fireDetectorA0 = A0; //Defines the pin used by the fire detector
const int sensorMin = 0;     // fire sensor minimum
const int sensorMax = 1024;  // fire sensor maximum
int sensormq135 = 4; //Gas sensor LPG, i-butane, propane, methane, alcohol, hydrogen and smoke
int sensorValue = 0;//Gas sensor
//Defines the Arduinos mac address
byte mac[] = {
  0x00, 0xAA, 0xBB, 0xCC, 0xDE, 0x02
};
EthernetClient client;


void setup() {
    if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    // no point in carrying on, so do nothing forevermore:
    for (;;)
      ;
  }
  // print your local IP address:
  Serial.begin(9600);
  pinMode(fireDetectorA0, INPUT);
  pinMode(sensormq135, INPUT);
  dht.begin();
  pinMode(8, OUTPUT); //buzzer
  printIPAddress();  
}

void printIPAddress()
{
  Serial.print("My IP address: ");
  for (byte thisByte = 0; thisByte < 4; thisByte++) {
    // print the value of each byte of the IP address:
    Serial.print(Ethernet.localIP()[thisByte], DEC);
    Serial.print(".");
  }

  Serial.println();
}

void loop() {
  delay(2000);
  int analogSensor = analogRead(fireDetectorA0);
  int fireSensorReading = analogRead(A0); 

  float temp = dht.readTemperature();
  float fahrenheit = dht.readTemperature(true);
  
  if (isnan(temp)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  int range = map(fireSensorReading, sensorMin, sensorMax, 0, 3);
  delay(1000);
  Serial.print("/////");
  Serial.print("temperature: ");
  Serial.print(temp);
  Serial.print("///////");
  delay(1000);
  sensormq135 = analogRead(1);
  Serial.println("Gas Sensor: ");
  Serial.println(sensormq135, DEC);
  Serial.println("////////");
  delay(1000);
  switch (range) {
  case 0:    // A fire closer than 1.5 feet away.
    Serial.println("** Close Fire **");
    digitalWrite(8, HIGH);
    delay(4000);
    digitalWrite(8, LOW);

    break;
  case 1:    // A fire between 1-3 feet away.
    Serial.println("** Distant Fire **");

    break;
  case 2:    // No fire detected.
    Serial.println("No Fire");
    break;
  }
  delay(1000);
}

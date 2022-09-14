#include<DHT.h>
#define DHTPIN 5 // what pin we're connected to
#define DHTTYPE DHT11 // DHT 11 (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal Microcontroller

//Variables

float hum; //Stores humidity value
float temp; //Stores temperature value

void setup()
{
Serial.begin(9600);
dht.begin();
}

void loop()
{
delay(1000);
//Read data and store it to variables hum and temp
hum = dht.readHumidity();
temp= dht.readTemperature();
//Print temp and humidity values to serial monitor
Serial.print("Humidity: ");// "humidity: 75"
Serial.print(hum);
Serial.print(" %, Temp: ");
Serial.print(temp);
Serial.println(" Celsius");
delay(3000); //Delay 3 sec.
}
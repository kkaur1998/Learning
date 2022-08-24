const int trigPin = 5;
const int echoPin = 4;
long duration;
int distance;
void setup(){
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);;
  duration = pulseIn(echoPin,HIGH);
  distance = (duration/2)*(0.034);
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println("cm");
  //Serial.println(duration);
  delay(500);
}